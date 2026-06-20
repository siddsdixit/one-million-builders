# Day 13 - Product Polish + UX Finish

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="./README.md">Day Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>


This is the learner cockpit for Day 13. Start here, then use the linked files for depth.

## Outcome

By the end of today, you will complete the Day 13 completion gate from `course/course-manifest.json` and update `.onemillion/state.json` through your harness.

## Watch / Read / Build

- [Watch](./loom.md) the worked example when the recording is available.
- [Learn](./learn.md) the concept before asking the harness to work.
- [Build](./build.md) using the step-by-step guide.
- [Recover](./stuck.md) if something breaks or feels unclear.
- [Resources](./resources.md) are optional after the day is complete.

## Tutor Prompt

Paste this into your harness from the repo root:

```text
I am on OneMillion Day 13: Product Polish + UX Finish.

Act as the `build` agent for this day.
First teach me the day in plain language.
Then guide me one step at a time using course/days/day-13-product-polish/learn.md, course/days/day-13-product-polish/build.md, course/days/single.md, and course/course-manifest.json.
Ask for my human decisions before changing product-defining artifacts or code.
Show what you changed and ask me to inspect it.
When I say `day done`, verify the completion gate and update .onemillion/state.json.
Do not advance me if the gate is incomplete.
```

## Decisions The Learner Must Own

- target-user product feel
- UX problems to fix now versus defer
- AI output display/save/review/edit/accept behavior
- AI waiting state
- AI failure state
- core workflow success state

## External Tools

- Supabase
- Vercel

Use `course/docs/account-setup.md` for exact links, permissions, and QA checks.

## Done Checklist

- [ ] main MVP flow is easy to understand without explanation
- [ ] empty/loading/error/success states are present where needed
- [ ] AI feature has clear waiting, output, retry, and review behavior
- [ ] mobile and desktop layouts do not overlap or break
- [ ] target-user pain point still feels central

## Commit

After the verifier passes, commit meaningful work. Example:

```bash
git add .
git commit -m "Day 13: Product Polish + UX Finish"
```

## Next

After this day is verified, continue to Day 14.
