# Day 9 Verification Prompt

**How to use:** Paste this entire prompt into your coding harness from your project folder.

---

You are a OneMillion course verifier. Today is Day 9 — Streaming UI.

## What to verify

**File system checks:**

1. **API route uses streaming.** Read the AI route file. Confirm it imports/uses `streamText` (not `generateText`).

2. **Edge runtime configured.** API route should have `export const runtime = 'edge';` (or `'nodejs'` if they have a reason — but Edge is preferred for streaming).

3. **UI uses streaming hook.** Find the page/component that has the AI button. Confirm it imports `useCompletion` from `'ai/react'`.

4. **`useCompletion` is used correctly.** It should:
   - Be called with `api: '/api/ai/...'`
   - Have its return values (`completion`, `isLoading`, `error`, `complete`) used in the component

**UI state checks:**

5. **Loading state exists.** Look for rendering tied to `isLoading` — should show some skeleton/loading indicator.

6. **Empty state exists.** Look for rendering tied to empty `completion` — should show placeholder/hint text.

7. **Error state exists.** Look for rendering tied to `error` — should show:
   - An error message (using `error.message` or similar)
   - A retry button (should call `complete()`)

**Manual checks (ask the builder):**

8. **Streaming visibly works.** Ask: "When you click the AI button, do you SEE the tokens appearing progressively (one at a time), or does the full output appear at once?"

   - "Progressively" → ✅
   - "All at once" → ❌ — likely `generateText` still in use OR Edge runtime missing

9. **Loading indicator appears within 100ms.** Ask: "When you click the button, do you see a loading indicator appear immediately, or is there a delay before anything happens?"

10. **Tested on Vercel live URL.** Ask: "Did you confirm streaming works on your deployed Vercel URL, not just localhost?"

**Optional remote check:**

11. If the builder shares their Vercel URL, do a POST request to the AI endpoint (with valid auth) and check response headers for `text/event-stream` or similar streaming Content-Type. (May not be feasible from every coding harness; skip if difficult.)

## Report format

```
# Day 9 Verification Report

## File System Checks
- [ ] / [x] API route uses streamText
- [ ] / [x] Edge runtime configured
- [ ] / [x] UI imports useCompletion from ai/react
- [ ] / [x] useCompletion used with correct api prop

## UI State Checks
- [ ] / [x] Loading state present (skeleton/indicator)
- [ ] / [x] Empty state present (hint text)
- [ ] / [x] Error state present (message + retry button)

## Manual Checks
- [ ] / [x] Streaming visibly works (tokens appear progressively)
- [ ] / [x] Loading indicator appears within 100ms
- [ ] / [x] Tested on live URL

## Result
PASS or NEEDS REVISION

## Feedback
(If PASS: encouragement + Day 10 preview)
(If NEEDS REVISION: priority. Most critical:
  - "Output appears all at once — not actually streaming. Check streamText is used."
  - "Edge runtime missing — works locally, breaks on Vercel"
  - "No retry button on error — user has no recovery path")
```

## After verification

If PASS:
- Save report to `.onemillion/verification-day-09.md`
- Tell builder: "Day 9 verified. Your AI feels alive. Tomorrow: AI takes actions."

If NEEDS REVISION:
- Be specific about which state is missing or broken

Begin verification.
