# Day 5 - Plan Architecture

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="./README.md">Day Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>


This is the learner cockpit for Day 5. Start here, then use the linked files for depth.

## Outcome

By the end of today, you will complete the Day 5 completion gate from `course/course-manifest.json` and update `.onemillion/state.json` through your harness.

## Watch / Read / Build

- [Watch](./loom.md) the worked example when the recording is available.
- [Learn](./learn.md) the concept before asking the harness to work.
- [Build](./build.md) using the step-by-step guide.
- [Recover](./stuck.md) if something breaks or feels unclear.
- [Resources](./resources.md) are optional after the day is complete.

## Tutor Prompt

Paste this into your harness from the repo root:

```text
I am on OneMillion Day 5: Plan Architecture.

Act as the `plan` agent for this day.
First teach me the day in plain language.
Then guide me one step at a time using course/days/day-05-plan-architecture/learn.md, course/days/day-05-plan-architecture/build.md, course/days/single.md, and course/course-manifest.json.
Ask for my human decisions before changing product-defining artifacts or code.
Show what you changed and ask me to inspect it.
When I say `day done`, verify the completion gate and update .onemillion/state.json.
Do not advance me if the gate is incomplete.
```

## Decisions The Learner Must Own

- product type
- backend path: Supabase-only or FastAPI with selected backend host
- auth model
- frontend/backend/database/AI boundaries
- tenancy model
- RBAC model

## External Tools

- None required by the manifest for this day.

## Done Checklist

- [ ] .onemillion/architecture.md exists
- [ ] .onemillion/sprints/ exists
- [ ] product type decision is recorded
- [ ] backend path decision is recorded
- [ ] tenancy model is recorded
- [ ] RBAC decision is recorded
- [ ] security model is recorded
- [ ] data ownership boundaries are recorded
- [ ] sprint briefs are small self-contained build contracts
- [ ] validate-plan passes or findings are resolved

## Commit

After the verifier passes, commit meaningful work. Example:

```bash
git add .
git commit -m "Day 5: Plan Architecture"
```

## Next

After this day is verified, continue to Day 6.
