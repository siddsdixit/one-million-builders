# Day 5 — Build Guide

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="../README.md">Week Overview</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Time: 1–2.5 hours.** You wire up Supabase, scaffold auth, and create your first table with RLS.

---

## Before You Start

- [ ] Day 4 verified (live URL working)
- [ ] You skimmed [learn.md](./learn.md) (especially Part 3 — the auth flow)
- [ ] Terminal in your project folder
- [ ] Both terminal windows open (one for `npm run dev`, one for git/claude)

---

## Step 1: Create Supabase Project (10 min)

1. Go to [supabase.com](https://supabase.com)
2. Click **Start your project** → Continue with GitHub
3. Click **New Project**
4. Fill in:
   - **Name:** `my-onemillion-app` (or your app name)
   - **Database Password:** generate a strong one, write it down somewhere safe
   - **Region:** pick closest to you
5. Click **Create project**. Wait 2 minutes.

Once it's ready, go to **Settings** (gear icon, left sidebar) → **API**.

You need TWO things from this page:
- **Project URL** — looks like `https://abcdefgh.supabase.co`
- **anon public** key — long string starting with `eyJ...`

Keep this tab open.

---

## Step 2: Configure Environment Variables (5 min)

In your project folder, create a file called `.env.local`:

```bash
touch .env.local
```

Open `.env.local` in your editor and add:

```
NEXT_PUBLIC_SUPABASE_URL=https://your-project-id.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJ_your_anon_key_here
```

Replace with YOUR values from Supabase.

**Verify it's gitignored.** Run:

```bash
cat .gitignore | grep .env.local
```

**You should see:** `.env.local` listed. If not, add it:

```bash
echo ".env.local" >> .gitignore
```

---

## Step 3: Add Same Vars To Vercel (5 min)

1. Go to [vercel.com/dashboard](https://vercel.com/dashboard) → your project
2. **Settings** → **Environment Variables**
3. Add both:
   - Name: `NEXT_PUBLIC_SUPABASE_URL` | Value: your URL
   - Name: `NEXT_PUBLIC_SUPABASE_ANON_KEY` | Value: your key
4. Click **Save**

> ⚠️ **Critical step.** If you skip this, your deployed app won't connect to Supabase. Local works, production breaks. This is the #1 Day 5 mistake.

---

## Step 4: Install Supabase Client Libraries (3 min)

In your second terminal:

```bash
npm install @supabase/supabase-js @supabase/ssr
```

**You should see:** `added 24 packages` or similar.

---

## Step 5: Let Claude Scaffold The Auth (30-45 min)

In your terminal:

```bash
claude
```

Paste this prompt:

```
I'm on Day 5 of OneMillion. I need to add Supabase Auth to my Next.js App
Router project. Set up:

1. A Supabase client utility (lib/supabase/client.ts for client components,
   lib/supabase/server.ts for server components)
2. A /signup page with email+password form
3. A /login page with email+password form
4. An /auth/callback route handler for Supabase email confirmation links
5. Middleware (middleware.ts) that refreshes the session on every request
6. A protected /dashboard page that shows the logged-in user's email
7. A Sign Out button on the dashboard

Use the @supabase/ssr package (not the deprecated @supabase/auth-helpers).
Use Tailwind for basic styling. Use the env vars
NEXT_PUBLIC_SUPABASE_URL and NEXT_PUBLIC_SUPABASE_ANON_KEY.

Don't overcomplicate. Aim for ~150-200 lines total. Show me what you'd
create before generating files.
```

Claude will outline the files. Review the plan. If it looks reasonable, say "Yes, generate."

Claude generates files. Review each one. Don't blindly accept — read what you're shipping.

---

## Step 6: Disable Email Confirmation For Dev (3 min)

In Supabase dashboard:

1. **Authentication** (left sidebar) → **Providers** → **Email**
2. Toggle **"Confirm email"** to **OFF**
3. Click **Save**

This lets you sign up without verifying email — much faster for testing.

(For production, you'll re-enable this on Day 13 — Production Hygiene.)

---

## Step 7: Test Locally (10 min)

In your first terminal:

```bash
npm run dev
```

In your browser:
1. Go to `http://localhost:3000/signup`
2. Enter `test@example.com` and any password
3. Click Sign Up
4. **You should:** be redirected to `/dashboard` showing your email

Test sign out:
5. Click "Sign Out" on dashboard
6. Try `http://localhost:3000/dashboard` directly
7. **You should:** be redirected to `/login`

Test login:
8. Go to `http://localhost:3000/login`
9. Enter the same credentials
10. **You should:** be back on `/dashboard`

If all this works locally, you're 80% done.

---

## Step 8: Create Your First Table With RLS (15 min)

You won't use this table until Day 6, but creating it now (with RLS) sets the production-hygiene baseline.

Look at your PRD's "Core Features" — pick the main entity. (For example: if you're building a freelance dashboard, it's `deliverables`. If it's a habit tracker, it's `habits`.)

In Supabase dashboard:
1. **Table Editor** (left sidebar) → **+ New table**
2. **Name:** your main entity (e.g., `deliverables`)
3. **Enable Row Level Security (RLS)** — ✅ keep this checked
4. Click **Save**

Now add a few columns. Click your new table → **+ Insert column**:

| Column name | Type | Default | Settings |
|-------------|------|---------|----------|
| `id` | uuid | auto-generated | already exists |
| `created_at` | timestamptz | `now()` | already exists |
| `user_id` | uuid | (none) | check: **Is foreign key** → table: `auth.users` → column: `id` |
| `name` | text | (none) | required |
| `status` | text | `'todo'` | (or any default that fits) |

Save.

Now add an RLS policy. Click your table → **Policies** (under the table name) → **New Policy** → **For full customization**:

- **Policy name:** `Users see only their own [entity]`
- **Allowed operation:** `ALL`
- **Target roles:** `authenticated`
- **USING expression:** `auth.uid() = user_id`
- **WITH CHECK expression:** `auth.uid() = user_id`

Click **Review** → **Save**.

> 💡 What this policy does: a logged-in user can only SELECT, INSERT, UPDATE, DELETE rows where the row's `user_id` matches their own auth ID. Without this, anyone could read any row.

---

## Step 8b: Pre-Deploy Checklist (MANDATORY)

**STOP. Before you push to git, complete this checklist.**

The most common Day 5 failure mode: works locally, breaks in production silently. This checklist catches it before you push.

- [ ] **`.env.local` exists locally** with both:
  - `NEXT_PUBLIC_SUPABASE_URL=https://...`
  - `NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJ...`

- [ ] **Vercel has the SAME env vars** (Settings → Environment Variables in your Vercel project dashboard). Take a screenshot or screenshot-equivalent visual scan: BOTH names visible.

- [ ] **`.env.local` is gitignored.** Run `git status` — you should NOT see `.env.local` in the list of files to be committed. If you do: `echo ".env.local" >> .gitignore`.

- [ ] **Supabase email confirmation is OFF** (for dev only). Supabase dashboard → Authentication → Providers → Email → "Confirm email" toggle: OFF.

- [ ] **RLS is enabled on your first table.** Supabase dashboard → Table Editor → click your table → green "RLS enabled" indicator.

- [ ] **RLS policy exists.** Same screen → Policies → at least one policy referencing `auth.uid()`.

If any box is unchecked: fix it before continuing. Don't skip.

## Step 9: Deploy + Verify Live (5 min)

Push everything to git:

```bash
git add .
git commit -m "Day 5: Supabase auth + first table with RLS"
git push
```

Wait ~60 seconds for Vercel to redeploy.

Visit `https://your-app.vercel.app/signup` and test the full flow LIVE (not localhost).

If it works in production: you're done.

If signup hangs or auth errors:
- Check Vercel logs (dashboard → your project → Deployments → click latest → View Function Logs)
- Most common issue: env vars not set in Vercel (re-do Step 3)

---

## Step 10: Run Day 5 Verification

```bash
claude
```

Paste contents of [`ai-instructions-day-05.md`](./ai-instructions-day-05.md).

---

## What Should Be True After Day 5

- [ ] Supabase project exists
- [ ] `.env.local` has the two NEXT_PUBLIC_ vars
- [ ] Vercel has the two NEXT_PUBLIC_ vars
- [ ] `@supabase/supabase-js` and `@supabase/ssr` installed
- [ ] `/signup`, `/login`, `/dashboard`, `/auth/callback` routes exist
- [ ] Test signup → login → logout works on your Vercel URL
- [ ] First table created with RLS enabled and a policy
- [ ] Verification passed ✅

---

## Update Your Progress Tracker

Before you close today, open `.onemillion/progress.md` and update:

- **Current day:** Day 5 complete
- **Last verified day:** Day 5
- **Current blocker:** None, or the exact blocker to resume from
- **Next smallest action:** Open Day 6.

If verification did not pass yet, keep **Last verified day** at the previous passed day and write the blocker clearly.

## If You Are Stuck

Open your coding harness from your project folder:

```bash
claude
```

Paste this:

```text
I am on OneMillion Day 05.

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
| Signup says "Email rate limit exceeded" | Supabase free tier limits emails. Use a different test email or disable email confirmation. |
| `Invalid API key` error | You pasted the wrong key. Use the `anon public` key (under Project Settings → API). Not the service_role one. |
| Auth works locally but not on Vercel | Env vars aren't on Vercel. Settings → Environment Variables → add both vars → redeploy. |
| RLS blocking my own inserts | Your policy is wrong. Should be `auth.uid() = user_id`. Make sure you're inserting with `user_id = the current user's id`. |
| Can't see test users in Supabase | Authentication → Users (left sidebar). They're there. |
| Stuck on "session not refreshing" | Make sure middleware.ts is at the project root (not inside `app/`). Restart `npm run dev`. |
| Got logged out unexpectedly | Sessions expire after ~1 hour by default. Log in again. |
| Vercel build fails after auth changes | Check the build log. Usually a TypeScript error — paste it into Claude for the fix. |

---

→ **Done with Day 5?** Move to [Day 6 — Core Feature](../day-06-core-feature/learn.md). Tomorrow you build your main feature.
