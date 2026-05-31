# Day 6 — Build Guide

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Time: 1.5–3 hours. The biggest day of Days 1-6.**

You're building your main feature end-to-end. Take breaks. Drink water.

---

## Before You Start

- [ ] Day 5 verified (auth + first table + RLS)
- [ ] You know your main entity (from PRD Section 3)
- [ ] You've reviewed your PRD's Definition of Done so you know what "done" means today
- [ ] Both terminal windows ready

---

## Step 1: Verify Your Table Has The Right Columns (10 min)

From Day 5, you created a table for your main entity. Look at your PRD's user stories — what fields does the user actually need?

For example, if the user story is "see all deliverables I owe across all clients," the table needs:
- `name` (the deliverable name)
- `client_name` (which client)
- `due_date` (when it's due)
- `status` (todo/in-progress/done)
- `user_id` (RLS)
- `id`, `created_at` (auto)

Open Supabase dashboard: https://supabase.com/dashboard

Choose your project → Table Editor → your table → add any missing columns now.

> 💡 **Don't overthink columns.** Add what you need. You can add more later. Start with 4-6 columns.

---

## Step 2: Build The API Routes (30-45 min)

```bash
claude
```

If you're going Big Bang (Approach A from learn.md):

```
I'm on Day 6 of OneMillion. I need full CRUD API routes for my entity called
"[your-entity-name]" — Supabase table with columns [list columns].

Create these route handlers using Next.js App Router conventions:

1. POST /api/[entity] — create a new one (auth required, sets user_id)
2. GET /api/[entity] — list all of mine (RLS does the filter)
3. GET /api/[entity]/[id] — get one by id
4. PUT /api/[entity]/[id] — update one
5. DELETE /api/[entity]/[id] — delete one

Use my existing Supabase server client. Handle errors properly — return
401 if not logged in, 404 if not found, 200/204 on success.

Show me each file before creating.
```

Claude shows the plan. Review. Say "Yes, create them."

If you're going piece by piece (Approach B):

```
I'm on Day 6. Build just the POST /api/[entity] route handler. Should:
- Require auth (use my server Supabase client)
- Accept JSON body with the entity fields
- Insert into Supabase with the current user's id
- Return the created row

Show me the code before creating the file.
```

Repeat for GET, PUT, DELETE.

---

## Step 3: Build The UI Page (45-60 min)

Once API routes are working, build the page that uses them.

```
Build a UI page at /[entity] that lets the logged-in user:

1. See a list of their [entities] (call GET /api/[entity])
2. Add a new one via a form at the top (call POST /api/[entity])
3. Update each one's status via a dropdown (call PUT /api/[entity]/[id])
4. Delete each one via a button (call DELETE /api/[entity]/[id])

Use Tailwind for styling. Handle:
- Loading state (spinner)
- Empty state ("No [entities] yet — add your first one!")
- Error state ("Something went wrong")

Don't make it pretty. Make it functional. Make it work.
```

Review what Claude generates. If it's importing React hooks like `useState` and `useEffect`, that's expected.

---

## Step 4: Test Everything Locally (20 min)

```bash
npm run dev
```

In your browser:

1. Log in
2. Go to `/[your-entity]` (e.g., `/deliverables`)
3. **You should see:** Empty state ("No deliverables yet")
4. Add one via the form
5. **You should see:** It appears in the list
6. Update its status via the dropdown
7. **You should see:** Status changes immediately
8. Delete it via the button
9. **You should see:** It disappears

If all this works locally, you're 70% done.

---

## Step 5: 🚨 SECURITY GATE — Test As A SECOND USER (10 min)

**⛔ DO NOT PUSH TO PRODUCTION UNTIL THIS PASSES.** This is the security gate. If you skip it, you risk shipping an app where any user can see every other user's data. That's a real security breach, real legal exposure, real reputational damage. Take 10 minutes. Test.

1. Open an incognito/private window
2. Go to your live URL — sign up as a NEW user (`test2@example.com`)
3. Navigate to `/[your-entity]`
4. **You should see:** EMPTY. No data from your first user.

If the second user sees the first user's data: **RLS is broken.** Critical bug. Fix before moving on.

How to fix RLS issues:
- Open Supabase dashboard: https://supabase.com/dashboard
- Choose your project → Table Editor → your table → Policies
- Make sure RLS is enabled (toggle is green)
- Make sure your policy uses `auth.uid() = user_id`
- Make sure your API route INSERTs include `user_id: user.id`

---

## Step 6: Deploy + Test Live (10 min)

```bash
git add .
git commit -m "Day 6: Core feature CRUD"
git push
```

Wait 30-60 seconds for Vercel to redeploy.

Go to your live URL. Repeat the full test (signup, add, edit, delete, second user check).

If everything works in production: **Days 1-6 is done.**

---

## Step 7: Run Day 6 Verification

```bash
claude
```

Ask your harness to run the OneMillion verifier for this day.

The verifier will:
- Check API route files exist
- Check the entity page exists
- Try to fetch the live URL
- Ask you to confirm the incognito test passed

---

## What Should Be True After Day 6

- [ ] API routes exist: POST, GET, PUT, DELETE for your entity
- [ ] A UI page exists where the user can do all CRUD operations
- [ ] Everything works on your **live URL** (not just localhost)
- [ ] A second user (incognito) sees no data from the first user (RLS working)
- [ ] Loading, empty, and error states are handled
- [ ] You committed and pushed all changes
- [ ] Verification passed ✅

---

## Update Orchestrator State

Before you close today, ask the orchestrator to update `.onemillion/state.json`:

- **Current day:** Day 6 complete
- **Last verified day:** Day 6
- **Current blocker:** None, or the exact blocker to resume from
- **Next smallest action:** Open Day 7.

If verification did not pass yet, keep **Last verified day** at the previous passed day and write the blocker clearly.

## If You Are Stuck

Open your coding harness from your project folder:

```bash
claude
```

Paste this:

```text
I am on OneMillion Day 06.

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
| `400 Bad Request` when inserting | Your INSERT is missing `user_id` or another required field. Check API route logs. |
| `401 Unauthorized` | The API route isn't using the server-side Supabase client with the user's session. Ask Claude: "Why is my API returning 401? Show me how to use the server client with the user's session." |
| `403 Forbidden` (RLS rejection) | The row's `user_id` doesn't match the current user. Make sure you're INSERTing with `user.id`. |
| List shows nothing even though I added items | RLS too strict OR your SELECT is wrong. Open Supabase dashboard: https://supabase.com/dashboard, then test the SQL directly in SQL Editor. |
| Page renders blank | Probably a JavaScript error. Open browser DevTools (F12) → Console tab. The error tells you where. Paste into Claude for the fix. |
| Form submits but nothing happens | Likely a network error or wrong API URL. DevTools → Network tab → click your request → see the response. |
| Status update doesn't persist | You're updating local state but not calling PUT. OR the PUT route is broken. Test the route directly with curl. |
| Incognito test shows other user's data | RLS not enabled or policy is wrong. Re-do Step 5 of Day 5. |

---

## Celebrate (Seriously)

You just finished **Days 1-6**. You have:
- A live, deployed product on the internet
- Real authentication
- A real database with proper security
- A real, working feature
- 6 days of commits in a GitHub repo

This is more than most people accomplish in months of trying to build things. Take 10 minutes. Make a coffee. Look at your URL. You earned this.

---

→ **Done with Day 6?** Move to [Day 7 — AI Feature Spec](../day-07-ai-spec/learn.md). Before you start, review your PRD's "out of scope" list and resist adding extra features.
