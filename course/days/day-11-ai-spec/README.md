# Day 11 - AI Feature Spec

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="./README.md">Day Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>


This is the learner cockpit for Day 11. Start here, then use the linked files for depth.

## Outcome

By the end of today, you will complete the Day 11 completion gate from `course/course-manifest.json` and update `.onemillion/state.json` through your harness.

## Watch / Read / Build

- [Watch](./loom.md) the worked example when the recording is available.
- [Learn](./learn.md) the concept before asking the harness to work.
- [Build](./build.md) using the step-by-step guide.
- [Recover](./stuck.md) if something breaks or feels unclear.
- [Resources](./resources.md) are optional after the day is complete.

## Tutor Prompt

Paste this into your harness from the repo root:

```text
I am on OneMillion Day 11: AI Feature Spec.

Act as the `spec` agent for this day.
First teach me the day in plain language.
Then guide me one step at a time using course/days/day-11-ai-spec/learn.md, course/days/day-11-ai-spec/build.md, course/days/single.md, and course/course-manifest.json.
Ask for my human decisions before changing product-defining artifacts or code.
Show what you changed and ask me to inspect it.
When I say `day done`, verify the completion gate and update .onemillion/state.json.
Do not advance me if the gate is incomplete.
```

## Decisions The Learner Must Own

- AI job-to-be-done
- provider/model preference
- simple AI feature versus agentic workflow
- what data the AI can see
- what data must be redacted before AI sees it
- whether tool calling is needed
- whether the user must approve output before saving, sending, scheduling, or acting
- quality bar

## Executive Assistant Safety Check

If your product uses meeting notes, calendar details, inbox snippets, personnel details, board topics, compensation, health information, or client-sensitive data, treat Day 11 as a privacy-design day.

- Define the redaction step before the model call.
- Prefer draft-only AI output for the MVP.
- Require human review and approval before anything is saved, sent, scheduled, or shared.
- Record what the AI is not allowed to see.
- Record what the AI is not allowed to do.

## External Tools

- None required by the manifest for this day.

## Done Checklist

- [ ] refined PRD includes the selected AI feature
- [ ] provider/model choice is recorded
- [ ] API key and secret-storage plan is recorded
- [ ] input/output contract is recorded
- [ ] tool-calling decision is recorded
- [ ] AI behavior is measurable
- [ ] failure modes, privacy boundary, latency, and cost budget are recorded

## Commit

After the verifier passes, commit meaningful work. Example:

```bash
git add .
git commit -m "Day 11: AI Feature Spec"
```

## Next

After this day is verified, continue to Day 12.
