# Day 9 — Streaming UI

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Days 7-12 | ~45-90 min | Make AI feel alive**

---

## Learning Frame

- **Mental model:** Streaming makes AI feel alive because users see progress immediately.
- **What can go wrong:** You break a working AI route while changing the response shape.
- **What to ignore today:** Ignore multi-turn chat; stream the existing feature.

## What You'll Have After Today

- **AI output that streams token-by-token** in your UI (text appears as it's generated)
- A proper loading state (skeleton or animated indicator before tokens start arriving)
- Polished error handling (specific error messages, retry button)
- That "AI app feel" — the one Claude.ai and ChatGPT have

This is a small change technically. It's a huge change for how your app feels.

---

## Video Walkthrough

Video walkthrough: coming soon. The written guide is complete.

---

## Part 1: Why Streaming Matters (~10 min read)

Yesterday's Day 8 implementation worked like this:

```
User clicks "Draft Update"
  → frontend shows "Generating..." for 3-5 seconds
    → AI finishes generating the FULL response server-side
      → response sent back to frontend
        → user sees the full output appear all at once
```

This is correct but **feels dead.** The user waits 4 seconds staring at nothing, then BOOM, 200 words appear. They think something broke. They click the button again. They wait another 4 seconds.

**Streaming changes the experience:**

```
User clicks "Draft Update"
  → frontend shows "Generating..." for 200-300ms
    → first tokens stream from AI
      → "Hi" appears
        → "Sarah," appears
          → "Thanks" appears
            → "for" appears (etc., token by token)
              → user reads while AI generates
                → output complete in same 4 seconds
```

Same total time. **Completely different feel.** The user sees progress immediately. The app feels alive. They never wonder if it's broken.

Every premium AI product (Claude.ai, ChatGPT, Cursor, etc.) streams. It's table stakes for an AI-native UI.

---

## Part 2: How Streaming Works Under The Hood (~10 min read)

**Server-side:** Instead of `generateText()` which returns the full response when done, we use `streamText()` which returns a *stream* — a series of small chunks (tokens) sent as soon as they're generated.

**Network:** The chunks travel via Server-Sent Events (SSE) — an HTTP standard for sending updates from server to client without keeping a connection "open" the way websockets do. The browser receives chunks as they arrive.

**Client-side:** Instead of `fetch()` + waiting for the whole JSON response, we use the Vercel AI SDK's `useCompletion()` or `useChat()` React hook, which manages the streaming state for us — including a `completion` string that updates in real-time as chunks arrive.

You don't write the streaming protocol code. The SDK does it. You just opt in by using the streaming methods.

---

## Part 3: Loading + Empty + Error States (~10 min read)

This is the day you also nail the **three states every AI UI must handle.**

### Loading State
**Before:** Button shows "Generating..." text.
**After (better):** Animated skeleton, typing dots, or progress indicator. Visible from the millisecond the button is clicked.

The loading state should be visible **within 100ms of click.** If the user clicks and nothing happens for 500ms, they think the click didn't register. They click again. Now your code runs twice.

### Empty State (first time using feature)
Before the user clicks the AI button for the first time, what does the area look like?

Bad: completely empty space (looks broken)
Good: Light hint text like "Click 'Draft Update' to generate an email with AI" or a placeholder showing what the output will look like.

### Error State
AI calls fail. Sometimes the network drops. Sometimes Anthropic is rate-limited. Sometimes your prompt has a syntax error.

Bad: red text saying "Error" with no detail
Good: Specific error ("Rate limit reached — try again in 30 seconds" or "Network error — check your connection") + a retry button

The Vercel AI SDK gives you a `error` state in its hooks. Use it.

---

## Today's Assignment

In [build.md](./build.md):
1. Update your Day 8 API route to use `streamText()` instead of `generateText()`
2. Update your UI to use `useCompletion()` hook from Vercel AI SDK
3. Add a proper loading skeleton (visible <100ms)
4. Add an empty state with helpful placeholder text
5. Add an error state with retry button
6. Test the full streaming flow on live URL

---

## What Good Looks Like

After Day 9, the user experience should be:

1. User loads the page → empty state with hint text visible
2. User clicks "Draft Update" → loading skeleton appears within 100ms
3. Within 300ms → first tokens start appearing
4. Tokens stream in over 3-4 seconds → user can read along
5. Streaming finishes → "Copy" button appears
6. If anything errors → clear message + retry button

That's the AI-native experience. Premium feel. Same backend cost. Wildly more engaging UI.

---

## Common Mistakes (Today)

1. **Using `generateText` instead of `streamText`.** Easy to miss. The two are nearly identical in syntax, but only `streamText` actually streams.

2. **No loading state.** Or a loading state that takes 500ms+ to appear. The user perceives "broken" before they perceive "thinking."

3. **Empty state is literally empty.** Looks like a bug. Even a placeholder text saying "Your draft will appear here" is better than nothing.

4. **Error swallowed silently.** The AI failed, the user has no idea why. Always surface the error visually.

5. **Streaming works locally but breaks on Vercel.** Usually a Next.js runtime issue. Add `export const runtime = 'edge'` to your route file. Edge runtime supports streaming natively.

---

## What Should Be True After Day 9

- [ ] API route uses `streamText` (not `generateText`)
- [ ] UI uses `useCompletion` from `ai/react`
- [ ] Tokens appear progressively (visible during streaming, not all at once)
- [ ] Loading skeleton appears within 100ms of click
- [ ] Empty state has helpful placeholder
- [ ] Error state has specific error message + retry button
- [ ] Streaming works on your LIVE URL (Edge runtime configured if needed)
- [ ] Verification passed ✅

---

## Verify Your Day 9

Ask your harness to run the OneMillion verifier for this day.
- Check API route uses streaming
- Verify UI uses streaming hook
- Confirm loading/empty/error states exist
- Test live URL response includes streaming headers
- Report pass / needs revision

---

## Share It

```
✅ Day 9 done: AI streams live in my app. Feels like a real product now.
🎯 Tomorrow: AI takes actions (tool use)
#BuildingWith1M
```

---

## Go Deeper

- **[Vercel AI SDK Streaming](https://sdk.vercel.ai/docs/ai-sdk-core/generating-text#streamtext)** — official
- **[`useCompletion` hook](https://sdk.vercel.ai/docs/reference/ai-sdk-ui/use-completion)** — what you'll use in UI
- **[Server-Sent Events MDN](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)** — the underlying protocol

---

→ **Next:** [Day 10 — Tool Use](../day-10-tool-use/learn.md)
