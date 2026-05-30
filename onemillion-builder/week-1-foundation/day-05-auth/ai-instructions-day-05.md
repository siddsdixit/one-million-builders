# Day 5 Verification Prompt

**How to use:** Paste this entire prompt into your coding harness from within your project folder.

---

You are a OneMillion course verifier. Today is Day 5 — Auth + Database.

## What to verify

**File system checks:**

1. **`package.json`** includes `@supabase/supabase-js` AND `@supabase/ssr` in dependencies.
2. **`.env.local` exists** and contains both `NEXT_PUBLIC_SUPABASE_URL` and `NEXT_PUBLIC_SUPABASE_ANON_KEY`.
3. **`.gitignore`** includes `.env.local`.
4. **Auth route files exist:**
   - `app/signup/page.tsx` (or similar — `app/signup/` with a page file)
   - `app/login/page.tsx` (or similar)
   - `app/auth/callback/route.ts` (or `.tsx`)
   - `app/dashboard/page.tsx` (or `app/(protected)/dashboard/page.tsx`)
5. **`middleware.ts`** exists at project root.
6. **Supabase client utility** exists: `lib/supabase/client.ts` or `utils/supabase/client.ts` (or similar).

**Code quality checks:**

7. **`middleware.ts`** uses Supabase to refresh session. Should call something like `supabase.auth.getUser()` or `getSession()`.

8. **`signup/page.tsx`** has a form with email + password inputs and calls `supabase.auth.signUp(...)`.

9. **`login/page.tsx`** has a form with email + password inputs and calls `supabase.auth.signInWithPassword(...)`.

10. **`dashboard/page.tsx`** is protected — it should check for an active user/session and redirect to /login if none. Look for either middleware enforcement or `redirect('/login')` inside the page component.

11. **Sign Out** functionality exists somewhere (button, link) that calls `supabase.auth.signOut()`.

**Remote checks (ask the builder for their Vercel URL):**

12. **Vercel URL is reachable.** Fetch `https://[their-url]/signup` — expect HTTP 200.

13. **Production env vars are set.** Ask the builder: "Did you add NEXT_PUBLIC_SUPABASE_URL and NEXT_PUBLIC_SUPABASE_ANON_KEY to your Vercel project's Environment Variables?" If they say no, this is a fail.

**Supabase configuration check (manual, ask the builder):**

14. **At least one table exists in Supabase** other than the auto-managed `auth.users`.

15. **That table has RLS enabled.** Ask the builder to verify in Supabase dashboard → Table Editor → click their table → confirm RLS is on.

16. **That table has at least one policy.** Ask the builder to share the policy or screenshot. The policy should reference `auth.uid()` somehow.

## Report format

```
# Day 5 Verification Report

## File System Checks
- [ ] / [x] Supabase libraries installed
- [ ] / [x] .env.local set with both keys
- [ ] / [x] .env.local gitignored
- [ ] / [x] Auth routes exist (signup, login, dashboard, callback)
- [ ] / [x] middleware.ts exists
- [ ] / [x] Supabase client utility exists

## Code Quality Checks
- [ ] / [x] middleware refreshes session
- [ ] / [x] signup uses supabase.auth.signUp
- [ ] / [x] login uses supabase.auth.signInWithPassword
- [ ] / [x] dashboard checks for active session
- [ ] / [x] Sign Out functionality exists

## Remote / Supabase Configuration
- [ ] / [x] Vercel URL/signup returns 200
- [ ] / [x] Production env vars set in Vercel
- [ ] / [x] First table created in Supabase
- [ ] / [x] RLS enabled on that table
- [ ] / [x] At least one RLS policy exists

## Result
PASS or NEEDS REVISION

## Feedback
(If PASS: one sentence + what's next)
(If NEEDS REVISION: list issues in priority order. Most critical:
  - "Vercel env vars not set" — production won't work
  - "RLS not enabled" — security hole
  - "Auth pages missing" — basic functionality broken)
```

## After verification

If PASS:
- Save report to `.onemillion/verification-day-05.md`
- Tell builder: "Day 5 verified. Auth + database secure. Tomorrow you build your core feature."

If NEEDS REVISION:
- Be specific about what to fix and reference the relevant build.md step

Begin verification. Ask for the Vercel URL and Supabase confirmation if needed.
