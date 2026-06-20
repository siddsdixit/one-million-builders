# Day 7 - If You Are Stuck

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="./README.md">Day Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

Day 7 failures usually come from one of four places: env vars, redirects, session handling, or RLS. Diagnose the layer before asking the harness to rewrite auth.

## Recovery Prompt

Paste this into your harness:

```text
I am on OneMillion Day 7: Auth + Database.
I am stuck.

Layer that seems broken:
[Supabase project / env vars / auth UI / callback redirect / protected route / RLS / live deploy / not sure]

What I tried:
[paste step or command]

What I expected:
[describe]

What happened:
[paste error, URL, dashboard setting, or browser behavior]

Please diagnose the smallest next action.
Teach the missing concept briefly.
Do not expose secrets.
Do not rewrite unrelated app code.
Do not advance Day 7 until auth works and second-user isolation passes when private data exists.
```

## First Checks

- Confirm Day 6 live deployment still works.
- Confirm Supabase URL and anon key exist locally and in Vercel.
- Confirm `.env.local` is not committed.
- Confirm `.env.example` contains placeholders only.
- Confirm Supabase redirect URLs include local and live URLs.
- Confirm private tables have RLS enabled.
- Confirm policies match user-owned or organization-owned data.

## Common Day 7 Issues

| Problem | Likely Cause | Smallest Fix |
|---|---|---|
| Works locally but not live | missing Vercel env vars | add env vars in Vercel and redeploy |
| Login redirects to localhost from production | Supabase redirect URLs incomplete | add live callback URL in Supabase Auth settings |
| User is logged out after refresh | middleware/session refresh missing or wrong | inspect server/client Supabase setup |
| Protected page flashes private data | auth check only happens client-side | enforce auth server-side or before rendering private data |
| RLS blocks all rows | policy does not match inserted owner field | inspect row owner column and policy condition |
| User 2 sees User 1 data | RLS missing or too broad | stop, enable RLS, tighten policies, retest |
| Build fails after adding Supabase | env vars assumed at build time | handle missing envs clearly and set Vercel vars |
| Service role key appears in app | wrong key copied | remove it, rotate it if exposed, use anon key/client-safe setup only |

## RLS Debug Questions

Ask these before changing policies:

- Is the private row owned by `user_id`, `organization_id`, or another tenant key?
- Is the owner field set by the server from the authenticated session?
- Does the policy check the same field that the row actually stores?
- Are `USING` and `WITH CHECK` both needed for this operation?
- Did you test in incognito with a real second user?

## What Not To Do

- Do not disable RLS to make the app work.
- Do not use service-role keys in browser code.
- Do not trust `user_id` sent from the client.
- Do not continue to Day 8 if User 2 can see User 1's data.

## Recovery Order

1. Re-read [learn.md](./learn.md) for the auth/RLS mental model.
2. Re-open [build.md](./build.md) and find the first unchecked requirement.
3. Identify the failing layer: env vars, redirect, session, route protection, or RLS.
4. Fix only that layer.
5. Retest locally and live when relevant.
6. Run the verifier only after auth and isolation checks pass.
