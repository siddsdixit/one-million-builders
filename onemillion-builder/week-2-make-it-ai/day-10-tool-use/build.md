# Day 10 — Build Guide

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="../README.md">Week Overview</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Time: 1-2.5 hr. Add tool use to your AI route.**

---

## Before You Start

- [ ] Day 9 verified — streaming works
- [ ] You've picked ONE tool to add today (start small)

---

## Step 1: Plan The Tool

In `.onemillion/tools-plan.md`, write down:

```markdown
## Tool 1: [tool_name]

**Purpose:** [What does it do?]

**Type:** [Read-only / Write]

**Parameters:**
- param1 (type, required, description)
- param2 (type, optional, description)

**What it returns:** [Shape of the data]

**Auth check:** [How does it verify the user can do this action?]

**Failure mode:** [What happens if it fails?]
```

Example:

```markdown
## Tool 1: save_email_draft

**Purpose:** After the AI generates a follow-up email, save it as a draft in
the user's drafts table so they can review and send later.

**Type:** Write

**Parameters:**
- client_id (number, required, the client this draft is for)
- subject (string, required, email subject)
- body (string, required, email body text)

**What it returns:** { success: true, draft_id: number } OR { success: false, error: string }

**Auth check:** Verify the user owns the client_id (lookup clients table where
client_id = X AND user_id = currentUserId; if no row, return 403).

**Failure mode:** If insert fails, return { success: false, error: "Could not save" }.
AI should tell user to try again.
```

---

## Step 2: Implement The Tool

```bash
claude
```

Paste:

```
I'm on Day 10 of OneMillion. Add tool use to my AI route at
app/api/ai/[my-feature]/route.ts.

Here's the tool I want to add:
[paste contents of .onemillion/tools-plan.md]

Update the route to:
1. Import `tool` from 'ai' and `z` from 'zod'
2. Define the tool with description, parameters (zod schema), and execute function
3. Pass the tool to streamText({ tools: { [tool_name]: ... } })
4. Update the system prompt to mention the tool is available
5. In the execute function: verify the user has permission BEFORE taking action
6. Return success/error from execute

Show me the file before saving.
```

Review the diff. Pay attention to:
- The auth check inside `execute()` — the user_id should come from the session, NOT from the tool parameters
- The Zod schema — should match what you wrote in tools-plan.md
- The system prompt update — should mention WHEN to use the tool

---

## Step 3: Test The Tool

Use your UI's AI button. Make a request that should trigger the tool.

For our example: in the UI, click "AI: Draft Update to Acme" → AI generates email → AI should automatically call `save_email_draft` → check your DB to confirm the row was inserted.

Open Supabase → Table Editor → drafts table. **You should see:** a new row with the AI-generated content.

---

## Step 4: Test Auth (CRITICAL)

The tool should refuse to do anything for another user's data. Test this:

1. Sign in as User A
2. Make an AI request that calls the tool with client_id=42 (User A's client)
3. ✅ Should work — tool saves draft
4. Note the draft_id created (e.g., draft_id=99)
5. Sign out, sign in as User B (different account)
6. Make an AI request that attempts to manipulate draft_id=99 OR client_id=42 (User A's data)
7. ✅ Should fail — tool returns error or empty

If User B can access User A's data via the tool, your auth check is broken. Fix before continuing.

---

## Step 5: Deploy + Test Live

```bash
git add .
git commit -m "Day 10: First tool added"
git push
```

Test the tool on live URL. Verify it works AND auth works.

---

## Step 6: Run Day 10 Verification

```bash
claude
```

Paste contents of [`ai-instructions-day-10.md`](./ai-instructions-day-10.md).

---

## What Should Be True After Day 10

- [ ] `.onemillion/tools-plan.md` exists with at least 1 tool documented
- [ ] API route defines the tool with `tool({ description, parameters, execute })`
- [ ] System prompt mentions the tool
- [ ] Tool's execute function checks auth using session user_id (not from AI parameters)
- [ ] Tool actually changes data when called
- [ ] User A's tool calls can't touch User B's data (cross-user test passed)
- [ ] Live URL has tool working
- [ ] Verification passed ✅

---

## Update Your Progress Tracker

Before you close today, open `.onemillion/progress.md` and update:

- **Current day:** Day 10 complete
- **Last verified day:** Day 10
- **Current blocker:** None, or the exact blocker to resume from
- **Next smallest action:** Open Day 11.

If verification did not pass yet, keep **Last verified day** at the previous passed day and write the blocker clearly.

## If You Are Stuck

Open your coding harness from your project folder:

```bash
claude
```

Paste this:

```text
I am on OneMillion Day 10.

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
| AI never calls the tool | Tool description is too vague. Make it explicit. Also: system prompt should hint at when the tool is useful. |
| AI calls tool with wrong parameters | Zod schema is too loose. Add `.describe()` to each field to tell AI what it's for. |
| Tool runs but data isn't saved | `execute` function has a bug. Add `console.log` at each step. Check Vercel logs. |
| Auth check passes when it shouldn't | You're using the user_id from tool parameters instead of from the session. Always pull from `auth.getUser()`. |
| Tool works locally, fails on Vercel | Same env var or Edge runtime issue as Day 9. Check logs. |
| AI hallucinates a tool that doesn't exist | The `tools` object passed to `streamText` only includes the tools you defined. AI can only call those. If you see this: probably a different bug. |

---

→ **Done with Day 10?** Move to [Day 11 — RAG](../day-11-rag/learn.md).
