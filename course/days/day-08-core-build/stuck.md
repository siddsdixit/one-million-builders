# Day 8 - If You Are Stuck

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="./README.md">Day Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

Day 8 problems usually come from scope, persistence, state updates, permissions, or deployment drift. Fix the smallest layer first.

## Recovery Prompt

Paste this into your harness:

```text
I am on OneMillion Day 8: Core Build.
I am stuck.

Layer that seems broken:
[scope / form / API or server action / Supabase query / UI state / auth permission / RLS / live deploy / not sure]

What I tried:
[paste step, command, or user action]

What I expected:
[describe]

What happened:
[paste error, browser behavior, database state, or screenshot text]

Please diagnose the smallest next action.
Teach the missing concept briefly.
Do not add unrelated features.
Do not add AI today.
Do not advance Day 8 until one useful sprint works locally and live.
```

## First Checks

- Confirm Day 7 auth still works.
- Confirm you selected exactly one sprint brief.
- Confirm the target entity/table exists.
- Confirm create/read/update/delete or archive scope is clear.
- Confirm data persists after refresh.
- Confirm the live deployment is the latest commit.

## Common Day 8 Issues

| Problem | Likely Cause | Smallest Fix |
|---|---|---|
| The agent starts building too much | sprint target is vague | restate exactly one workflow and defer the rest |
| Form submits but nothing appears | mutation succeeds but UI does not refetch/update | inspect network/server response and refresh state |
| Item appears then disappears | insert failed or data not persisted | inspect Supabase table and server error |
| Update/delete affects wrong row | missing owner/tenant filter | add auth-aware query and rely on RLS |
| Logged-out user can see data | route protection missing | enforce auth before rendering private data |
| User 2 sees User 1 data | RLS or query filter is wrong | stop and fix isolation before continuing |
| Empty state never appears | UI only designed for happy path | add empty state before records exist |
| Error is invisible | errors swallowed in client/server code | show recoverable error copy |
| Works locally but not live | deployment/env drift | push latest commit, verify Vercel deploy, retest live URL |

## Scope Guard

Today is not complete because the app has many partial features. It is complete when one core workflow works end to end.

Use this sentence to reset scope:

```text
For Day 8, we are building only [workflow] for [target user]. Everything else is deferred.
```

## Permission Debug Questions

- Does the server know who the current user is?
- Is the owner or tenant field set from the authenticated session?
- Does the query filter by the right owner/tenant?
- Does RLS enforce the same rule at the database layer?
- Did you test logged-out and second-user behavior?

## Recovery Order

1. Re-read [learn.md](./learn.md) for vertical slice thinking.
2. Re-open [build.md](./build.md) and identify the selected sprint.
3. Reproduce the failure locally.
4. Inspect the data layer before changing UI.
5. Fix one layer.
6. Retest local, permissions, and live deploy.
7. Run the verifier only after the done checklist is true.
