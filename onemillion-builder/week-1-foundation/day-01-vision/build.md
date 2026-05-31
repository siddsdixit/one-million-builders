# Day 1 — Build Guide

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="../README.md">Week Overview</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**No code today.** This is your "learn the OneMillion pipeline, set up your product folder, and write down your idea" day.

If you've already done [getting-started.md](../../docs/getting-started.md), you have all the tools. We're just creating a folder and a file.

---

## Before You Start

- [ ] Terminal is open (Mac: Terminal app. Windows: Git Bash.)
- [ ] You have read the OneMillion pipeline section in [learn.md](./learn.md)
- [ ] You've decided on a `product_type` (web_app / ai_agent / hybrid) — see [learn.md](./learn.md) Part 3
- [ ] You've drafted an idea (2 sentences) — see [learn.md](./learn.md) Today's Assignment

---

## Step 1: Ask Your Harness To Explain The Pipeline

Before you create files, make the harness teach the OneMillion development pipeline in plain language:

```text
I am on OneMillion Day 1.

Before we create files, explain the OneMillion development pipeline:
idea -> research -> PRD -> validate spec -> design -> plan -> build -> review -> test -> guard -> ship -> sell.

For each stage, tell me:
1. what the stage is for,
2. which OneMillion agent helps,
3. what artifact gets produced,
4. why this matters for my product.

Keep it beginner-friendly and then help me pick my Day 1 product direction.
```

You should understand that Day 1 is not random brainstorming. It is the first stage of the pipeline.

---

## Step 2: Create Your Project Folder

In your terminal, navigate to the root of your cloned course fork:

```bash
cd /path/to/teach-one-million
```

Then create the product folder inside that course repo:

```bash
mkdir my-onemillion-build
cd my-onemillion-build
```

**You should see:** Your terminal prompt now shows you're inside `my-onemillion-build`.

> 💡 Keep the product folder inside your cloned course repo. The installer and verifier expect `teach-one-million/my-onemillion-build` unless your harness deliberately updates `.onemillion/state.json`.

---

## Step 3: Create The Hidden Course Folder

The course uses a folder called `.onemillion/` (the dot makes it hidden) to track your progress and store course-specific files. Create it:

```bash
mkdir .onemillion
```

**You should see:** Nothing visible if you run `ls`, because `.onemillion/` is hidden. Run `ls -la` to see all files including hidden ones.

---

## Step 4: Create Your Progress Tracker

The course uses `.onemillion/progress.md` as your restart point. If you fall behind, this file tells you where to resume.

Create `.onemillion/progress.md` and paste this:

```markdown
# OneMillion Progress

## Builder

- **Builder name:** [Your name]
- **Product name:** [Product name or "not named yet"]
- **Target user:** [Specific user]
- **Current day:** Day 1
- **Last verified day:** None

## Links

- **GitHub repo:** [add on Day 4]
- **Live URL:** [add on Day 4]
- **Supabase project:** [add on Day 5]
- **Vercel project:** [add on Day 4]
- **Demo Loom:** [add on Day 18]

## Current State

- **What works now:** Day 1 setup in progress
- **Current blocker:** None
- **Next smallest action:** Finish project.json
```

Fill in your name, product name if you have one, and target user. A fuller template lives at [templates/progress.md](../../docs/templates/progress.md).

---

## Step 5: Create `project.json`

This file holds the answers to "what am I building?" The verifier reads it on every day to check your progress.

Open your editor:

```bash
code .            # opens VS Code in this folder
```

In your editor, create a new file: `.onemillion/project.json`

Paste this in, then **edit the values** to match YOUR product:

```json
{
  "product_type": "web_app",
  "idea": "Yoga studio owners spend hours each week manually following up with clients who didn't rebook. I want a tool that automates the follow-up while letting the owner approve each message before it goes.",
  "builder_name": "Your Name",
  "started_at": "2026-05-18"
}
```

**Replace:**
- `product_type` → `web_app`, `ai_agent`, or `hybrid`
- `idea` → your 2-sentence idea from learn.md
- `builder_name` → your actual name
- `started_at` → today's date

Save the file.

---

## Step 6: Run Day 1 Verification

You're going to ask your coding harness to check your work. This is how every day ends — the AI verifies that you actually did what you were supposed to.

In your terminal, in `my-onemillion-build`:

```bash
claude
```

Your coding harness starts. Once it is ready, ask it to run the day verifier or paste the fallback verifier prompt.

**You should see:** Claude reads your `.onemillion/project.json`, checks each requirement, and reports back. Either:
- ✅ **Pass** — Day 1 complete, you can move on to Day 2
- ⚠️ **Needs revision** — specific feedback on what to fix

If needs revision, fix the issues and re-paste the verification prompt.

---

## What Should Be True After Day 1

- [ ] `teach-one-million/my-onemillion-build/` folder exists inside your cloned course repo
- [ ] `.onemillion/progress.md` exists
- [ ] `.onemillion/project.json` exists and is valid JSON
- [ ] `product_type` is one of `web_app`, `ai_agent`, or `hybrid`
- [ ] `idea` is 2 sentences with a specific user and specific pain
- [ ] You can explain the OneMillion pipeline in plain language
- [ ] You know which agent is helping today: `idea`
- [ ] Verification ran and returned "Pass" (or you've addressed all revision notes)

---

## Update Your Progress Tracker

Before you close today, open `.onemillion/progress.md` and update:

- **Current day:** Day 1 complete
- **Last verified day:** Day 1
- **Current blocker:** None, or the exact blocker to resume from
- **Next smallest action:** Open Day 2.

If verification did not pass yet, keep **Last verified day** at the previous passed day and write the blocker clearly.

## If You Are Stuck

Open your coding harness from your project folder:

```bash
claude
```

Paste this:

```text
I am on OneMillion Day 01.

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
| `mkdir: command not found` | You're on Windows in CMD. Switch to Git Bash. |
| `mkdir: cannot create directory: Permission denied` | You're trying to create in a protected folder. Run `cd ~` first to go to your home folder. |
| Editor command `code` not found | Open VS Code manually, then File → Open → navigate to your folder. Then in VS Code: Cmd/Ctrl+Shift+P → "Shell Command: Install 'code' command". |
| JSON syntax error in verification | Check for missing commas, missing quotes, or trailing commas. Use [jsonlint.com](https://jsonlint.com) to find the issue. |
| your harness says "I can't find project.json" | Make sure you're running `claude` from inside `my-onemillion-build`, not from your home folder. |
| `.onemillion/` folder not visible | It's hidden (starts with `.`). Use `ls -la` to see it, or in VS Code use Cmd+Shift+. to toggle hidden files. |

---

→ **Done with Day 1?** Move to [Day 2 — Problem + Research](../day-02-problem/learn.md).
