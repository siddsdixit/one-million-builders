# Day 1 — Build Guide

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="../README.md">Week Overview</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**No code today.** This is your "set up your project folder and write down your idea" day.

If you've already done [getting-started.md](../../docs/getting-started.md), you have all the tools. We're just creating a folder and a file.

---

## Before You Start

- [ ] Terminal is open (Mac: Terminal app. Windows: Git Bash.)
- [ ] You've decided on a `product_type` (web_app / ai_agent / hybrid) — see [learn.md](./learn.md) Part 2
- [ ] You've drafted an idea (2 sentences) — see [learn.md](./learn.md) Today's Assignment

---

## Step 1: Create Your Project Folder

In your terminal, navigate to where you want the project to live. Usually your home folder:

```bash
cd ~
```

Then create the project folder:

```bash
mkdir my-onemillion-build
cd my-onemillion-build
```

**You should see:** Your terminal prompt now shows you're inside `my-onemillion-build`.

> 💡 You can name the folder anything you want — `yoga-followup` or `client-tracker` or whatever fits your idea. The course uses `my-onemillion-build` as a placeholder.

---

## Step 2: Create The Hidden Course Folder

The course uses a folder called `.onemillion/` (the dot makes it hidden) to track your progress and store course-specific files. Create it:

```bash
mkdir .onemillion
```

**You should see:** Nothing visible if you run `ls`, because `.onemillion/` is hidden. Run `ls -la` to see all files including hidden ones.

---

## Step 3: Create Your Progress Tracker

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

## Step 4: Create `project.json`

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

## Step 5: 🎉 Bonus — Deploy Your First URL (10 min, browser only)

Before you finish Day 1, you're going to put your name on the internet.

This is the magic moment. No coding. No terminal. Just a browser. By the end of these 10 minutes you'll have a real URL — `your-name.vercel.app` — that anyone in the world can visit. **Day 1 ends with you having shipped something public.**

### Step 4a — Open Vercel's template gallery
Go to [vercel.com/templates/next.js](https://vercel.com/templates/next.js) (any free Next.js template works — recommended: pick the simplest one, like "Next.js Starter" or "Hello World").

### Step 4b — Click "Deploy"
You'll be asked to sign in to Vercel (use your GitHub if you've set that up; otherwise sign in with email).

### Step 4c — Pick a project name
Use something like `[your-first-name]-onemillion-day-1` (e.g., `priya-onemillion-day-1`).

Click **Create**. Vercel does the rest — clones the template, deploys it, gives you a URL.

### Step 4d — Wait 60 seconds, then click your URL
Your URL will be `https://[whatever-you-named-it].vercel.app`. Open it.

**You should see:** a working Next.js homepage. It's not yours yet — it's a template. But it's running on the internet, with your name in the URL, deployed by you.

### Step 4e — Send the URL to ONE person
A friend. Your spouse. A coworker. Your group chat. Whoever. Say:

> "Day 1 of OneMillion done. Started building. Here's my URL: [your URL]. Going to make it real over the next 17 days."

That's the public commitment. You shipped on Day 1. You're not a course-taker anymore. You're a builder.

> 💡 **Why this matters:** Most courses end Day 1 with "write something in a journal." OneMillion ends Day 1 with a live URL and a public commitment. You now have skin in the game. Day 4 (the hard day) doesn't feel like quitting an idea — it feels like quitting something real you already shipped.

> 🔧 **Engineers:** Yes, this is just a Vercel template deploy. We use it as a psychological hook, not a technical exercise. The real Day 4 work (creating your own Next.js project locally with proper structure) still happens. Trust the process.

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

- [ ] `~/my-onemillion-build/` folder exists
- [ ] `.onemillion/progress.md` exists
- [ ] `.onemillion/project.json` exists and is valid JSON
- [ ] `product_type` is one of `web_app`, `ai_agent`, or `hybrid`
- [ ] `idea` is 2 sentences with a specific user and specific pain
- [ ] **Your Vercel template URL is live** (e.g., `https://your-name-onemillion-day-1.vercel.app`)
- [ ] You sent the URL to at least one person (public commitment moment)
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

→ **Done with Day 1?** Move to [Day 2 — Problem + Mom Test](../day-02-problem/learn.md).
