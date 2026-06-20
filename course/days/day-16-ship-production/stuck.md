# Day 16 - If You Are Stuck

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="./README.md">Day Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>


## Universal Recovery Prompt

Paste this into your harness:

```text
I am on OneMillion Day 16: Ship Production.
I am stuck.

What I was trying to do:
[paste the step]

What I expected:
[describe]

What happened instead:
[paste the error, screenshot text, or behavior]

Please diagnose the smallest next action.
Teach the missing concept briefly.
Do not skip my required human decisions.
Do not advance the day until the completion gate is true.
```

## First Checks

- Confirm you are in the forked `one-million-builders` repo, not a downloaded zip.
- Confirm `.onemillion/state.json` exists or ask the harness to create/repair it from the manifest.
- Confirm the previous day is marked complete before continuing.
- Re-open this day's `build.md` and compare your current state against the done checklist.
- If an external dashboard is involved, open `course/docs/account-setup.md` and verify the exact URL, permission, and QA check.

## Common Day 16 Issues

- Production URL loads but auth fails: check Supabase Site URL and redirect URLs.
- Monitoring is incomplete: configure it or explicitly defer with a reason.
- Custom domain delays launch: document skip and use the Vercel production URL.

## Recovery Order

1. Re-read [learn.md](./learn.md) for the concept.
2. Re-open [build.md](./build.md) and find the first unchecked requirement.
3. Ask the harness for the smallest next action using the recovery prompt above.
4. Run the verifier only after the done checklist is true.
