# Day 8 - Core Build

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="./README.md">Day Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

Day 8 is where the app becomes useful. You are building one real product workflow end to end, not the whole roadmap.

## Outcome

By the end of today, your app should have one completed vertical slice:

- one selected sprint brief
- one core entity or workflow
- create/read/update/delete or archive behavior
- data persisted in Supabase
- loading, empty, error, and success states
- protected route behavior still intact
- second-user isolation still passing when private data exists
- deployed workflow working live

## Watch / Read / Build

- [Watch](./loom.md) the worked example when the recording is available.
- [Learn](./learn.md) the vertical slice mindset.
- [Build](./build.md) one useful sprint, not every feature.
- [Recover](./stuck.md) if CRUD, persistence, UI state, permissions, or live deploy breaks.
- [Resources](./resources.md) are optional after the day is complete.

## What Good Looks Like

The finished Day 8 workflow should pass this human test:

```text
A logged-in target user can complete one meaningful job in the product without you explaining the UI.
```

For many products, that means:

1. Open protected product page.
2. See a helpful empty state.
3. Create the core record.
4. See it appear immediately.
5. Update or archive it.
6. Refresh the page and confirm the data persisted.
7. Sign in as another user and confirm private data does not leak.
8. Push, deploy, and repeat the same workflow on the live URL.

## Tutor Prompt

Paste this into your harness from the repo root:

```text
I am on OneMillion Day 8: Core Build.

Act as the `build` agent for this day.
First teach me vertical slice thinking in plain language: one useful workflow from UI to server/data and back.
Then guide me one step at a time using course/days/day-08-core-build/learn.md, course/days/day-08-core-build/build.md, course/days/single.md, and course/course-manifest.json.

Before changing code, ask me for:
- which sprint brief is today's target
- core entity fields
- the minimum usable workflow
- whether today's action is CRUD, archive, or another workflow
- visible states that must exist today
- what we will defer

Use my Day 5 architecture, Day 7 auth/database setup, and the selected sprint brief as the build contract.
Build exactly one useful sprint.
Do not add AI today.
Do not expand scope beyond the selected sprint without asking me.
Show what changed and ask me to inspect it.
Verify data persistence, protected routes, second-user isolation when private data exists, and live deployed behavior.
When I say `day done`, verify the completion gate and update .onemillion/state.json.
```

## Decisions The Learner Must Own

- Which sprint brief is the Day 8 target.
- Core entity fields.
- Minimum usable workflow.
- CRUD or archive actions in scope.
- Required states: empty, loading, error, success, permission.
- What to defer.

## External Tools

- Supabase
- Vercel

Use `course/docs/account-setup.md` for exact links, permissions, and QA checks.

## Common Checks

Ask the harness to verify:

- The workflow uses the authenticated user or tenant from the server/session, not a client-supplied owner.
- Data persists after page refresh.
- The UI has a real empty state before records exist.
- Mutations show success or recoverable error feedback.
- Logged-out users cannot reach protected data.
- A second user cannot see private records from the first user.
- The live deployed workflow matches local behavior.

## Done Checklist

- [ ] exactly one useful sprint is selected and completed
- [ ] core create/read/update/delete or archive works locally
- [ ] data persists in Supabase
- [ ] loading, empty, error, and success states are handled
- [ ] protected routes still reject unauthenticated users
- [ ] second user cannot see first user data when private data exists
- [ ] deployed app works after the feature is pushed
- [ ] live deployed workflow matches the local source/build
- [ ] one meaningful sprint commit exists

## Commit

After the verifier passes, commit meaningful work:

```bash
git add .
git commit -m "Day 8: core workflow"
```

## Next

After Day 8 is verified, continue to Day 9: Implementation Review.
