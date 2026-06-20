# Day 7 - Auth + Database

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="./README.md">Day Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

Day 7 adds identity and private data. This is the day where the app stops being only a public shell and starts becoming a real product with users.

## Outcome

By the end of today, your app should have:

- Supabase project
- local and Vercel environment variables
- chosen auth method
- signup/login/logout or the equivalent auth flow
- protected route behavior
- first private product tables
- RLS enabled on private tables
- second-user isolation test passed

## Watch / Read / Build

- [Watch](./loom.md) the worked example when the recording is available.
- [Learn](./learn.md) the difference between identity, session, authorization, RBAC, tenancy, and RLS.
- [Build](./build.md) one step at a time.
- [Recover](./stuck.md) if auth, env vars, redirects, or RLS break.
- [Resources](./resources.md) are optional after the day is complete.

## What Good Looks Like

Before saying `day done`, you should be able to demonstrate:

1. Logged-out users cannot access protected product pages.
2. User 1 can sign up or sign in.
3. User 1 can create or view private data.
4. User 2, tested in incognito or a separate browser profile, cannot see User 1's private data.
5. The same auth flow works on the live Vercel URL when signup is part of the product.

The second-user isolation test is the most important check of the day. If it fails, stop and fix RLS before continuing.

## Tutor Prompt

Paste this into your harness from the repo root:

```text
I am on OneMillion Day 7: Auth + Database.

Act as the `build` agent for this day.
First teach me auth and data privacy in plain language:
- identity: how the product knows who I am
- session: how the app remembers I am logged in
- authorization: what I am allowed to access
- tenancy: whether data belongs to a user, organization, or public space
- RBAC: whether roles like owner/admin/member/viewer matter
- RLS: how Supabase prevents cross-user or cross-tenant data leaks

Then guide me one step at a time using course/days/day-07-auth-db/learn.md, course/days/day-07-auth-db/build.md, course/days/single.md, and course/course-manifest.json.

Before changing code or database schema, ask me for:
- auth method
- public and protected routes
- single-user vs team/multi-tenant model
- profile, organization, membership, and role hierarchy if needed
- RLS policy intent for each private table
- local and deployed redirect URLs

Use the existing Day 5 architecture and sprint brief.
Keep service-role keys out of client code.
Add placeholders only to .env.example.
Show what changed and ask me to inspect it.
Do not let me advance until second-user isolation passes when private data exists.
When I say `day done`, verify the completion gate and update .onemillion/state.json.
```

## Decisions The Learner Must Own

- Auth method: email/password, magic link, OAuth, invite-only, or admin-created users.
- Which routes are public.
- Which routes are protected.
- Whether data is user-owned, organization-owned, or public/community data.
- Whether RBAC roles are needed.
- First product table shape.
- RLS policy intent.
- Local and deployed redirect URLs.

## External Tools

- Supabase
- Vercel

Use `course/docs/account-setup.md` for exact links, permissions, and QA checks.

## Common Checks

Ask the harness to inspect:

- `.env.example` has placeholders only.
- `.env.local` is not committed.
- No `SUPABASE_SERVICE_ROLE` or server-only secret appears in client code.
- Supabase Auth redirect URLs include local and live URLs.
- Private tables have RLS enabled.
- RLS policies match the chosen ownership model.

## Done Checklist

- [ ] Supabase project exists
- [ ] auth method is chosen and implemented
- [ ] single-tenant or multi-tenant model is chosen intentionally
- [ ] RBAC roles are defined when teams, organizations, or admin/member differences exist
- [ ] signup works locally and live when signup is part of the product
- [ ] login/logout works
- [ ] protected routes reject unauthenticated users
- [ ] RLS enabled on private tables
- [ ] second-user isolation passes when private data exists
- [ ] env vars are not leaked

## Commit

After the verifier passes, commit meaningful work:

```bash
git add .
git commit -m "Day 7: auth database and RLS"
```

## Next

After Day 7 is verified, continue to Day 8: Core Build.
