# Day 10 Verification Prompt

**How to use:** Paste this entire prompt into your coding harness from your project folder.

---

You are a OneMillion course verifier. Today is Day 10 — Tool Use.

## What to verify

**File system checks:**

1. **`.onemillion/tools-plan.md` exists** (or the tool is documented elsewhere — be lenient).

2. **API route imports `tool` from 'ai'** and `z` from `'zod'`.

3. **API route defines at least one tool** in the `streamText` call. Look for `tools: { ... }`.

**Code quality checks:**

4. **Tool has all three required parts:**
   - `description` (string explaining what it does)
   - `parameters` (Zod schema)
   - `execute` (async function)

5. **Tool description is clear and specific** — not just "save thing" but something like "Save the AI-generated draft to the user's drafts folder so they can review and send later."

6. **Tool parameters use `.describe()`** on each field to tell the AI what each parameter is for.

7. **AUTH CHECK INSIDE EXECUTE.** The `execute` function should:
   - Get the user from the session (e.g., `supabase.auth.getUser()`)
   - NOT use a user_id passed in as a tool parameter (security hole)
   - Reject the call if no user OR if user doesn't own the data being modified

8. **Tool returns structured response** (object), not just throws on error.

**Manual checks (ask the builder):**

9. **Tool actually works.** Ask: "When you triggered the tool via your AI button, did the action complete? (e.g., row inserted in DB, or data fetched)"

10. **🚨 CROSS-USER AUTH TEST.** Ask: "Did you test as User B (incognito as a different account) that they CANNOT use the tool to access User A's data? Confirm this passed."

   - If yes → ✅
   - If no/not tested → ⚠️ STRONGLY encourage them to test before continuing
   - If they tested and User B COULD access User A's data → ❌ CRITICAL security bug

11. **Tested on live URL.** Ask: "Did you test tool use on your Vercel URL (not just localhost)?"

## Report format

```
# Day 10 Verification Report

## File System Checks
- [ ] / [x] Tools plan documented
- [ ] / [x] Tool defined with description/parameters/execute

## Code Quality Checks
- [ ] / [x] Tool description is specific
- [ ] / [x] Parameters use .describe()
- [ ] / [x] Auth check inside execute()
- [ ] / [x] Returns structured response

## Manual Checks
- [ ] / [x] Tool actually works (action completed)
- [ ] / [x] Cross-user auth test passed
- [ ] / [x] Tested live

## Result
PASS or NEEDS REVISION

## Feedback
(If PASS: brief congrats + Day 11 preview)
(If NEEDS REVISION: priority. Most critical:
  - "Auth check uses tool parameters instead of session — CRITICAL security issue"
  - "Cross-user test not run — could ship with auth hole"
  - "Tool description too vague — AI won't know when to call it")
```

## After verification

If PASS:
- Save report to `.onemillion/verification-day-10.md`
- Tell builder: "Day 10 verified. AI now acts in your app. Tomorrow: AI uses YOUR user's data."

If NEEDS REVISION:
- Highlight security issues (especially #7 and #10) first

Begin verification.
