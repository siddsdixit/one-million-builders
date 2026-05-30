# Week 1 — Foundation

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
  <a href="../START-HERE.md">Start Here</a> &bull;
  <a href="../week-2-make-it-ai/README.md">Next Week</a> &bull;
  <a href="../recover.md">Recover</a>
</p>

**Outcome by end of Week 1:** A real web app deployed at your own URL with working signup/login and your core feature live.

No AI yet. That's Week 2. Week 1 is about getting the bones in place — auth, database, deployment, and one feature working end to end. Once these are solid, adding AI is fast.

---

## Agent Modes This Week

Use the portable OneMillion agents in this order:

```text
/idea → /spec → /design → /plan → /build
```

Week 1 is where your harness uses those agents to create your first `.onemillion/` artifacts, lock scope, design the product shape, and start the app.

---

## The Six Days

| Day | Title | What you ship | Time |
|-----|-------|---------------|------|
| **1** | [Vision + Mental Map](./day-01-vision/learn.md) | Picked product type + idea | 30–60 min |
| **2** | [Problem + Mom Test](./day-02-problem/learn.md) | 3 real problems from real conversations | 45–75 min |
| **3** | [Write Your PRD](./day-03-prd/learn.md) | Locked PRD with 5 sections | 45–90 min |
| **4** | [Stack + First Deploy](./day-04-stack/learn.md) | Hello-world live at yourapp.vercel.app | 1–2.5 hr |
| **5** | [Auth + Database](./day-05-auth/learn.md) | Signup → login → logout working | 1–2.5 hr |
| **6** | [Core Feature](./day-06-core-feature/learn.md) | Your main feature working live | 1.5–3 hr |

---

## The Five Pillars Show Up Here

| Pillar | Where this week |
|--------|----------------|
| **Spec before code** | Days 1–3 (you build nothing until your spec is locked) |
| **Multi-agent decomposition** | Day 6 (the Data → API → UI pattern is three separate agent calls) |
| **Validation gates** | End of every day (the "What Should Be True" checklist + the AI verifier) |
| **Production hygiene from day 1** | Day 5 (RLS on every table, secrets in `.env` not git) |
| **Human review loop** | Every day's "What to spot-check" section |

---

## What You Need Before Starting

- ✅ A coding harness ready to read `AGENTS.md` ([getting-started.md](../getting-started.md))
- ✅ GitHub, Supabase, Vercel accounts (signed up, no setup yet)
- ✅ ~10 hours of total time over the next 6 days

---

## What If Week 1 Takes Longer Than 6 Calendar Days?

Fine. Milestone-based, not calendar-based. Day 4 (stack setup) is the longest day for non-engineers — give it a weekend if you need it. The verification system only cares that each day's "What Should Be True" checklist passes. It doesn't care when.

Most builders finish Week 1 in 6–10 days. Engineers finish in 4–6 days.

---

## When You're Done With Week 1

You are ready for Week 2 if:
- A live URL where strangers can sign up and use your app
- A GitHub repo with 6+ commits, one per day minimum
- A core feature that works end-to-end (create, read, update, delete on your main entity)
- Row Level Security enabled on your database
- A locked PRD that hasn't been changed since Day 3
- Days 1-6 are verified

Then you move on to **Week 2: Make It AI** — adding real AI features to the app you just built.

→ **Start:** [Day 1 — Vision + Mental Map](./day-01-vision/learn.md)
