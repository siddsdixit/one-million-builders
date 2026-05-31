# Day 0 — Public Commitment

**Time: 10-15 minutes. Mandatory before Day 1.**

Before you start Day 1, set up your fork and make a commitment. Publicly if you can. Privately to five real people if you cannot post yet.

This sounds small. It is the course's first real learning gate: you create a public workspace, prove you can work from your own fork, and make it harder to disappear when the build gets uncomfortable.

---

## Harness Opening Script

If you are a coding harness teaching this course, render this before asking the learner to do anything:

```text
Welcome to OneMillion. I will be your course guide inside this coding harness.

Here is what this course is:
Over 18 build-days, you will go from an idea to a deployed AI product. You will build in a real GitHub repo, deploy to a real URL, add auth and a database, add an AI feature, collect feedback, record a Loom demo, and submit a Builder Claim.

Here is how we will work:
- I will teach one day at a time.
- I will explain the concept before the task.
- I will give you exact commands, links, prompts, and checklists.
- I will inspect files and run verifiers where I can.
- You will make the product decisions.
- You will touch the real external tools yourself.
- When a day is complete, you will say `day done`; I will verify and advance you.

Today is Day 0: Public Commitment + Fork Setup.

The goal today is not coding. The goal is to create accountability and prove that your course repo is correctly set up from your own fork.

What you will do now:
1. Confirm the GitHub fork/clone setup is correct.
2. Make a public commitment, or privately send the commitment to 5 real people.
3. Come back and say `day done`.

Copy the message below. You may post it on LinkedIn/X, or send it privately by text, email, Slack, WhatsApp, or DM.
```

Then show the commitment template from this page. Do not summarize it away.

End the opening with:

```text
What counts as done for Day 0:
- The repo is a real clone of your fork.
- `origin` points to your fork.
- `upstream` points to Sid's repo.
- You starred/forked the upstream repo.
- You made the public or private commitment.

After those are true, come back and type:

day done
```

Do not say only "do Day 0." The learner needs the full orientation.

---

## Required Setup

Do not skip this. Your coding harness should stop the course if any item is missing.

Open the exact setup playbook first: [Account Setup Playbook](../docs/account-setup.md#day-0-github-course-fork)

- [ ] Starred `siddsdixit/teach-one-million`
- [ ] Forked `siddsdixit/teach-one-million` into your own GitHub account
- [ ] Cloned your fork locally
- [ ] `origin` points to your fork
- [ ] `upstream` points to `siddsdixit/teach-one-million`
- [ ] Opened the cloned fork in your coding harness

Run this from the repo root if you have not already:

```bash
./onemillion-builder/install-agents.sh
```

### If You Do Not Have GitHub Yet

1. Create an account: https://github.com/signup
2. Open the course repo: https://github.com/siddsdixit/teach-one-million
3. Click **Star**.
4. Fork directly: https://github.com/siddsdixit/teach-one-million/fork
5. Install GitHub CLI if you want the easiest terminal path: https://cli.github.com/
6. If Git is not installed, use GitHub's setup guide: https://docs.github.com/en/get-started/git-basics/set-up-git

### QA: Prove The Setup Is Correct

Run:

```bash
git remote -v
git rev-parse --show-toplevel
test -f AGENTS.md
test -f onemillion-builder/course-manifest.json
```

You pass Day 0 setup only when:

- `origin` contains your GitHub username.
- `upstream` contains `siddsdixit/teach-one-million`.
- You are not working from a downloaded zip.
- Your harness can read `AGENTS.md` and `onemillion-builder/course-manifest.json`.

---

## Why This Works

The single biggest predictor of whether someone finishes a self-paced course isn't intelligence, time, or experience. It's **public commitment.**

When you post that you're starting OneMillion:
- Your network sees you start. They expect you to finish.
- Day 4 (the hard day) becomes "I'm not going to be the person who quit publicly on Day 4"
- Your network becomes your accountability partner. Some will check in. Some will encourage you. Some will follow your daily updates.
- People you've never met may DM you to say "I'm doing this too." Instant cohort, even if you're self-serve.

Builders who post on Day 0 finish at roughly **2x the rate** of those who don't. This is one of the most consistent findings across MOOC research.

Five minutes of cringe → 2x odds of finishing → a real product on the internet. Take the deal.

---

## The LinkedIn Template

Copy. Paste. Customize. Post.

```
Starting #OneMillion today.

The plan: in 18 days, build and ship a real AI-native product from scratch.
1-2 hours/day. Free, open source. Anyone can do this.

I'm building: [your one-sentence idea — keep it specific, or "idea gets locked on Day 1"]

For: [the specific person you're building it for — name them, or "specific user gets locked on Day 1"]

I'll post a quick update at the end of each day. If you have feedback, ideas,
or are doing this too, hit me in the comments.

The course is open source — anyone can join. Repo:
https://github.com/siddsdixit/teach-one-million

Day 1 starts now. Tagging @Sid Dixit (who built this).

Let's see what 18 days of compounded building looks like.
```

---

## The X (Twitter) Version

```
Starting OneMillion today.

Building a real AI-native product from scratch in 18 days. 1-2 hours/day.
Free, open source.

Building: [your one-sentence idea, or idea gets locked on Day 1]
For: [specific person, or specific user gets locked on Day 1]

Will post a daily update.

Day 1 → 🚀
#BuildingWith1M
```

---

## Optional: The Photo

Take one of these to attach:
- A screenshot of `https://github.com/siddsdixit/teach-one-million` open in your browser
- A photo of you at your laptop with your terminal open
- Just text-only — also fine

---

## What To Expect

- **First 30 min after posting:** mostly silence. Normal.
- **First 2 hours:** ~5-15 reactions, a few comments.
- **By end of Day 1:** someone you haven't talked to in years will message you saying "wait, I want to do this too."
- **By Day 4:** at least one person will ask "how's it going?" — that's accountability.
- **By Day 18:** the people who reacted on Day 0 will see your finished product. They'll remember.

---

## What If I Don't Have A Big Following?

It works at any size. 100 followers is enough. 1000 is plenty. The mechanism isn't reach — it's **commitment to specific humans you know.**

Even sending the same text as a DM to 5 close friends works. The mechanism is "people I respect now expect me to do this."

---

## What If I'm Anxious About Posting?

You're not the first. Most builders feel cringe about Day 0. Do it anyway.

The cringe lasts 30 minutes. The retention boost lasts 18 days.

Worst case: nobody reacts and you finish anyway. Best case: you build a small audience following your build, which makes Day 17 (launch) 10x easier — you have people waiting to see what you shipped.

Either way: you win.

---

## Now: Go Post It

Then come back and tell your coding harness:

```text
day done
```

Your harness should verify the fork/clone/upstream setup and commitment before it starts [Day 1](../week-1-foundation/day-01-vision/learn.md).
