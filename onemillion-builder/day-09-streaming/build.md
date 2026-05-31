# Day 9 — Build Guide

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Time: 45-90 min. Convert your Day 8 implementation to stream.**

---

## Before You Start

- [ ] Day 8 verified — first AI call working
- [ ] Both terminals open; `npm run dev` running

---

## Step 1: Convert Your API Route To Streaming

In your coding harness:

```bash
claude
```

Paste:

```
I'm on Day 9 of OneMillion. My API route at app/api/ai/[my-feature]/route.ts
currently uses generateText() — needs to use streamText() so the UI can stream
tokens.

Update the route to:
1. Use streamText() instead of generateText() (from the 'ai' package)
2. Return result.toDataStreamResponse() (compatible with useCompletion hook)
3. Add `export const runtime = 'edge';` at the top (Edge runtime supports
   streaming natively on Vercel — node runtime can be flaky)
4. Keep the auth check + system prompt + error handling

Show me the updated file before saving.
```

Review the diff. The structural change is small — just `streamText` instead of `generateText`, and a different return type.

---

## Step 2: Update Your UI To Stream

```
Update my UI page that has the AI button. It currently uses fetch() and waits
for the JSON response. Switch it to use the useCompletion hook from 'ai/react'.

Specifically:
1. Import { useCompletion } from 'ai/react';
2. Hook into the route: useCompletion({ api: '/api/ai/[my-feature]' })
3. Render { completion } in the output area (it updates token-by-token)
4. Render { isLoading } in the loading state
5. Render { error } in the error state with a Retry button

Keep the input fields and button. Just swap the fetch logic for the hook.
```

---

## Step 3: Polish The Three States

### Loading State
Make sure it appears INSTANTLY when the button is clicked. Tell Claude:

```
The loading state needs to appear within 100ms of clicking the button.
Use the isLoading flag from useCompletion. Render a simple animated
skeleton (3 gray bars of varying widths, pulsing) when isLoading is true
and completion is empty.
```

### Empty State
```
When isLoading is false and completion is empty (initial render),
show: "Click the button above to generate your draft." (or whatever
fits your AI feature). Light gray, italicized.
```

### Error State
```
When error is truthy from useCompletion, show:
- A friendly message ("Something went wrong: [error.message]")
- A "Try Again" button that calls complete() to retry
- If error message contains "rate limit", show extra helper text:
  "We're sending requests too fast. Wait 30 seconds and try again."
```

---

## Step 4: Test Locally

In your browser:
1. Refresh the page
2. **You should see:** Empty state with hint text
3. Click the AI button
4. **You should see:** Loading skeleton appears immediately
5. **Within 300ms:** First tokens appear
6. **Over next 3-4 sec:** Tokens stream in (you can READ them as they arrive)
7. Done — Copy button appears

If tokens still arrive all at once instead of streaming: the Edge runtime export is missing. Re-do Step 1.

---

## Step 5: Test Error Flow

To test error handling: temporarily break the API route (e.g., comment out the auth check OR sign out, then refresh).

Click the button. **You should see:** Error message + retry button.

Restore the route to working state.

---

## Step 6: Deploy + Test Live

```bash
git add .
git commit -m "Day 9: Streaming UI"
git push
```

Wait for Vercel deploy. Test streaming on LIVE URL.

> 🚨 **If streaming works locally but breaks on Vercel:** You forgot `export const runtime = 'edge'`. Add it. Redeploy.

---

## Step 7: Run Day 9 Verification

```bash
claude
```

Ask your harness to run the OneMillion verifier for this day.

---

## What Should Be True After Day 9

- [ ] API route uses `streamText` (not `generateText`)
- [ ] Route has `export const runtime = 'edge';`
- [ ] UI uses `useCompletion` from `ai/react`
- [ ] Tokens appear progressively (you can SEE them streaming)
- [ ] Loading skeleton appears within 100ms
- [ ] Empty state has helpful hint
- [ ] Error state has message + retry button
- [ ] Works on LIVE Vercel URL
- [ ] Verification passed ✅

---

## Update Orchestrator State

Before you close today, ask the orchestrator to update `.onemillion/state.json`:

- **Current day:** Day 9 complete
- **Last verified day:** Day 9
- **Current blocker:** None, or the exact blocker to resume from
- **Next smallest action:** Open Day 10.

If verification did not pass yet, keep **Last verified day** at the previous passed day and write the blocker clearly.

## If You Are Stuck

Open your coding harness from your project folder:

```bash
claude
```

Paste this:

```text
I am on OneMillion Day 09.

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
| Output still appears all at once (not streaming) | API route is still using `generateText` OR Edge runtime not configured. Check both. |
| `useCompletion is not a function` | Update import: `import { useCompletion } from 'ai/react';` (not from `'ai'`). |
| Streaming works locally, fails on Vercel | Add `export const runtime = 'edge';` to API route. |
| Stream cuts off mid-sentence | Anthropic call hit max_tokens. Increase `maxOutputTokens` in `streamText({ ... })`. |
| Loading state never appears | The button is calling something other than the streaming endpoint. Check the `api` prop in `useCompletion`. |
| Error shows but retry button does nothing | Retry button should call `complete()` (not `submit()`). Look at the hook's docs. |
| First token takes too long (>2 sec) | Anthropic Sonnet vs Haiku — switch to Haiku for snappier UX. |
| Token streams but UI doesn't re-render | `completion` from useCompletion is being rendered correctly. Verify with `console.log(completion)`. |

---

→ **Done with Day 9?** Move to [Day 10 — Tool Use](../day-10-tool-use/learn.md). Tomorrow: AI takes actions in your app.
