# Day 8 — Build Guide

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="../README.md">Week Overview</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Time: 1-2 hours. Your first real AI call.**

---

## Before You Start

- [ ] Day 7 verified — AI feature spec locked
- [ ] You have `ANTHROPIC_API_KEY` in your Anthropic console (from getting-your-api-key.md)
- [ ] Both terminal windows ready

---

## Step 1: Install The AI SDK

We'll use **Vercel AI SDK** — it's a clean abstraction over Anthropic, OpenAI, Google, etc. Lets you swap models with one line if needed.

```bash
npm install ai @ai-sdk/anthropic
```

**You should see:** `added 23 packages` or similar.

> 🔧 **Engineers:** You can use raw `@anthropic-ai/sdk` if you prefer. The course uses Vercel AI SDK because it handles streaming better (matters Day 9) and the syntax is cleaner. Both work.

---

## Step 2: Add Anthropic Key To Env Vars

In `.env.local`:

```
ANTHROPIC_API_KEY=sk-ant-your-actual-key-here
```

**Note:** No `NEXT_PUBLIC_` prefix. This must stay server-side only.

Then add the same to Vercel:
1. vercel.com → your project → Settings → Environment Variables
2. Add `ANTHROPIC_API_KEY` with your key value
3. Save

> 🚨 **Critical:** Never use `NEXT_PUBLIC_` for `ANTHROPIC_API_KEY`. That would expose your key to anyone who opens DevTools on your site.

---

## Step 3: Use Your Coding Harness To Build The Route

```bash
claude
```

Paste:

```
I'm on Day 8 of OneMillion. I need to build an API route that calls Claude.

Here's my AI Feature Spec:
[paste contents of .onemillion/ai-feature.md]

Create:
1. app/api/ai/[your-feature-slug]/route.ts — a POST route that:
   - Verifies the user is authenticated (uses my Supabase server client)
   - Receives the input fields from the request body
   - Constructs a prompt using my spec's role/goal/tone/constraints/format
   - Calls Claude using Vercel AI SDK + @ai-sdk/anthropic
   - Returns the response as JSON

Use Claude Sonnet 4 (or Haiku if my cost budget is tight).
Use generateText (not streamText — streaming is tomorrow's Day 9).
Add error handling: return 401 if not authed, 500 if Anthropic fails.

Show me the file before creating.
```

Claude shows the plan. Review it. Note especially: the prompt construction.

---

## Step 4: Review The Prompt Construction

Open the new route file. Find the part where the prompt is built. It should look like:

```typescript
const systemPrompt = `You are a [role from your spec]. 
Your goal: [goal].
Tone: [tone].
Constraints:
- [constraint 1]
- [constraint 2]
...
Format: [format].`;

const userMessage = `[whatever context the user provides]`;
```

If the prompt isn't clearly structured with all 5 elements, ask Claude to rewrite:

```
The prompt in this route is too vague. Rewrite it with all 5 elements
explicitly labeled: Role, Goal, Tone, Constraints, Format. Use my AI
Feature Spec to fill in the details.
```

---

## Step 5: Add A Button In Your UI

Pick a page in your app where the AI feature makes sense (e.g., on the deliverable detail page if it's a "draft update" feature).

Tell Claude:

```
Add a button to [path to relevant page] that:
1. Calls POST /api/ai/[my-feature]
2. Sends [whatever the user's context is — the relevant entity ID, etc.]
3. Shows "Generating..." while waiting
4. Displays the AI response in a text area below the button
5. Has a "Copy" button next to the output
6. Handles errors gracefully ("Something went wrong. Please try again.")
```

Save. `npm run dev` should still be running in your first terminal — refresh your browser.

---

## Step 6: Test Locally

1. Log in
2. Navigate to the page with the AI feature
3. Click your AI button
4. Wait 2-5 seconds
5. **You should see:** real AI-generated output appearing in the text area

If it works locally: 70% done.

---

## Step 7: Deploy + Test Live

```bash
git add .
git commit -m "Day 8: First AI call working"
git push
```

Wait 30-60 sec for Vercel deploy.

Visit your LIVE URL. Test the AI feature on production.

> 🚨 **If it works locally but not on Vercel:** ANTHROPIC_API_KEY isn't set in Vercel. Add it. Trigger redeploy.

---

## Step 8: Run Day 8 Verification

```bash
claude
```

Paste contents of [`ai-instructions-day-08.md`](./ai-instructions-day-08.md).

---

## What Should Be True After Day 8

- [ ] `ai` and `@ai-sdk/anthropic` in package.json
- [ ] `ANTHROPIC_API_KEY` in `.env.local`
- [ ] `ANTHROPIC_API_KEY` in Vercel (verify in dashboard)
- [ ] API route exists at `app/api/ai/[your-feature]/route.ts`
- [ ] Route checks auth (returns 401 if no user)
- [ ] Prompt has all 5 elements (role/goal/tone/constraints/format)
- [ ] No `NEXT_PUBLIC_ANTHROPIC` anywhere in code (security)
- [ ] Button in UI works on LIVE URL
- [ ] AI output appears in UI
- [ ] Verification passed ✅

---

## Update Your Progress Tracker

Before you close today, open `.onemillion/progress.md` and update:

- **Current day:** Day 8 complete
- **Last verified day:** Day 8
- **Current blocker:** None, or the exact blocker to resume from
- **Next smallest action:** Open Day 9.

If verification did not pass yet, keep **Last verified day** at the previous passed day and write the blocker clearly.

## If You Are Stuck

Open your coding harness from your project folder:

```bash
claude
```

Paste this:

```text
I am on OneMillion Day 08.

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
| `401 Unauthorized` from Anthropic | API key wrong or expired. Check console.anthropic.com → API Keys. |
| `429 Rate Limit` | You're calling Claude too fast. Add a delay or upgrade Anthropic tier. |
| `Insufficient credits` | Add funds at console.anthropic.com → Billing. |
| API returns 500 with no detail | Add `console.error(error)` in the catch block. Check Vercel function logs. |
| Output is empty | Your prompt or user input is empty. Add a console.log to check both. |
| Output is generic / not useful | Prompt is too vague. Re-read Day 7 spec, tighten the prompt. |
| Works locally, breaks in production | ANTHROPIC_API_KEY not in Vercel. Add it. |
| Output costs more than expected | Switch to Claude Haiku (`@ai-sdk/anthropic` lets you specify the model). |

---

→ **Done with Day 8?** Move to [Day 9 — Streaming UI](../day-09-streaming/learn.md). Tomorrow we make the output appear live.
