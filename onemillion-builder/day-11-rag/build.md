# Day 11 — Build Guide

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Time: 1-2 hours. Add retrieval to your AI route.**

---

## Before You Start

- [ ] Day 10 verified — tool use working
- [ ] You know which user data the AI should access (review Day 7 spec's "Input" section)

---

## Step 1: Identify The Data You Need

Look at your AI Feature Spec from Day 7, the "Input" section. What context does the AI need?

Common examples:
- The specific entity being acted on (one deliverable, one habit, one project)
- Related entities (the client for this deliverable, history)
- User profile / preferences
- Recent activity / timeline

Pick the MINIMUM you need. Less context = faster + cheaper + more focused AI output.

---

## Step 2: Add Retrieval To Your API Route

```bash
claude
```

Paste:

```
I'm on Day 11 of OneMillion. Add RAG (retrieval) to my AI route at
app/api/ai/[my-feature]/route.ts.

The AI needs to know about: [list the data — e.g., "the deliverable they
selected, the client associated with it, and the last 3 communications"]

Update the route to:
1. After auth check, fetch the relevant rows from Supabase
   (use the server-side client, RLS will enforce user-scoping)
2. Convert the fetched data into a structured text summary
   (NOT raw JSON — a prose paragraph the AI can use)
3. Inject that summary as part of the system prompt OR as a context message
4. Update the system prompt to reference the available context
5. Handle the "no results" case (don't make up data — tell AI to ask user)

Show me the updated file.
```

---

## Step 3: Review The Retrieval Pattern

Open the updated route. The pattern should look like:

```typescript
// 1. Auth
const supabase = createClient();
const { data: { user } } = await supabase.auth.getUser();
if (!user) return new Response('Unauthorized', { status: 401 });

// 2. Get request input
const { deliverableId } = await req.json();

// 3. Retrieve — RLS auto-filters by user
const { data: deliverable } = await supabase
  .from('deliverables')
  .select('*, clients(*)')  // join client info
  .eq('id', deliverableId)
  .single();

if (!deliverable) {
  return Response.json({ error: 'Not found' }, { status: 404 });
}

// 4. Summarize into prose
const context = `Deliverable: ${deliverable.name}
Status: ${deliverable.status}
Due: ${deliverable.due_date}
Client: ${deliverable.clients.name} (${deliverable.clients.industry || 'industry unknown'})
Last update: ${deliverable.last_updated_at}`;

// 5. Inject into prompt
const result = streamText({
  model: anthropic('claude-3-5-sonnet-20241022'),
  system: `You are a client communications assistant for freelance designers.
  
  Context for this request:
  ${context}
  
  Use the context to make your output specific. Don't invent details — if
  you need info not provided, ask the user.
  
  [rest of system prompt]`,
  messages: [{ role: 'user', content: userPrompt }],
  tools: { ... }
});
```

If your route looks meaningfully different from this pattern, ask Claude to align.

---

## Step 4: Test That AI Uses The Data

Click your AI button in the UI. The output should now reference:
- Specific entity names (not generic placeholders)
- Specific dates / statuses from your data
- Specific people / clients from your DB

Bad (no RAG): "Here's a draft follow-up email for your client..."
Good (RAG working): "Hi Jen, Just following up on the new website project — we're at 60% with the wireframes done. Aiming to wrap up the homepage mockup by Friday..."

The good version is only possible if the AI got Jen + 60% + Friday from your DB.

---

## Step 5: 🚨 Cross-User RAG Test (CRITICAL)

This is the day's security gate. Same pattern as Day 6, applied to RAG.

1. Sign in as User A. Create some data (deliverables, clients, whatever).
2. Trigger your AI feature as User A. Confirm output references User A's data. ✅
3. Sign out. Sign in as a brand new User B (incognito).
4. Trigger your AI feature as User B.
5. **You should NOT see** any of User A's data in User B's AI output.
6. If you DO see User A's data in User B's output: **stop**. Your RAG retrieval isn't filtering by user. Fix before continuing.

The fix is usually: use the server-side Supabase client (`createClient()` from `lib/supabase/server.ts`) which respects the user's session. NOT the service_role client (which bypasses RLS).

---

## Step 6: Deploy + Test Live

```bash
git add .
git commit -m "Day 11: RAG added"
git push
```

Test on Vercel URL. Confirm RAG works AND cross-user test still passes.

---

## Step 7: Run Day 11 Verification

```bash
claude
```

Ask your harness to run the OneMillion verifier for this day.

---

## What Should Be True After Day 11

- [ ] API route fetches user-specific data BEFORE calling AI
- [ ] Retrieval uses server-side Supabase client (RLS enforced)
- [ ] Fetched data is converted to prose context (not raw JSON)
- [ ] Context is injected into system prompt
- [ ] "No results" case is handled (AI told to ask, not invent)
- [ ] AI output visibly uses the user's actual data
- [ ] Cross-user test passed (User B never sees User A's data)
- [ ] Live URL works
- [ ] Verification passed ✅

---

## Update Orchestrator State

Before you close today, ask the orchestrator to update `.onemillion/state.json`:

- **Current day:** Day 11 complete
- **Last verified day:** Day 11
- **Current blocker:** None, or the exact blocker to resume from
- **Next smallest action:** Open Day 12.

If verification did not pass yet, keep **Last verified day** at the previous passed day and write the blocker clearly.

## If You Are Stuck

Open your coding harness from your project folder:

```bash
claude
```

Paste this:

```text
I am on OneMillion Day 11.

Here is the step I was trying to complete:
[paste the step heading or instructions]

Here is what happened:
[paste the error, terminal output, or describe what I see]

Diagnose the likely cause and give me the next smallest action.
Do not rewrite unrelated code.
Ask for one missing detail at a time if needed.
```

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| AI output still generic, ignores context | Context isn't reaching the AI. Add `console.log(context)` before the streamText call. |
| Retrieval returns empty (`data` is null) | Either no rows match OR RLS blocking. Check Supabase logs. |
| Cross-user test shows leaked data | You're using service_role client somewhere. Switch to server client with user session. |
| Output references wrong user's data | Same — auth context isn't propagating. |
| Costs spiked (>2x normal) | Your context is too big. Limit retrieval (e.g., last 3 messages, not last 30). |
| AI hallucinates info that wasn't in context | System prompt isn't explicit enough. Add: "Only use information from the Context section. If something isn't there, ask the user." |
| Slow first token (>3 sec) | Retrieval + AI call combined. Optimize: do retrieval in parallel if possible. |

---

→ **Done with Day 11?** Move to [Day 12 — Lock The AI Feature](../day-12-lock-ai/learn.md).
