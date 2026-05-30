# Day Done Protocol

Say this to your coding harness when you believe a day is finished:

```text
day done
```

Your harness should:

1. Read `.onemillion/state.json`.
2. Read the current day's completion gate from `course-manifest.json`.
3. Inspect files and app behavior it can inspect.
4. Ask you for manual confirmation where needed.
5. Write `.onemillion/verification-day-XX.md`.
6. Update `.onemillion/state.json`.
7. Tell you the next day and what you will learn.

If a gate is missing, the harness should not advance you. It should give the next smallest action.

