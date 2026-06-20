# Day 15 - QA + Production Readiness

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="./README.md">Day Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>


This is the learner cockpit for Day 15. Start here, then use the linked files for depth.

## Outcome

By the end of today, you will complete the Day 15 completion gate from `course/course-manifest.json` and update `.onemillion/state.json` through your harness.

## Watch / Read / Build

- [Watch](./loom.md) the worked example when the recording is available.
- [Learn](./learn.md) the concept before asking the harness to work.
- [Build](./build.md) using the step-by-step guide.
- [Recover](./stuck.md) if something breaks or feels unclear.
- [Resources](./resources.md) are optional after the day is complete.

## Tutor Prompt

Paste this into your harness from the repo root:

```text
I am on OneMillion Day 15: QA + Production Readiness.

Act as the `test` agent for this day.
First teach me the day in plain language.
Then guide me one step at a time using course/days/day-15-qa-production-readiness/learn.md, course/days/day-15-qa-production-readiness/build.md, course/days/single.md, and course/course-manifest.json.
Ask for my human decisions before changing product-defining artifacts or code.
Show what you changed and ask me to inspect it.
When I say `day done`, verify the completion gate and update .onemillion/state.json.
Do not advance me if the gate is incomplete.
```

## Decisions The Learner Must Own

- critical paths that must pass before shipping
- which tests should be automated now
- which tests can remain manual for MVP
- AI pass/fail examples and quality threshold
- what defects block Day 16
- accepted non-critical risks

## External Tools

- Supabase
- Vercel
- Anthropic

Use `course/docs/account-setup.md` for exact links, permissions, and QA checks.

## Done Checklist

- [ ] local build/test commands pass or failures are understood and fixed/deferred
- [ ] manual QA covers the main user journey, auth, data, AI feature, and error states
- [ ] automated tests cover the highest-risk behavior the repo can support
- [ ] live deployment is checked for the critical path
- [ ] AI pass/fail examples produce acceptable behavior
- [ ] no Day 14 critical security/trust blocker remains
- [ ] production-blocking bugs are fixed before Day 16
- [ ] accepted risks are explicit in the existing state/verification trail

## Commit

After the verifier passes, commit meaningful work. Example:

```bash
git add .
git commit -m "Day 15: QA + Production Readiness"
```

## Next

After this day is verified, continue to Day 16.
