# Day 0 - If You Are Stuck

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="./README.md">Day Home</a>
</p>



## Universal Recovery Prompt

Paste this into your harness:

```text
I am on OneMillion Day 0: Orientation + Commitment + GitHub Workspace.
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

## Common Day 0 Issues

- `origin` points to Sid's repo instead of your fork: change `origin` to your fork before starting.
- You cloned a zip or loose folder: clone your fork with git instead.
- Commitment feels too public: use the private-message path to 5 real people.
- GitHub CLI is not installed: do the fork/star steps in the browser and set remotes manually.
