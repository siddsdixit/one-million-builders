# I Fell Behind

You are not behind. The 18 days are units of progress, not calendar days.

Use this page when you stopped for a few days or weeks and need to restart without rereading everything.

---

## Step 1: Find Your Last Verified Day

Open your project folder and check:

```bash
ls .onemillion/verification-day-*.md
```

The highest numbered file is your last completed checkpoint.

If you have no verification files yet, restart at [Day 1](../week-1-foundation/day-01-vision/learn.md).

---

## Step 2: Check Your Current App State

Run:

```bash
npm run dev
```

Open `http://localhost:3000`.

If the app starts, you are in good shape. If it fails, copy the error.

---

## Step 3: Ask Your Harness To Resume With You

Open your coding harness from the course repo or your product folder. Ask it to read `AGENTS.md` if it has not already.

Paste this:

```text
I am returning to OneMillion after a break.

My last verified day appears to be Day [X].
Here are my verification files:
[paste output of ls .onemillion/verification-day-*.md]

Here is what happens when I run npm run dev:
[paste result or error]

Inspect my project and tell me:
1. What day I should resume from
2. Whether my app is currently healthy
3. The next smallest action I should take
4. Which OneMillion agent I should use next

Do not rewrite unrelated code. Ask for one missing detail at a time if needed.
```

---

## Step 4: Resume From The Next Day

If your last verified day is:

| Last verified | Resume here |
|---------------|-------------|
| None | [Day 1](../week-1-foundation/day-01-vision/learn.md) |
| Day 1 | [Day 2](../week-1-foundation/day-02-problem/learn.md) |
| Day 2 | [Day 3](../week-1-foundation/day-03-prd/learn.md) |
| Day 3 | [Day 4](../week-1-foundation/day-04-stack/learn.md) |
| Day 4 | [Day 5](../week-1-foundation/day-05-auth/learn.md) |
| Day 5 | [Day 6](../week-1-foundation/day-06-core-feature/learn.md) |
| Day 6 | [Week 2](../week-2-make-it-ai/README.md) |
| Day 12 | [Week 3](../week-3-ship-and-sell/README.md) |
| Day 17 | [Day 18](../week-3-ship-and-sell/day-18-demo/learn.md) |

For any other day, open the next day in the same week folder.

---

## Step 5: Post A Tiny Restart Update

Use this if public accountability helps:

```text
Restarting my OneMillion build today.

Last verified checkpoint: Day [X].
Next step: Day [Y].

No shame, no streaks. Just back to building.

#BuildingWith1M
```
