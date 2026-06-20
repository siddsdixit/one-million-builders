# Day 3 - Lock The Spec

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="./README.md">Day Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>


This is the learner cockpit for Day 3. Start here, then use the linked files for depth.

## Outcome

By the end of today, you will complete the Day 3 completion gate from `course/course-manifest.json` and update `.onemillion/state.json` through your harness.

## Watch / Read / Build

- [Watch](./loom.md) the worked example when the recording is available.
- [Learn](./learn.md) the concept before asking the harness to work.
- [Build](./build.md) using the step-by-step guide.
- [Recover](./stuck.md) if something breaks or feels unclear.
- [Resources](./resources.md) are optional after the day is complete.

## Tutor Prompt

Paste this into your harness from the repo root:

```text
I am on OneMillion Day 3: Lock The Spec.

Act as the `spec` agent for this day.
First teach me the day in plain language.
Then guide me one step at a time using course/days/day-03-spec/learn.md, course/days/day-03-spec/build.md, course/days/single.md, and course/course-manifest.json.
Ask for my human decisions before changing product-defining artifacts or code.
Show what you changed and ask me to inspect it.
When I say `day done`, verify the completion gate and update .onemillion/state.json.
Do not advance me if the gate is incomplete.
```

## Decisions The Learner Must Own

- MVP functional requirements
- core entities and CRUD actions
- MVP stories
- acceptance criteria
- out-of-scope items
- definition of done

## External Tools

- None required by the manifest for this day.

## Done Checklist

- [ ] .onemillion/refined-prd.md exists
- [ ] .onemillion/refined-prd.md includes Day 3 Locked Spec
- [ ] functional requirements listed
- [ ] core MVP entities and CRUD actions listed
- [ ] features tagged MVP or POST-MVP
- [ ] complete core flow listed
- [ ] data schema and business rules listed
- [ ] exactly 3 core user stories
- [ ] 2+ use cases
- [ ] testable acceptance criteria
- [ ] 2+ KPIs/success signals
- [ ] locked out-of-scope list
- [ ] concrete definition of done

## Commit

After the verifier passes, commit meaningful work. Example:

```bash
git add .
git commit -m "Day 3: Lock The Spec"
```

## Next

After this day is verified, continue to Day 4.
