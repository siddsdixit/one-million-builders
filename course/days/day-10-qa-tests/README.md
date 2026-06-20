# Day 10 - QA + Tests

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="./README.md">Day Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>


This is the learner cockpit for Day 10. Start here, then use the linked files for depth.

## Outcome

By the end of today, you will complete the Day 10 completion gate from `course/course-manifest.json` and update `.onemillion/state.json` through your harness.

## Watch / Read / Build

- [Watch](./loom.md) the worked example when the recording is available.
- [Learn](./learn.md) the concept before asking the harness to work.
- [Build](./build.md) using the step-by-step guide.
- [Recover](./stuck.md) if something breaks or feels unclear.
- [Resources](./resources.md) are optional after the day is complete.

## Tutor Prompt

Paste this into your harness from the repo root:

```text
I am on OneMillion Day 10: QA + Tests.

Act as the `test` agent for this day.
First teach me the day in plain language.
Then guide me one step at a time using course/days/day-10-qa-tests/learn.md, course/days/day-10-qa-tests/build.md, course/days/single.md, and course/course-manifest.json.
Ask for my human decisions before changing product-defining artifacts or code.
Show what you changed and ask me to inspect it.
When I say `day done`, verify the completion gate and update .onemillion/state.json.
Do not advance me if the gate is incomplete.
```

## Decisions The Learner Must Own

- critical paths to test manually
- which tests should be automated now
- which checks can remain manual for MVP
- acceptable risk
- QA evidence

## External Tools

- Vercel
- Supabase

Use `course/docs/account-setup.md` for exact links, permissions, and QA checks.

## Done Checklist

- [ ] .onemillion/test-plan.md exists
- [ ] acceptance criteria are mapped to manual or automated test cases
- [ ] .onemillion/test-results.md exists
- [ ] manual QA checklist is completed
- [ ] automated tests run where the repo supports them
- [ ] auth/RLS/tenant/RBAC permission checks are covered
- [ ] live app passes critical path QA
- [ ] failures are fixed or explicitly deferred with reason

## Commit

After the verifier passes, commit meaningful work. Example:

```bash
git add .
git commit -m "Day 10: QA + Tests"
```

## Next

After this day is verified, continue to Day 11.
