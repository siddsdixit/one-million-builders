# Day 12 - First AI Build

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="./README.md">Day Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>


This is the learner cockpit for Day 12. Start here, then use the linked files for depth.

## Outcome

By the end of today, you will complete the Day 12 completion gate from `course/course-manifest.json` and update `.onemillion/state.json` through your harness.

## Watch / Read / Build

- [Watch](./loom.md) the worked example when the recording is available.
- [Learn](./learn.md) the concept before asking the harness to work.
- [Build](./build.md) using the step-by-step guide.
- [Recover](./stuck.md) if something breaks or feels unclear.
- [Resources](./resources.md) are optional after the day is complete.

## Tutor Prompt

Paste this into your harness from the repo root:

```text
I am on OneMillion Day 12: First AI Build.

Act as the `build` agent for this day.
First teach me the day in plain language.
Then guide me one step at a time using course/days/day-12-first-ai-build/learn.md, course/days/day-12-first-ai-build/build.md, course/days/single.md, and course/course-manifest.json.
Ask for my human decisions before changing product-defining artifacts or code.
Show what you changed and ask me to inspect it.
When I say `day done`, verify the completion gate and update .onemillion/state.json.
Do not advance me if the gate is incomplete.
```

## Decisions The Learner Must Own

- prompt behavior
- sample inputs
- first output quality
- selected provider and env var name
- what product data is safe to send
- what product data must be redacted before sending to AI
- whether output is displayed, saved, reviewed, edited, sent, scheduled, or acted on
- whether the user must approve output before saving, sending, scheduling, or acting

## Executive Assistant Safety Check

If your feature drafts reminders, summaries, follow-ups, calendar prep, inbox replies, meeting notes, or executive communications, keep the first AI build draft-only.

- Redact sensitive details before the server-side AI call.
- Show the user what context will be sent when practical.
- Do not auto-send, auto-schedule, or auto-share AI output.
- Add a visible review/edit/approval step before any final action.
- Make the failure state safe: no partial send, no leaked secret, no hidden background action.

## External Tools

- Anthropic
- Vercel

Use `course/docs/account-setup.md` for exact links, permissions, and QA checks.

## Done Checklist

- [ ] AI route or server action exists
- [ ] AI output appears in app
- [ ] selected provider key is stored in .env.local
- [ ] selected provider key is stored in Vercel env vars
- [ ] .env.example has placeholders only
- [ ] API key is not exposed to client code
- [ ] local app AI path works
- [ ] live app AI path works
- [ ] common error states are handled

## Commit

After the verifier passes, commit meaningful work. Example:

```bash
git add .
git commit -m "Day 12: First AI Build"
```

## Next

After this day is verified, continue to Day 13.
