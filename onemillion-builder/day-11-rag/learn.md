# Day 11 — RAG (AI Reads Your User's Data)

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Days 7-12 | ~1-2 hours | Make the AI personalized**

---

## Learning Frame

- **Mental model:** RAG means retrieving the right user data and injecting it into the prompt.
- **What can go wrong:** You leak another user’s data or retrieve irrelevant context.
- **What to ignore today:** Ignore vector databases unless simple SQL cannot serve the feature.

## What You'll Have After Today

- An AI feature **grounded in your user's actual data** — not generic
- Understanding of **RAG (Retrieval-Augmented Generation)** — the pattern behind every "AI that knows your data" product
- A working retrieval step in your API route: fetch from DB → inject into prompt → call AI
- The "wait, the AI actually knows me" moment for your users

This is what separates novelty AI ("write me a poem") from useful AI ("write me a follow-up email to MY client about MY deliverable").

---

## Video Walkthrough

Video walkthrough: coming soon. The written guide is complete.

---

## Part 1: What Is RAG? (~10 min read)

RAG = **Retrieval-Augmented Generation**.

The pattern:
```
1. User asks something
2. Your code FETCHES relevant data from your DB
3. Your code INJECTS that data into the prompt
4. AI uses the data to generate a grounded response
```

Without RAG, your AI is operating on "general knowledge from training" + whatever the user typed. With RAG, your AI knows the user's actual data — their clients, their projects, their habits, their emails, whatever.

### Two Mental Models

**The "Open Book Test" Model**
Without RAG: AI takes a test from memory. Sometimes confidently wrong.
With RAG: AI takes the same test with their notes open. Reads the relevant chapter before answering.

**The "Pre-Briefing" Model**
Without RAG: You ask a consultant a question cold.
With RAG: You first send the consultant a packet of relevant context, then ask the question.

---

## Part 2: Two Flavors Of RAG (~10 min read)

### Flavor 1: Simple SQL RAG
Your data lives in tables. Fetch the relevant rows. Inject as text into the prompt.

When to use: structured data, clear relevance criteria.

Example:
```
User asks: "Draft a follow-up to Acme about the new website project"
Your code:
  - Fetches Acme's profile from clients table
  - Fetches the "new website" project from deliverables table
  - Fetches the last 3 communications with Acme
Prompt becomes:
  "Here's what we know:
   Client: Acme. Industry: SaaS. Contact: Jen.
   Deliverable: New website. Status: in-progress. Due: 2026-06-01.
   Last 3 messages: [recent emails]
   
   Now: draft a follow-up email about the new website."
```

**This is what we're building today.** Simple. Works. Covers 80% of real-world RAG needs.

### Flavor 2: Vector / Semantic RAG
Your data is unstructured (long documents, articles, knowledge bases). You can't query "find the relevant rows" because relevance is semantic, not categorical.

You use a **vector database** that stores text embeddings and lets you query "find chunks similar to this question."

When to use: knowledge bases, documents, "ask my files," etc.

**You don't need this today.** It is an advanced path for later. The simple SQL approach is more useful for most products.

---

## Part 3: Why RAG > Just Bigger AI (~5 min read)

A common mistake: "the AI doesn't know my data, let me train a bigger model" or "let me fine-tune."

That's almost always wrong. Reasons:

1. **Fine-tuning is expensive and slow.** You re-train every time your data changes (constantly).
2. **You don't get isolation.** If you fine-tune on User A's data, User B's queries can leak User A's data through model weights.
3. **Quality is worse.** Fine-tuned models tend to perform worse on the underlying task while supposedly learning new "facts."
4. **RAG just works.** Stuff the relevant data into the prompt at call time. Done.

The right way to make an AI "know your data": **retrieve relevant pieces, inject them into the prompt.** That's RAG. That's what every premium AI product does (Cursor, Claude.ai with projects, Notion AI, etc.).

---

## Part 4: The RLS Connection (~5 min read)

RAG without proper auth = data leak.

If User A asks "summarize my deliverables" and your retrieval code does `SELECT * FROM deliverables`, you're feeding User B's deliverables into User A's prompt. Then the AI's response to User A might include User B's data.

**Always filter retrieval by the current user.** Either:
- Use Supabase's server client with the user's session (RLS automatically filters)
- Or manually `.eq('user_id', currentUser.id)` in every query

Day 5 set up RLS specifically so that this is easy. Day 11 cashes that check.

If you skipped the RLS gate on Day 5 — go back and fix it before continuing.

---

## Today's Assignment

In [build.md](./build.md):
1. Pick ONE place in your AI feature where user data matters
2. Add a retrieval step before the AI call: fetch the relevant rows from Supabase (with RLS)
3. Inject the fetched data as context in your prompt
4. Test that the AI's output references the user's actual data
5. Cross-user test: User B's prompt does NOT include User A's data

---

## What Good Looks Like

After Day 11, an interaction looks like this:

```
User A clicks "Draft Update" on her Acme project
  → Your API route runs
  → Auth check: get User A from session ✅
  → Retrieval: SELECT * FROM deliverables WHERE id = X AND user_id = User A
  → Retrieval: SELECT * FROM clients WHERE id = Acme's id AND user_id = User A
  → Retrieval: SELECT * FROM messages WHERE client_id = Acme's id AND user_id = User A
  → Prompt includes:
      System: "You are a client comms assistant..."
      Context: "Sarah's client Acme. Last project status: 60% done.
                Previous communications: [summarized]"
      User: "Draft a follow-up update"
  → AI generates an email that includes the project name, the right status,
    references the last message
  → Sarah reads the output and thinks: "wait, the AI knows about Acme"
```

That's the moment your product crosses from "novelty AI demo" to "real AI tool I'd use."

---

## Common Mistakes (Today)

1. **Stuffing too much context.** "Let me give the AI EVERYTHING about the user" → prompt is 50K tokens, cost spikes 10x, AI gets confused. Filter to ONLY what's relevant for this specific request.

2. **Skipping RLS / auth filter.** The #1 RAG bug. Always filter retrieval by current user.

3. **Putting raw DB output in the prompt.** Raw JSON from Supabase is verbose. Summarize the relevant fields into prose: not `{ "client": { "name": "Acme", ... } }` but `"Client: Acme (SaaS company, contact Jen)"`.

4. **No "no results" handling.** What if retrieval finds nothing? AI shouldn't make up data. Tell it in the prompt: "If the context is empty, ask the user for more info instead of guessing."

5. **Forgetting to update Quality Criteria from Day 7.** Now that AI has access to user data, your quality criteria can be tighter: "AI output must reference the client by name" is now verifiable AND should pass 100% of the time.

---

## What Should Be True After Day 11

- [ ] AI route fetches at least 1 piece of user-specific data before calling AI
- [ ] Retrieval uses server-side Supabase client (RLS enforced)
- [ ] Retrieved data is injected as context in the prompt (not as raw JSON)
- [ ] AI output visibly uses the user's data (mentions client name, deliverable status, etc.)
- [ ] Cross-user test: User B's AI calls never include User A's data
- [ ] Live URL works
- [ ] Verification passed ✅

---

## Verify Your Day 11

Ask your harness to run the OneMillion verifier for this day.

---

## Share It

```
✅ Day 11 done: AI knows MY user's actual data. Output is personalized.
🎯 Tomorrow: lock acceptance criteria, hit cost budget
#BuildingWith1M
```

---

## Go Deeper

- **[RAG Primer](https://docs.langchain.com/docs/use-cases/question-answering/)** — the canonical explanation
- **[Anthropic + RAG](https://docs.anthropic.com/en/docs/build-with-claude/embeddings)** — when you need vector search later
- **[Pinecone Learn](https://www.pinecone.io/learn/)** — when you graduate to vector DBs
- **[Supabase Vector](https://supabase.com/docs/guides/ai)** — if you want vectors inside your current stack later

---

→ **Next:** [Day 12 — Lock The AI Feature](../day-12-lock-ai/learn.md)
