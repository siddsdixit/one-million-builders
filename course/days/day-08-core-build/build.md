# Day 8 — Build Guide

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
I am on OneMillion Day 8: Core Build.

Act as the `build` agent for this day.
First teach me the concept in plain language:
- what "one useful sprint" means
- what a vertical slice is
- why the core non-AI workflow comes before AI
- how CRUD becomes forms, lists, detail pages, status changes, and archive/delete actions
- how the sprint brief acts as the build contract
- how to preserve auth, RLS, tenancy, and RBAC decisions from Day 7
- what local verification and live deployment verification mean

Then guide me one step at a time.
Use the course manifest, single.md, and the current pipeline artifacts.
Read .onemillion/architecture.md and the next incomplete sprint brief in .onemillion/sprints/.
Build exactly one useful sprint today unless the sprint brief itself is too small to prove a useful workflow.
Do not skip my human decisions.
Do not create paperwork-only files.
When an external provider is needed, give the exact full URL and QA check.
```

## Step 2: Make The Human Decisions

Before the harness writes or changes anything, answer these decisions:

- core entity fields
- minimum usable workflow
- which sprint brief is the Day 8 target
- which route/screen proves the workflow is useful
- what create/read/update/delete or archive actions are in scope
- which states must be visible today: loading, empty, error, success, permission denied
- what to defer

## Step 3: Produce The Day Output

Expected output today:

- one completed useful sprint from `.onemillion/sprints/`
- one core workflow working end to end
- real data saved and read from Supabase
- auth/RLS/tenancy/RBAC boundaries preserved
- loading, empty, error, and success states for the workflow
- local verification
- deployed verification on the live URL
- one meaningful git commit for the sprint

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
Run the OneMillion verifier for Day 8.
Inspect the selected sprint brief, app code, Supabase persistence, auth/RLS boundaries, deployment link, and manual confirmations.
Confirm one useful vertical sprint works locally and live.
Record the result in .onemillion/state.json.
Do not create separate verifier markdown files.
```

## Update Orchestrator State

Before you close today, ask the orchestrator to update `.onemillion/state.json`:

- **Current day:** Day 8 complete
- **Last verified day:** Day 8
- **Current blocker:** None, or the exact blocker to resume from
- **Next smallest action:** Open Day 9.

## What Should Be True After Day 8

- [ ] exactly one useful sprint is selected and completed
- [ ] core create/read/update/delete or archive workflow works locally
- [ ] data persists in Supabase
- [ ] loading, empty, error, and success states are handled
- [ ] protected routes still reject unauthenticated users
- [ ] second user cannot see first user data when private data exists
- [ ] deployed app works after the feature is pushed
- [ ] live deployed workflow matches the local source/build
- [ ] one meaningful sprint commit exists

## If You Are Stuck

Paste this into your harness:

```text
I am on OneMillion Day 8: Core Build.
I am stuck on this part:
[paste the step or artifact]

Here is what I expected:
[describe]

Here is what happened:
[describe]

Help me find the smallest next action. Teach the concept if I am missing it. Do not skip the learning moment.
```


---

-> **Next:** [Day 9 — Implementation Review](../day-09-review/learn.md)
