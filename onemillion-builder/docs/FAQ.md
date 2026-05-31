# FAQ

The 12 questions everyone asks. Bookmark this; you'll come back.

---

## 1. Do I really not need to know how to code?

Correct. The AI writes the code. You direct it.

Most people who finish this course never wrote a line of code before Day 1. They wrote a clear spec, ran agents, reviewed what came out, and shipped. That's the whole skill. By Day 18 you'll have a deployed product and a feel for HOW software comes together — which is more useful than knowing a specific language.

Engineers: yes, you'll learn things too. The agentic SDLC framework is genuinely new — most engineers don't yet have a good intuition for spec-driven AI development. That's what you're here for.

---

## 2. How much time does this actually take?

| Audience | Per day | Total over 18 days |
|----------|---------|--------------------|
| Never coded | 1.5–2 hours | ~30 hours |
| Some technical background (PM, analyst, etc.) | 1–1.5 hours | ~20 hours |
| Engineer | 30–60 minutes | ~12 hours |

The course is calibrated for the middle. EAs will spend more time on Day 4 (setup) and Day 6 (CRUD). Engineers will skim much of Days 1–3 (concept). Everyone arrives at Day 18 around the same time.

If you fall behind, that's fine. The course is milestone-based, not calendar-based. Catch up. You're allowed to skip the weekend if you need to.

If you paused for a while, use [I Fell Behind](./recover.md) to find your last verified day and resume.

---

## 3. What if I get stuck on a day and can't move forward?

Three escalation steps:

1. **Read the day's troubleshooting table** (bottom of every `build.md`). Most problems are listed there.
2. **Say `day done` to your coding harness.** It reads the completion gate for that day and tells you specifically what's missing.
3. **Ask for help in the channel you have access to.** If you're in a cohort, ask in the cohort community. If you're self-serve, open a GitHub issue and tag the day number.

If your local machine is the blocker, switch to **Codespaces** ([see the browser setup path](./codespaces.md)). Most setup problems are local-environment-related. Codespaces eliminates them.

---

## 4. What tool do I use for the course?

For this version of the course, use your favorite coding harness.

The repo contains `AGENTS.md`, `course-manifest.json`, and portable OneMillion agents. Claude Code, Cursor, Codex, Gemini, Antigravity, Copilot, and similar tools can read those files and become your course orchestrator.

```text
/idea → /spec → /design → /plan → /build → /test → /guard → /ship → /sell
```

If your harness supports native slash commands or subagents, use them. If not, tell it to read `AGENTS.md` and emulate the mapped agent for the day.

---

## 4.5 What if I fall behind?

You'll fall behind. Everyone does. Real life happens. The course is designed for it.

**There's no shame, no streak, no badge taken away if you skip a day or a week.** The 18 days are units of progress, not calendar days. Builder #N gets earned when you finish, not by when you finish.

Many builders take 30 or 60 calendar days to complete the 18 days of work. Some take 90 days. They all graduate. You will too.

The only failure mode is not coming back. If life pulls you away, just come back when it lets you. We're not Duolingo. The course waits.

When you come back, use [I Fell Behind](./recover.md). It gives you one harness-neutral prompt to find your current state and restart.

## 5. Can I skip days or do them out of order?

Not really. Each day depends on the previous one. Day 4 needs Day 3's PRD. Day 7 needs Day 6's working app. The verification system enforces this — you can't get Builder #N if you skipped days.

You **can** take more than one calendar day per "day" if you need to. Spread Day 4 over a weekend. Take a week off. Come back. The 18 days are *units of progress*, not literal calendar days.

---

## 6. What if my product idea is bad?

You'll find out on Day 2 (the Mom Test conversations) and Day 3 (the PRD). By then you can pivot. Many builders change their idea between Day 1 and Day 4 — that's expected, not failure.

**Common pivots:**
- "Too big" → narrow scope to one user, one feature
- "Already exists" → focus on the niche existing tools ignore
- "I don't actually need this" → pick a problem you *do* feel personally

After Day 3 your PRD is locked. Don't pivot after that — finish what you started, learn the skill, then build the next product.

---

## 7. What if I break something during the build?

Welcome to engineering. This is normal.

Your code lives in a Git repo. Every change is reversible. The course shows you how to commit at safe checkpoints. If something breaks badly, first ask your coding harness to inspect your Git history:

```bash
git status
git log --oneline -5
```

Paste that output into your coding harness and ask for the safest recovery plan. Do not run destructive Git commands until you understand which files will change.

If things really go sideways, you can delete the project and start over. You'll lose your code, not your skill.

---

## 8. Will my product actually work, or is it a toy?

It will actually work.

By Day 18 your product should have:
- Real authentication (signup, login, password reset)
- A real database (Supabase Postgres, not localStorage)
- A real AI feature (calling Claude with streaming, tool use, and your user's data)
- Production monitoring (Sentry catches errors, Vercel Analytics tracks usage)
- A live Vercel URL, with an optional custom domain if you choose to add one
- Real outreach and feedback captured from at least one target user conversation or product trial

It is not a toy tutorial. It is a real product foundation. You can keep building on it after Day 18, ship features, get more users, charge money if you want. It's yours.

---

## 9. What if I'm not in a cohort?

Self-serve works fine. The entire course content and portable agent flow are in this repo. You'll miss the cohort layer:

1. **Live Saturday sessions** — available during live cohorts.
2. **Cohort community** — available to cohort members.
3. **Mentor support** — available when a cohort is actively running.

Self-serve completion is harder because there is less accountability. If you go self-serve, use Day 0 publicly and post progress every few days so other people know you're still building.

---

## 10. How does Builder #N actually work?

When you complete Day 18 and pass all verification checks, you have a verified local submission. Sid or the Builder Wall review process then issues the next sequential Builder number. It's:

- **Permanent.** Yours forever. No re-certification.
- **Sequential.** Builder #47 was the 47th person to graduate. Builder #500 was the 500th.
- **Public.** Listed in the Builder Wall once your submission is accepted.
- **Linked.** Your profile shows your deployed product, 18-day commit history, demo Loom.
- **Shareable.** A LinkedIn badge image links back to your verified profile.

The first 100 accepted builders ever get **Founding Builder** status — same number, additional permanent badge, plus Sid's personal Slack DM access and an intro to one investor or hiring manager on graduation.

---

## 11. What if Anthropic / Vercel / Supabase changes pricing?

Then we update the course. The agentic SDLC framework is stable — the tools may shift.

If a service we recommend becomes too expensive or shuts down, we'll publish migration guides and update the course content. The Builder Wall is permanent regardless.

(For what it's worth: Anthropic, Vercel, Supabase, and GitHub all have free tiers that have been generous and stable for years. We don't expect issues.)

---

## 12. What happens on Day 19?

Whatever you want.

Common paths:
- **Keep building.** Add features, polish, market it, monetize if you can.
- **Build another product.** You have the skill now. Pick another idea, ship in 5 days, then 3 days, then 1.
- **Become a Ship Captain.** Help run the next cohort. Get paid in OneMillion equity-of-mission (and Sid's gratitude).
- **Teach what you learned.** Many alumni become AI-builder consultants, charging $200–500/hr to help companies adopt the same patterns.
- **Just exist with the skill.** Use it when you need it. The skill doesn't expire.

Builder #N is the credential. What you do with it is up to you.

---

→ **More:** [Manifesto](../../MANIFESTO.md) · [Getting Started](./getting-started.md) · [Agent-Led Learning Flow](./agent-flow.md) · [Day 1](../day-01-idea/learn.md)
