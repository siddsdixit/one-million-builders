# Day Done Protocol

Say this to your coding harness when you believe a day is finished:

```text
day done
```

Your harness should:

1. Read `.onemillion/state.json`.
2. Read the current day's completion gate from `course-manifest.json`.
3. Open the current day `README.md` and `build.md`.
4. Inspect files and app behavior it can inspect.
5. Ask you for manual confirmation where needed.
6. Compare the evidence to the completion gate.
7. If anything is missing, stop and give the smallest next action.
8. If the gate passes, update verification status inside `.onemillion/state.json`.
9. Preserve the active pipeline artifacts and code.
10. Tell you the next day and what you will learn.

If a gate is missing, the harness should not advance you. It should give the next smallest action.

## What Should Happen Before You Say It

Your harness should not simply tell you "do Day X." At the start of each day it should:

1. Greet and orient you.
2. Explain what today's lesson is about.
3. Explain why it matters.
4. Give the exact actions and copy-ready text or commands.
5. Tell you what counts as done.

Only say `day done` after the done checklist is actually true.

## If The Gate Fails

Failure is normal. The harness should not shame you or jump ahead. It should:

1. Name the missing gate item.
2. Point to the relevant part of the current day `build.md` or `stuck.md`.
3. Give one next action.
4. Re-check only after that action is complete.
