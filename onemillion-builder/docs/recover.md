# I Fell Behind

You are not behind. The 18 days are units of progress, not calendar days.

Use this page when you stopped for a few days or weeks and need to restart without rereading everything.

---

## Step 1: Find Your Last Verified Day

Open your project folder and check:

```bash
cat .onemillion/state.json
```

Look for `last_verified_day` and the `verification.days` object.

If `last_verified_day` is missing, restart at [Day 1](../day-01-idea/learn.md).

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
Here is my OneMillion state:
[paste .onemillion/state.json]

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
| None | [Day 1](../day-01-idea/learn.md) |
| Day 1 | [Day 2](../day-02-validate-prd/learn.md) |
| Day 2 | [Day 3](../day-03-spec/learn.md) |
| Day 3 | [Day 4](../day-04-first-deploy/learn.md) |
| Day 4 | [Day 5](../day-05-auth-db/learn.md) |
| Day 5 | [Day 6](../day-06-core-feature/learn.md) |
| Day 6 | [Day 7](../day-07-ai-spec/learn.md) |
| Day 12 | [Day 13](../day-13-production-hygiene/learn.md) |
| Day 17 | [Day 18](../day-18-demo/learn.md) |

For any other day, open the next day in the same day folder.

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
