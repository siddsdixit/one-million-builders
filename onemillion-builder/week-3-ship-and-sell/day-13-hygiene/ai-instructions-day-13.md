# Day 13 Verification Prompt

**How to use:** Paste this entire prompt into your coding harness from your project folder.

---

You are a OneMillion course verifier. Today is Day 13 — Production Hygiene Audit.

## What to verify

**File system checks:**

1. **`.onemillion/audit-day-13.md` exists** and documents all 9 audit checks.

2. **All 9 checks marked complete** in the audit document.

3. **`.env.local` is gitignored.** Check `.gitignore`. Also: `git log --all --full-history -- .env.local` should return empty (no history of the file).

4. **gitleaks scan passes.** Run `gitleaks detect --source . --no-banner 2>&1 | tail -5` and report — should say "no leaks found" or "0 secrets found".

5. **No hidden routes.** List `app/` directories. Flag any of: `/admin`, `/internal`, `/debug`, `/test`, `/dev`. If found, ask the builder if they're protected by role checks.

**Code checks (grep through codebase):**

6. **No hardcoded API keys.** Grep for patterns: `sk-ant-`, `sk-proj-`, `eyJ...` (long JWT-looking strings outside .env files). All matches should be in .env files only.

7. **Errors normalized.** Look at API route files. If any return `error.message` or `error.stack` directly in the response, flag as potential leak.

8. **AI rate limit present.** API route should have logic that counts user's calls and returns 429 if over limit.

**Manual checks (ask the builder):**

9. **RLS audit.** Ask: "Did you verify every Supabase table has RLS enabled AND a policy that references auth.uid()?"

10. **🚨 Re-confirm cross-user test.** Ask: "Did you re-run the cross-user test today (User B incognito tries to see User A's data)? Confirm it still passes."

11. **Rate limit triggered.** Ask: "Did you temporarily lower your AI rate limit, trigger it, and confirm it returned 429?"

12. **Hidden routes addressed.** Ask: "If you have any admin/test/debug routes, are they protected by role checks (not just hidden links)?"

## Report format

```
# Day 13 Verification Report

## File System Checks
- [ ] / [x] audit-day-13.md exists with 9 checks
- [ ] / [x] .env.local gitignored
- [ ] / [x] No .env.local in git history
- [ ] / [x] gitleaks scan clean
- [ ] / [x] No hidden routes

## Code Checks
- [ ] / [x] No hardcoded secrets in code
- [ ] / [x] Errors normalized (no raw messages)
- [ ] / [x] AI rate limit present

## Manual Checks
- [ ] / [x] All tables have RLS + correct policies
- [ ] / [x] Cross-user test passes
- [ ] / [x] Rate limit verified working
- [ ] / [x] No unprotected admin routes

## Result
PASS or NEEDS REVISION

## Feedback
(If PASS: encouragement + Day 14 preview)
(If NEEDS REVISION: priority. Most critical:
  - "gitleaks found exposed credentials — rotate IMMEDIATELY"
  - "Cross-user test fails — RLS broken on table X"
  - "Errors leak internals — wrap in try/catch")
```

## After verification

If PASS:
- Save report to `.onemillion/verification-day-13.md`
- Tell builder: "Day 13 verified. App is launch-safe. Tomorrow: custom domain."

If NEEDS REVISION:
- Security issues first
- Be specific about what file / which check fails

Begin verification.
