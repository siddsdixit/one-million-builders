# Day 13 — Build Guide

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="../README.md">Week Overview</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Time: 1-2 hours. Run the 9-point audit. Fix what's broken.**

---

## Before You Start

- [ ] Week 2 done — AI feature locked + tested
- [ ] Terminal open in your project

---

## Step 1: Install gitleaks (Secret Scanner)

```bash
# Mac
brew install gitleaks

# Windows (Git Bash)
# Download from https://github.com/gitleaks/gitleaks/releases
```

Run the scan:

```bash
cd ~/my-onemillion-build
gitleaks detect --source . --verbose
```

**You should see:** `0 leaks found` (or "No leaks found").

If leaks ARE found: that's a real problem. Each leak is a real credential exposed. Fix:
1. Rotate the leaked credential (regenerate from Anthropic / Supabase / etc.)
2. Remove from git history using `git filter-repo` (more complex — ask Claude for help)
3. Re-run gitleaks to confirm clean

---

## Step 2: Audit RLS Per Table

Open Supabase → Table Editor.

For EACH table you have, click it. Look at:
- **RLS indicator:** should be green (enabled). If not, click "Enable RLS."
- **Policies tab:** should have at least one policy.

For each policy, verify:
- `USING` expression includes `auth.uid() = user_id` (or equivalent)
- `WITH CHECK` expression for INSERT/UPDATE also includes the check

Document in `.onemillion/audit-day-13.md`:

```markdown
## RLS Audit
- deliverables: ✅ RLS on, policy: auth.uid() = user_id
- clients: ✅ RLS on, policy: auth.uid() = user_id
- ai_call_log: ✅ RLS on, policy: auth.uid() = user_id
```

---

## Step 3: Re-Run Cross-User Test

Open incognito. Create a brand new User B account.

For each main feature (your CRUD entity + your AI feature):
- As User B, try to see / modify User A's data
- Should fail / return empty

If anything leaks: RLS policy is wrong somewhere. Find and fix.

---

## Step 4: Verify Rate Limits

Supabase Auth: dashboard → Authentication → Rate Limits. Confirm signup/login rates are reasonable (defaults are fine).

Your AI rate limit (from Day 12): test it. Temporarily set the cap to 2. Try 3 calls. The 3rd should fail with 429. Restore to 100 (or your real limit).

Add IP-level rate limiting if you don't have it yet:

```bash
claude
```

```
Add IP-level rate limiting to my AI API route. If an IP makes more than
60 AI calls per hour (regardless of user), return 429. This catches abuse
before they even sign up.

Use Vercel's built-in `@vercel/kv` if available, or a simple in-memory
counter for now (acceptable for Cohort 0 scale).
```

---

## Step 5: Normalize Errors

```
Audit my API routes for error leakage. Specifically:
1. Find any `throw new Error(...)` that exposes internal info
2. Find any `return Response.json({ error: error.message })` patterns
3. Wrap them in a generic 500 with "Internal error — please try again"
4. Log the real error server-side for my debugging

Show me the changes.
```

---

## Step 6: Search For Hidden Routes

```bash
ls app
# Look for any folders like /admin, /test, /debug, /internal
# Delete or protect them
```

If you have admin functionality: it should check the user's role/permissions, not just hide the link.

---

## Step 7: Confirm .env.local Is Gitignored

```bash
cat .gitignore | grep ".env"
# Should show: .env.local AND .env (both)

git log --all --full-history -- .env.local
# Should show: nothing (empty output)

git log --all --full-history -- .env
# Should show: nothing (empty output)
```

If either shows commits: there's secret history. Use `git filter-repo` to remove (or ask Claude).

---

## Step 8: Write The Audit Document

Create `.onemillion/audit-day-13.md` summarizing all 9 checks + any fixes you made. Use the template from learn.md.

---

## Step 9: Commit + Push + Verify

```bash
git add .
git commit -m "Day 13: Production audit passed"
git push
```

```bash
claude
```

Paste contents of [`ai-instructions-day-13.md`](./ai-instructions-day-13.md).

---

## What Should Be True After Day 13

- [ ] gitleaks scan clean
- [ ] All tables have RLS + policies
- [ ] Cross-user test passes
- [ ] Rate limits work (Supabase auth + your AI route + IP-level)
- [ ] Error responses don't leak internals
- [ ] No hidden admin/debug routes
- [ ] .env files gitignored, no history
- [ ] `.onemillion/audit-day-13.md` documents everything
- [ ] Verification passed ✅

---

## Update Your Progress Tracker

Before you close today, open `.onemillion/progress.md` and update:

- **Current day:** Day 13 complete
- **Last verified day:** Day 13
- **Current blocker:** None, or the exact blocker to resume from
- **Next smallest action:** Open Day 14.

If verification did not pass yet, keep **Last verified day** at the previous passed day and write the blocker clearly.

## If You Are Stuck

Open your coding harness from your project folder:

```bash
claude
```

Paste this:

```text
I am on OneMillion Day 13.

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
| gitleaks finds leaks | Rotate the credential. Use `git filter-repo` to remove from history. Re-scan. |
| RLS test shows User B sees data | Policy is wrong. Check policy is `(auth.uid() = user_id)` not `(true)`. |
| Rate limit doesn't trigger | Logic issue — log the count. May be checking the wrong user. |
| Error normalization breaks tests | Errors return 500 with no info now. Add server-side logging so YOU still see the real error in Vercel logs. |
| Can't get rid of .env from git history | `git filter-repo` is the safest tool. If you've never used it, ask Claude to walk you through. |

---

→ **Done with Day 13?** Move to [Day 14 — Custom Domain](../day-14-domain/learn.md).
