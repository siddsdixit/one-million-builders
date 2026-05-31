# Day 13 — Production Hygiene

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Days 13-18 | ~1-2 hours | The audit before launch**

---

## Learning Frame

- **Mental model:** Production hygiene removes the obvious ways a real user can get hurt or stuck.
- **What can go wrong:** You treat security, errors, and rate limits as optional polish.
- **What to ignore today:** Ignore new features; harden the product you have.

## What You'll Have After Today

- A **9-point production audit** passed on your app
- **All secrets** out of code, in env vars only
- **RLS audit** complete — every table, every policy verified
- **Rate limits** in place on auth + AI endpoints
- **Error normalization** — no stack traces leaking to users
- A clean conscience before showing real humans your product

This is the unglamorous day. No new features. Just making sure nothing embarrassing happens when real people sign up.

---

## Video Walkthrough

Video walkthrough: coming soon. The written guide is complete.

---

## Part 1: Why This Day Matters (~10 min read)

You've built a working product. Real users are 4 days away. **What could embarrass you?**

- ❌ Your Anthropic API key visible in your GitHub repo
- ❌ User A can see User B's data via a missed RLS rule
- ❌ A bot signs up 10,000 times in an hour and consumes your monthly Anthropic budget
- ❌ Your app crashes and shows a 500 page with a Python-looking stack trace
- ❌ You ship a feature that works for you but breaks on anyone's iPhone Safari

Most launched products have at least one of these. Some have all five. Day 13 is the safety net.

This is the fourth pillar of agentic SDLC: **production hygiene from day 1**. Most courses save this for "if you have time." OneMillion makes it mandatory. The Builder Wall doesn't admit products that ship with these holes.

---

## Part 2: The 9-Point Production Audit (~15 min read)

Each check is binary. Pass or fail. Day 13 doesn't end until all 9 pass.

### 1. No Secrets In Git
Search your codebase for hardcoded keys, tokens, passwords. Any string starting with `sk-`, `eyJ`, or matching a known token pattern. There should be none. All secrets in `.env.local` (gitignored) and Vercel env vars.

### 2. RLS On Every Table
Open Supabase dashboard: https://supabase.com/dashboard

Choose your project → Table Editor. Every table should have RLS enabled (green indicator) AND at least one policy. Service-only tables (admin) should explicitly DENY anon.

### 3. RLS Policies Are Correct
For each table, the policy should reference `auth.uid()`. Test with: log in as User B in incognito, try to access User A's data — must fail.

### 4. Rate Limit On Auth
Open Supabase dashboard: https://supabase.com/dashboard

Choose your project → Authentication → Rate Limits. Supabase has built-in rate limits on signup/login. Verify they're enabled. Default: ~30/hour per IP for signup.

### 5. Rate Limit On AI Endpoints
You added a per-user daily cap on Day 12. Verify it's still working. Add IP-level rate limits too (covers abuse before auth).

### 6. Errors Don't Leak Internals
Trigger an error in your API route (e.g., bad input). User-facing response should be a generic "Something went wrong" — NOT a stack trace, file paths, or database error text.

### 7. .env.local Is Gitignored
Run `git status`. `.env.local` should NEVER appear in staged files. Run `git log --all --full-history -- .env.local` — should show NO history.

### 8. CORS / Same-Origin Locked
Your API routes should only accept requests from your own domain. Vercel sets this by default for same-origin Next.js apps. Verify by trying to call your API from a different origin (e.g., curl with a fake Origin header) — should fail.

### 9. No Hidden Admin Routes
Walk through your app's routes. Any `/admin`, `/internal`, `/debug` paths? They should be either: removed, or protected behind admin role checks (not just "if you know the URL").

---

## Part 3: The "Three Categories Of Breach" Mental Model (~5 min read)

Three types of things can go wrong. The audit covers all three.

### Category 1: Credential Leaks
Your secrets visible to attackers. Mitigated by checks 1, 7.

### Category 2: Authorization Failures
Users seeing data they shouldn't. Mitigated by checks 2, 3, 9.

### Category 3: Abuse
Bots / bad actors burning your resources. Mitigated by checks 4, 5.

### Category 4: Information Disclosure
Your app accidentally telling the user too much. Mitigated by checks 6, 8.

Cover these four categories and you've covered ~90% of what real apps get burned by. The other 10% is exotic (timing attacks, supply chain, etc.) — beyond Day 13.

---

## Today's Assignment

In [build.md](./build.md):
1. Run all 9 audit checks
2. Fix any that fail
3. Fix what is unsafe and let the verifier record the result in `.onemillion/state.json`
4. Run Day 13 verification

---

## What Good Looks Like

After Day 13, your code/config should show:

```markdown
# Day 13 — Production Audit

## Results
1. ✅ No secrets in git — gitleaks scan clean
2. ✅ RLS on every table (6 tables, all enabled)
3. ✅ RLS policies correct — incognito cross-user test passed
4. ✅ Supabase auth rate limit on — 30/hour default
5. ✅ AI rate limit confirmed (per-user, 100/day; also added IP-level 60/hour)
6. ✅ Errors normalized — added error handler middleware, no stack traces
7. ✅ .env.local gitignored, no history
8. ✅ CORS verified — cross-origin requests rejected
9. ✅ No admin routes (removed /test page that I had)

## Issues Found + Fixed
- Found `.env` (not `.env.local`) in repo — added to gitignore, removed from history with git filter-branch
- Found error in `/api/deliverables/[id]` route that returned raw Postgres error message — wrapped in generic 500 response

## Audit Pass — Date: 2026-05-12
```

---

## Common Mistakes (Today)

1. **Marking pass without testing.** Each check needs an actual test, not a "feels right." Especially RLS — the only real test is incognito as User B.

2. **Fixing only the symptom.** You found one stack trace leaking? Don't just fix that route. Add a global error handler.

3. **Skipping the gitleaks scan.** Builders assume "I never committed a secret." 30% of the time they're wrong. Run the scan. Use `gitleaks detect --source .` or similar.

4. **Forgetting CORS.** Next.js defaults are usually OK, but if you added custom CORS for any reason, audit it.

5. **Removing admin routes by deleting links, not the route file.** If `/admin` page still exists at the file system, someone can navigate there. Delete the file, not just the link.

---

## What Should Be True After Day 13

- [ ] All 9 audit checks pass
- [ ] guard checks pass in code/config and `.onemillion/state.json`
- [ ] Any issues found are FIXED (not just noted)
- [ ] Cross-user RLS test passed AGAIN (re-confirm)
- [ ] Verification passed ✅

---

## Verify Your Day 13

Ask your harness to run the OneMillion verifier for this day.
- Scan code for hardcoded secrets
- Walk through your audit document
- Verify the 9 checks
- Probe for common holes
- Report pass / needs revision

---

## Share It

```
✅ Day 13 done: production audit passed. App is safe for real users.
🎯 Tomorrow: custom domain ✨
#BuildingWith1M
```

---

## Go Deeper

- **[OWASP Top 10](https://owasp.org/www-project-top-ten/)** — the canonical list of web app vulnerabilities
- **[Supabase Security Checklist](https://supabase.com/docs/guides/database/secure-data)** — official
- **[Vercel Security Headers](https://vercel.com/docs/security/headers)** — defense in depth
- **[Anthropic Best Practices](https://docs.anthropic.com/en/docs/build-with-claude/prompt-injection)** — AI-specific risks

---

→ **Next:** [Day 14 — Custom Domain](../day-14-domain/learn.md)
