# Day 6 — Core Feature

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Days 1-6 | ~1.5–3 hours | Build the main feature end-to-end**

---

## Learning Frame

- **Mental model:** Your core feature is the smallest useful loop a user can complete.
- **What can go wrong:** You build too many fields or skip the second-user security test.
- **What to ignore today:** Ignore AI and polish; make CRUD work end to end.

## What You'll Have After Today

- **Your core feature working live** — create, read, update, delete
- The "Data → API → UI" pattern in your muscle memory
- A real product, with auth, that users can actually USE
- The end of Days 1-6 — you have a deployable, shareable thing

This is the biggest day of Days 1-6 in terms of code volume. But you're not writing the code — Claude is. You're directing it.

---

## Video Walkthrough

Video walkthrough: coming soon. The written guide is complete.

---

## Part 1: The Data → API → UI Pattern (~10 min read)

Every feature in software follows the same three-step pattern. Once you see it, you see it everywhere. By Day 18 it'll be how you think about every feature you build.

### Step 1: Data
**What does this feature need to remember?**

You design the table. Columns, types, who can see it (RLS). This is what gets stored in Supabase.

### Step 2: API
**What does the app need to be able to do with this data?**

You design the API routes. What does the app receive? What does it do? What does it return? In Next.js, these are files in `app/api/`.

### Step 3: UI
**What does the user see?**

You design the page. Forms for adding data. Lists for showing data. Buttons that call your API. Loading states. Empty states. Error states.

**Example — saving a "favorite":**

| Step | What it looks like |
|------|-------------------|
| **Data** | A `favorites` table with columns: `id`, `user_id`, `item_id`, `created_at`. RLS: `auth.uid() = user_id`. |
| **API** | `POST /api/favorites` — receives `{ item_id }`, checks auth, inserts row with current user's id. `DELETE /api/favorites/[id]` — removes a row (if it belongs to the user). |
| **UI** | A heart button. When clicked: call POST. Heart turns red. When clicked again: call DELETE. Heart turns gray. Show a "Saving..." spinner during the call. Show an error if it fails. |

Today you do this whole pattern for your **main entity** — the one from your PRD.

---

## Part 2: CRUD — The Four Operations (~5 min read)

Every feature in every app does some combination of four operations:

- **C** reate — insert a new row
- **R** ead — fetch existing rows  
- **U** pdate — change a row
- **D** elete — remove a row

That's it. Every product on earth — Notion, Airbnb, Stripe — at its core, is just CRUD operations on data + some logic on top.

Today you build all four for your main entity. By end of Day 6, your user can:
- **Create** a [whatever your entity is — task, deliverable, habit, etc.]
- **Read** their list of all of them
- **Update** the status or content of one
- **Delete** any of them

This is the foundation. AI features come Days 7-12. Today: the bones.

---

## Part 3: How To Build CRUD With Claude (~10 min read)

There are two approaches:

### Approach A: Big bang
Ask Claude to build the whole CRUD feature at once. Faster, but you don't see how each piece works.

```
Build a complete CRUD feature for [entity] in my Next.js + Supabase app.
Need: API routes (POST, GET, PUT, DELETE), a /[entity] page with form +
list, full RLS-aware Supabase calls. Use my existing auth setup.
```

### Approach B: Piece by piece (RECOMMENDED for EAs)
Walk through Data → API → UI separately. Slower, but you understand each layer.

1. First: "Create the database table with these columns. Show me the SQL."
2. Then: "Now create the API route to create one. Show me the code."
3. Then: "Now create the API route to read all of them. Show me."
4. ... etc

By the end you've understood each piece. Slower today, faster on Day 11+ when you're debugging.

> 🔧 **Engineers:** Big bang is fine for you. You can pattern-match.

---

## Today's Assignment

Pick your main entity (from Section 3 of your PRD — your most important feature).

For example, if your PRD's first user story is "As Sarah, I want to see all deliverables in one dashboard," your entity is `deliverables`. If it's "As David, I want to track my daily habits," it's `habits`.

Then in [build.md](./build.md), wire up CRUD for that entity:
1. Verify the table from Day 5 has the right columns (or add some)
2. Build API routes: POST, GET, PUT, DELETE
3. Build a UI page that uses them
4. Test the full flow live
5. Run Day 6 verification

---

## What Good Looks Like

After Day 6, your live URL should have a page where:

- You sign up / log in
- You see a form to create a new [entity]
- You add a few, they appear in a list
- You can mark one as "done" / change its status (Update)
- You can delete one (it disappears)
- If you sign out and sign back in, your data is still there
- If you open the same site in incognito as a different user, you see NOTHING (RLS is working)

That last one — incognito test — is critical. It proves your auth + RLS + API are all working together.

---

## Common Mistakes (Today)

1. **Skipping the RLS test.** Builders test as themselves, everything works, ship. Then a friend signs up, sees their data. **Always test as a second user.**

2. **API routes returning all data.** A poorly-coded API route can return data from all users, even with RLS on the table. Make sure your API routes use the **server-side Supabase client** with the user's session, not the service_role key.

3. **Not handling loading/empty/error states.** A "list of deliverables" page that shows a blank screen for 2 seconds while loading looks broken. Add a spinner. Add "No deliverables yet — create one!" for empty state. Add "Something went wrong" for errors.

4. **Trying to handle 100 features at once.** Today is ONE entity, ONE CRUD. Tomorrow is more features (or AI). Don't try to build everything today.

5. **Confusing client-side and server-side Supabase clients.** Client-side runs in the user's browser (less trusted). Server-side runs in your API routes (more trusted, has the user's session). Use the right one — Claude knows the difference, ask it to explain if confused.

---

## What Should Be True After Day 6

- [ ] You can create a [main entity] via the UI
- [ ] You can see a list of [main entities] you've created
- [ ] You can update one (e.g., mark done, change status)
- [ ] You can delete one
- [ ] Data persists across page refreshes and re-login
- [ ] A different user (incognito test) doesn't see your data
- [ ] The whole flow works on your **live Vercel URL** (not just localhost)
- [ ] Verification passed ✅

---

## Verify Your Day 6

```bash
claude
```

Ask your harness to run the OneMillion verifier for this day.
- Check API routes exist (POST, GET at minimum)
- Verify the entity page exists and uses the routes
- Test fetching the live URL
- Ask you to verify the incognito test passed
- Report pass / needs revision

---

## Share It

```
✅ Days 1-6 done: A real app at [your URL] with auth + full CRUD
🎯 Days 7-12: Adding AI 🤖
#BuildingWithOneMillion
```

You finished Days 1-6. **That's a massive milestone.** Most courses haven't gotten to a deployed CRUD app by hour 10. You did it in 6 days.

---

## Go Deeper

- **[Next.js Route Handlers](https://nextjs.org/docs/app/building-your-application/routing/route-handlers)** — how the API routes work
- **[Supabase Data API Patterns](https://supabase.com/docs/guides/api)** — different ways to query your DB
- **[React Forms with Server Actions](https://nextjs.org/docs/app/building-your-application/data-fetching/server-actions-and-mutations)** — modern Next.js pattern

---

→ **Next:** [Day 7 — AI Feature Spec](../day-07-ai-spec/learn.md)
