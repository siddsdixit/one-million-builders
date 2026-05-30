# Day 6 Verification Prompt

**How to use:** Paste this entire prompt into your coding harness from within your project folder.

---

You are a OneMillion course verifier. Today is Day 6 — the core CRUD feature.

## What to verify

**File system checks:**

1. **API routes exist** in `app/api/`. Look for files matching:
   - `app/api/[entity]/route.ts` — handles POST + GET (list)
   - `app/api/[entity]/[id]/route.ts` — handles GET/PUT/DELETE (one)
   (Substitute `[entity]` with whatever the builder's main entity is.)

2. **Page exists** for the entity. Look for `app/[entity]/page.tsx` or similar.

3. **Route handlers use server-side Supabase.** Open the API route files and check that they import from the server-side Supabase utility (typically `lib/supabase/server.ts` or similar). NOT the client-side one. The route should look something like:
   ```ts
   const supabase = createClient()  // server-side
   const { data: { user } } = await supabase.auth.getUser()
   if (!user) return new Response('Unauthorized', { status: 401 })
   ```

**Code quality checks:**

4. **Auth check in POST route.** The POST handler should check for an authenticated user and return 401 if not.

5. **user_id set on INSERT.** When creating a new row, the code should set `user_id` to the current user's id. Look for `.insert({ ..., user_id: user.id })`.

6. **UI page handles loading/empty/error states.** Read the page component. Confirm there's:
   - Some kind of loading indicator while fetching
   - An empty-state message ("No [entities] yet" or similar)
   - An error message if the fetch fails

**Remote checks (ask the builder):**

7. **Vercel URL is live.** Fetch `https://[their-url]` and confirm 200.

8. **Builder confirms incognito test passed.** Ask the builder: "Did you sign up as a second user in incognito and confirm they see NO data from the first user?" 
   - If yes → ✅
   - If no/not tested → ⚠️ critical — they MUST test before moving on
   - If second user DID see data → ❌ RLS is broken, fix before pass

**Manual verification step:**

9. Ask the builder: "Walk me through your live app. Can you sign up, add a [entity], update it, delete it, and confirm data persists across login?" Get a yes or no.

**🚨 SECURITY GATE — HARD FAIL IF NOT PASSED:**

10. **Ask the builder explicitly:** "Did you sign up as a SECOND user in incognito/private mode, navigate to your entity page, and CONFIRM you see no data from the first user?"
    - If yes ✅ AND they can describe what they saw (empty list, "no items yet" message) → PASS
    - If no ❌ OR they say "I'll do it later" → FAIL VERIFICATION, write "RLS gate failed — security risk. Fix before any further course progress."
    - If they say "I tested but saw the other user's data" → CRITICAL FAILURE — guide them to fix the RLS policy immediately.

This is a non-negotiable security gate. The course refuses to advance a builder who hasn't verified RLS works.

## Report format

```
# Day 6 Verification Report

## File System Checks
- [ ] / [x] API routes exist (POST/GET/PUT/DELETE)
- [ ] / [x] Entity page exists
- [ ] / [x] Routes use server-side Supabase client

## Code Quality Checks
- [ ] / [x] Auth check in POST route
- [ ] / [x] user_id set on INSERT
- [ ] / [x] UI handles loading/empty/error

## Remote / Manual Checks
- [ ] / [x] Vercel URL returns 200
- [ ] / [x] Incognito test passed (RLS working)
- [ ] / [x] Full CRUD flow works live

## Result
PASS or NEEDS REVISION

## Feedback
(If PASS: massive congratulations — Week 1 is complete)
(If NEEDS REVISION: specific issues. Most critical:
  - "Incognito test failed — RLS is broken, must fix"
  - "API returning 401 — server client not configured correctly"
  - "Loading state missing — UX is broken")
```

## After verification

If PASS:
- Save report to `.onemillion/verification-day-06.md`
- Write a celebration message: "🎉 Week 1 complete! You have a live, authenticated, secure CRUD app. Week 2 is coming — we'll add AI features."

If NEEDS REVISION:
- Save report to `.onemillion/verification-day-06.md`
- The most common Day 6 failure is RLS — be especially explicit about that

Begin verification now.
