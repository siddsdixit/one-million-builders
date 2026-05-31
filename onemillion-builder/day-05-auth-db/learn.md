# Day 5 — Auth + Database

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Days 1-6 | ~1–2.5 hours | Real auth + secure database**

---

## Learning Frame

- **Mental model:** Auth plus RLS turns a demo into a product with private user data.
- **What can go wrong:** You create data access without proving users are isolated.
- **What to ignore today:** Ignore advanced login options; get email auth and one protected table working.

## What You'll Have After Today

- A **Supabase project** linked to your app
- **Signup, login, logout** working on your live URL
- A **users table** automatically managed by Supabase Auth
- **Row Level Security (RLS)** turned on — the single most important security feature in your app
- An understanding of WHY each piece matters (this is where production hygiene starts)

By tomorrow you build your core feature. Today you build the foundation it sits on.

---

## Video Walkthrough

Video walkthrough: coming soon. The written guide is complete.

---

## Quick Note: Why Supabase + Not Postgres (For Engineers)

> 🔧 **If you've shipped before, you've probably wondered:** "Why are we using Supabase instead of plain Postgres?"
> Three reasons:
> 1. **Built-in auth.** Rolling your own auth (signup/login/sessions/forgot-password/OAuth) is 2-3 days of careful work *if you do it right* — and most people don't. Supabase ships it as a free, battle-tested service.
> 2. **Row Level Security at the DB layer.** RLS in Supabase is a thin wrapper around Postgres RLS. So you ARE using Postgres — just with a great managed layer.
> 3. **Speed.** Setting up auth + DB + API in 2 hours instead of 2 days lets you spend the time savings on AI features in Days 7-12.
>
> If you really want to swap for raw Postgres later (after Day 18), every Supabase concept you learn maps cleanly. Auth flows go to `next-auth` or your own. RLS stays as RLS. Done.

## Part 1: Why Auth Is Always First (~10 min read)

Every product needs to know **who the user is.** Without that, nothing personal can happen. No dashboards, no saved data, no "your" anything.

Auth (short for authentication) does three things:
1. **Signup** — create a new user account
2. **Login** — verify an existing user's identity
3. **Session** — remember they're logged in for the next ~hour

You'd think this is simple. It's not. Auth is famously the place where security breaches happen. Passwords stored wrong. Sessions hijacked. "Forgot password" flows that let attackers in. Whole companies have been ruined by auth gone wrong.

**The good news:** you don't write auth from scratch. Supabase does it for you. We use what they built. It's safer than what you (or even Anthropic's models) could write.

This is the second pillar of agentic engineering: **don't reinvent foundational infrastructure.** Use battle-tested tools for the dangerous parts.

---

## Part 2: What Supabase Is (~10 min read)

Supabase is **the pantry from the restaurant analogy** — your database. But it also includes the maître d' who knows every customer (auth) and the bouncer who keeps people out of areas they shouldn't be in (Row Level Security).

You can think of it as three things in one:

### The Database (PostgreSQL)
A real, full-featured relational database. Tables. Rows. Columns. Same kind of database that runs Instagram, Uber, Slack. Free up to 500 MB on the free tier (your app uses ~1 MB).

### The Auth System
Built-in signup, login, password reset, email confirmation, Google OAuth, magic links. You don't write any of this. You configure it in their dashboard and call their library from your code.

### Row Level Security (RLS)
This is the killer feature. RLS is a rule attached to every database table that says: **"A user can only see rows where THIS condition is true."**

Example: a `tasks` table with RLS rule `(user_id = auth.uid())` means "a user can only see/edit tasks where the task's user_id matches their own ID." Without this rule, anyone with your public API key could read every task in the database. With it, even if your code is wrong, the database itself enforces the rule.

**Enable RLS on every table. One rule per table. Always.**

If you take only one thing from Day 5, take this. RLS is the difference between "I built an app" and "I built an app that's safe to put real users on."

---

## Part 3: The Auth Flow You're Building (~10 min read)

Here's the user journey for what you build today:

1. New user visits your app, sees a "Sign Up" button
2. Clicks it, gets a signup form (email + password)
3. Enters credentials, clicks Submit
4. Supabase creates the account
5. (Optional, off by default for dev) Sends a confirmation email
6. User is logged in, sees the homepage with their email
7. There's a "Sign Out" button
8. Clicks Sign Out — back to logged-out state
9. Closes the browser, comes back later
10. Sees a "Log In" button (because there's no active session anymore)
11. Clicks Log In, enters credentials, signs in

That's the whole loop. Supabase handles steps 4-10 internally. You wire up the UI.

### What Supabase Gives You For Free
- `users` table (auto-managed — you don't create this)
- Email/password validation
- Password hashing (with bcrypt, properly)
- Session tokens (JWT-based, secure)
- "Forgot password" flow
- Email confirmation (optional)
- Google OAuth, GitHub OAuth, etc. (optional)

### What You Build
- `/signup` page — a form
- `/login` page — a form
- `/auth/callback` route — handles the auth redirect
- A protected page (your future dashboard)
- A "Sign Out" button somewhere
- Middleware that checks if a user is logged in

This is ~200 lines of code total. Claude writes most of it. You review what came out.

---

## Today's Assignment

In [build.md](./build.md):
1. Create a Supabase project
2. Install Supabase client libraries
3. Set up environment variables (local + Vercel)
4. Use Claude to scaffold the auth pages
5. Create your first table (for tomorrow's core feature) with RLS enabled
6. Test the full signup → login → logout flow on your live URL

---

## What Good Looks Like

After Day 5, here's what working looks like:

- Visit `https://your-app.vercel.app/signup`
- Enter `test@example.com` / `password123`, click Sign Up
- You're redirected to a page that says "Welcome, test@example.com"
- Click "Sign Out" — redirected to the logged-out homepage
- Click "Log In", enter the same credentials, sign in — works
- In your Supabase dashboard → Authentication → Users, you see your test user

If all of that works, Day 5 is done.

---

## Common Mistakes (Today)

1. **Skipping RLS.** Builders forget or "I'll do it later." Then Day 6 they put real data in their tables, deploy, and any visitor can read all data via the public API key. **Always RLS. From the start.**

2. **Storing secrets in code.** Your Supabase URL and anon key go in `.env.local` (gitignored) AND in Vercel's environment variables UI. Never in your code files. Never committed to git.

3. **Forgetting to add env vars to Vercel.** Local works (`.env.local` is read by `npm run dev`). Production breaks because Vercel doesn't read `.env.local`. You must add the same vars in Vercel's dashboard.

4. **Email confirmation enabled in dev.** Supabase defaults to requiring email confirmation. For development this slows you down. Disable it in Supabase dashboard → Authentication → Providers → Email → "Confirm email" OFF (re-enable for real users later).

5. **Confusing `anon key` and `service_role key`.** Use the **anon key** in your frontend code (it's safe to be public). Never put the **service_role key** in frontend code — that one has full admin access. We don't need service_role today.

---

## What Should Be True After Day 5

- [ ] Supabase project created
- [ ] `@supabase/supabase-js` and `@supabase/ssr` installed in your project
- [ ] `.env.local` has `NEXT_PUBLIC_SUPABASE_URL` and `NEXT_PUBLIC_SUPABASE_ANON_KEY`
- [ ] Same vars added to Vercel project settings
- [ ] `/signup` page works on your Vercel URL
- [ ] `/login` page works on your Vercel URL
- [ ] Sign out works
- [ ] You can see your test user in Supabase dashboard
- [ ] At least one table created with RLS enabled
- [ ] Verification passed ✅

---

## Verify Your Day 5

Ask your harness to run the OneMillion verifier for this day. It will:
- Check Supabase libraries are installed
- Verify env vars are set
- Check auth routes exist
- Confirm RLS is enabled on your first table
- Test the signup/login flow against your live URL
- Report pass / needs revision

---

## Share It

```
✅ Day 5 done: Auth working + RLS enabled. Real users can sign up now.
🎯 Tomorrow: building the core feature
#BuildingWithOneMillion
```

---

## Go Deeper

- **[Supabase Auth Docs](https://supabase.com/docs/guides/auth)** — go deeper on auth patterns
- **[Supabase + Next.js Quickstart](https://supabase.com/docs/guides/getting-started/quickstarts/nextjs)** — official guide
- **[RLS Deep Dive](https://supabase.com/docs/guides/database/postgres/row-level-security)** — when you want to write more complex policies
- **[Auth security 101](https://owasp.org/www-project-top-ten/)** — what NOT to do with auth (OWASP)

---

→ **Next:** [Day 6 — Core Feature](../day-06-core-feature/learn.md)
