# Day 3 — Build Guide

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="../README.md">Week Overview</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Last "no code" day.** You're writing the PRD with Claude's help, then locking it.

---

## Before You Start

- [ ] Day 2 verified (3+ conversations recorded)
- [ ] You've read [learn.md](./learn.md) (especially Part 2 — the 5 sections)
- [ ] Terminal open, in your `my-onemillion-build` folder

---

## Step 1: Start your coding harness

```bash
cd ~/my-onemillion-build
claude
```

Wait for Claude to start.

---

## Step 2: Draft Your PRD With Claude

Pick one of the two approaches from learn.md.

### Approach 1 — Direct Draft (best for: engineers, PMs who like to write)

In Claude, paste this:

```
I'm starting Day 3 of OneMillion. I need to write a PRD with exactly 5
sections: Problem, User (one named person), 3 Core Features (user story format),
Out of Scope, Definition of Done.

Here are my conversation notes:
[paste contents of .onemillion/notes.md]

Here's my idea from Day 1:
[paste contents of .onemillion/project.json]

Draft my PRD. Push back if any section feels vague or generic. The goal is
to lock scope today so I can start building tomorrow.
```

Claude drafts. Review it. If a section feels off, ask Claude to revise that specific section. Iterate 2-3 times until it sings.

### Approach 2 — Interview Mode (best for: EAs, builders who feel stuck)

In Claude, paste this:

```
I'm starting Day 3 of OneMillion. Help me write my PRD by asking me one
question at a time, section by section.

Here are my Day 2 conversation notes:
[paste contents of .onemillion/notes.md]

Start with Section 1 (Problem): ask me what specific pain my user feels, with
evidence from my conversations.
```

Claude asks a question. You answer. Claude asks the next. By the end, your PRD writes itself.

---

## Step 3: Save The PRD

Once you're happy with Claude's draft, ask Claude to save it:

```
This looks good. Save the final PRD to .onemillion/prd.md
```

**You should see:** Claude creates the file. Confirm by running:

```bash
ls .onemillion/
```

You should see: `project.json`, `notes.md`, `prd.md`, and possibly verification files from earlier days.

---

## Step 4: Read Your PRD Aloud

Yes, aloud. Out loud. To yourself.

This is the easiest quality check. If a section sounds like marketing fluff when you read it aloud, it's not specific enough. If you stumble over a feature, it's not clear enough. If the Definition of Done doesn't feel concrete, you'll never feel done.

Edit anything that feels off. Re-save.

---

## Step 5: Lock Scope

In your terminal:

```bash
git init                            # initialize git (if not already)
git add .onemillion/prd.md
git commit -m "Day 3: PRD locked"
```

That commit is your scope lock. From this point forward, **the PRD does not change** without an explicit conversation with yourself (or your cohort) about WHY.

If you want to add a feature later, it goes in "v2 or later" — not v1.

---

## Step 6: Run Day 3 Verification

```bash
claude
```

Paste the contents of [`ai-instructions-day-03.md`](./ai-instructions-day-03.md).

Claude reads `prd.md`, checks all 5 sections, validates user story format, and reports pass / needs-revision.

---

## What Should Be True After Day 3

- [ ] `.onemillion/prd.md` exists with all 5 sections
- [ ] Section 3 has exactly 3 user stories in `As [user], I want [action] so that [outcome]` format
- [ ] Section 4 has at least 5 out-of-scope items
- [ ] You've committed the PRD to git
- [ ] Verification passed ✅

---

## Update Your Progress Tracker

Before you close today, open `.onemillion/progress.md` and update:

- **Current day:** Day 3 complete
- **Last verified day:** Day 3
- **Current blocker:** None, or the exact blocker to resume from
- **Next smallest action:** Open Day 4.

If verification did not pass yet, keep **Last verified day** at the previous passed day and write the blocker clearly.

## If You Are Stuck

Open your coding harness from your project folder:

```bash
claude
```

Paste this:

```text
I am on OneMillion Day 03.

Here is the step I was trying to complete:
[paste the step heading or instructions]

Here is what happened:
[paste the error, terminal output, or describe what I see]

Diagnose the likely cause and give me the next smallest action.
Do not rewrite unrelated code.
Ask for one missing detail at a time if needed.
```

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Claude wrote a 10-section PRD | Tell it: "Reduce to exactly 5 sections: Problem, User, 3 Features, Out of Scope, Definition of Done. No more." |
| My PRD has 5 features instead of 3 | Cut to the 3 most essential. Move the rest to Out of Scope. This is the hardest part of Day 3. |
| My user story format is wrong | Format must be exactly: `As [user], I want [action] so that [outcome]`. Claude can fix this — ask it. |
| I keep wanting to pivot to a new idea | After Day 3, don't pivot. Ship this one. Then build the next idea. The skill compounds. |
| `git init` failed | Make sure you're in `my-onemillion-build` folder, not your home folder. `cd ~/my-onemillion-build` first. |
| Don't know what counts as "out of scope" | Anything you imagined adding that isn't one of your 3 core features. Brainstorm 5+ things you WON'T build. |

---

→ **Done with Day 3?** Move to [Day 4 — Stack + First Deploy](../day-04-stack/learn.md). Tomorrow you write actual code.
