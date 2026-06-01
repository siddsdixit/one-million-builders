# Day 7 — Build Guide

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

## Before You Start

- [ ] Previous day is verified in `.onemillion/state.json`.
- [ ] You are in the correct product/course workspace.
- [ ] You have read [learn.md](./learn.md).

## Step 1: Ask The Harness To Teach The Day

Paste this:

```text
I am on OneMillion Day 7: Auth + Database.

Act as the `build` agent for this day.
First teach me auth as a product module in plain language:
- why authentication matters for trust, privacy, personalization, billing, audit trails, and safe AI actions
- identity: how the product knows who I am
- session: how the app remembers I am logged in
- authorization: what a logged-in user can do
- RBAC: what Role-Based Access Control means, and how owner/admin/member/viewer roles work
- single-tenant vs multi-tenant: when to use owner_id, organization_id, tenant_id, and membership tables
- secure user information: how to avoid leaking private data, service-role keys, tenant records, or user profile data
- RLS: how Supabase prevents one user or tenant from reading another user's rows
- redirect URLs: why local and deployed auth callbacks must be configured
- env vars: what can be public and what must stay server-only

Then guide me one step at a time.
Use the course manifest, single.md, and the current pipeline artifacts.
Read .onemillion/architecture.md and .onemillion/sprints/S1-auth-db.md before changing code.
Do not skip my human decisions.
Do not create paperwork-only files.
When an external provider is needed, give the exact full URL and QA check.
```

## Step 2: Make The Human Decisions

Before the harness writes or changes anything, answer these decisions:

- auth method: email/password, magic link, OAuth, invite-only, or admin-created users
- which routes are public and which routes are protected
- single-user, team/multi-tenant, or public/community data model
- profile, organization, membership, and role hierarchy if the product may become multi-user
- RBAC roles: owner, admin, member, viewer, or simpler product-specific roles
- first product table shape from the sprint brief
- RLS policy intent for each private table
- local and deployed redirect URLs

## Step 3: Produce The Day Output

Expected output today:

- Supabase project connected to the app
- Supabase Auth wired into Next.js
- signup/login/logout/callback/session behavior
- protected route wrapper or middleware
- first product tables from the architecture/sprint brief
- profile, organization, or membership tables when the product needs multi-user hierarchy
- RLS policies for private user-owned or tenant-owned data
- `.env.example` with placeholders only
- local env values configured outside git

Work with the harness until the output matches the day's purpose. Review generated artifacts before accepting them.

## Step 4: External Tools

- Supabase dashboard: https://supabase.com/dashboard
- Supabase project shortcut: https://database.new
- Supabase Next.js Auth: https://supabase.com/docs/guides/auth/quickstarts/nextjs
- Supabase API keys: https://supabase.com/docs/guides/getting-started/api-keys
- Supabase redirect URLs: https://supabase.com/docs/guides/auth/redirect-urls
- Supabase RLS: https://supabase.com/docs/guides/database/postgres/row-level-security
- Vercel signup: https://vercel.com/signup
- Vercel import: https://vercel.com/new
- Vercel dashboard: https://vercel.com/dashboard
- Vercel Git docs: https://vercel.com/docs/deployments/git
- Vercel env vars: https://vercel.com/docs/projects/environment-variables
- Vercel domains docs: https://vercel.com/docs/domains
- Vercel Analytics: https://vercel.com/docs/analytics

If the harness mentions an external provider, it must also give the exact link, permission/settings, and QA check from `course/docs/account-setup.md`.

## Step 5: Verify

Ask your harness:

```text
Run the OneMillion verifier for Day 7.
Inspect the relevant artifacts, app code, deployment links, and manual confirmations.
Record the result in .onemillion/state.json.
Do not create separate verifier markdown files.
```

## Update Orchestrator State

Before you close today, ask the orchestrator to update `.onemillion/state.json`:

- **Current day:** Day 7 complete
- **Last verified day:** Day 7
- **Current blocker:** None, or the exact blocker to resume from
- **Next smallest action:** Open Day 8.

## What Should Be True After Day 7

- [ ] Supabase project exists
- [ ] auth method is chosen and implemented
- [ ] signup works locally and live when signup is part of the product
- [ ] login/logout works
- [ ] protected routes reject unauthenticated users
- [ ] first product tables exist
- [ ] single-tenant or multi-tenant model is chosen intentionally
- [ ] RBAC roles are defined when the product has teams, organizations, or admin/member differences
- [ ] RLS enabled on private tables
- [ ] second-user isolation passes when private data exists
- [ ] env vars are not leaked

## If You Are Stuck

Paste this into your harness:

```text
I am on OneMillion Day 7: Auth + Database.
I am stuck on this part:
[paste the step or artifact]

Here is what I expected:
[describe]

Here is what happened:
[describe]

Help me find the smallest next action. Teach the concept if I am missing it. Do not skip the learning moment.
```


---

-> **Next:** [Day 8 — Core Build](../day-08-core-build/learn.md)
