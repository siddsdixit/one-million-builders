# Week 3 — Ship & Sell

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
  <a href="../week-2-make-it-ai/README.md">Previous Week</a> &bull;
  <a href="../docs/verification/README.md">Verification</a> &bull;
  <a href="../../builders/README.md">Builder Wall</a>
</p>

**Outcome by end of Week 3:** A launch-ready product with monitoring, a landing page, real outreach, captured feedback, and a Day 18 Builder Claim submission.

This is the week that turns your AI-native app from "thing on Vercel.app" to "actual product." Same code base. Same features. Different posture.

---

## The Six Days

| Day | Title | What you ship | Time |
|-----|-------|---------------|------|
| **13** | [Production Hygiene](./day-13-hygiene/learn.md) | Audit-passed app — secrets, RLS, rate limits, errors | 1-2 hr |
| **14** | [Custom Domain](./day-14-domain/learn.md) | Optional custom domain with SSL, or a documented decision to stay on Vercel | 30-60 min |
| **15** | [Monitoring](./day-15-monitoring/learn.md) | Sentry + Vercel Analytics + UptimeRobot active | 30-60 min |
| **16** | [Landing Page](./day-16-landing/learn.md) | Real landing page at root URL | 1-2 hr |
| **17** | [First 10 Users](./day-17-first-users/learn.md) | Outreach sent + real feedback captured | 45-90 min |
| **18** | [Demo Day → Builder #N](./day-18-demo/learn.md) | 5-min Loom + verification + Builder Claim submission | 30-60 min |

---

## Agent Modes This Week

Use the portable OneMillion agents in this order:

```text
/guard → /ship → /sell
```

Guard checks production risk. Ship deploys the product. Sell turns the finished build into a launch page, outreach, and feedback loop.

---

## The 5 Pillars This Week

| Pillar | Where it shows up |
|--------|------------------|
| **Spec before code** | Day 16 (landing page is a spec for what your product is) |
| **Multi-agent decomposition** | Day 15 (monitoring = 3 separate small concerns) |
| **Validation gates** | Day 13 (audit gate), Day 18 (final verification → Builder Claim) |
| **Production hygiene** | This entire week is Pillar 4 |
| **Human review loop** | Day 17 (real user feedback — humans review YOUR product) |

---

## What You Need Before Week 3

- ✅ Week 1 + Week 2 complete and verified
- ✅ A working AI feature you'd be willing to show your toughest friend
- ✅ ~$10-15 budget if you want a custom domain (optional but recommended)
- ✅ One person in mind who would actually use your product

---

## When You're Done With Week 3

You are ready to submit your Builder Claim if:
- Your product live at `yourapp.com` (or staying on .vercel.app — still counts)
- Sentry catching errors before users complain about them
- Analytics showing real visits (even if just yours, your friends, and one user)
- A landing page that explains what + for whom + a clear CTA
- Outreach sent and at least one piece of real target-user feedback captured
- A 5-minute Demo Day Loom
- Day 18 final verification passed locally
- Builder Claim issue submitted for review

Then you're done with the course work. Once your claim is accepted, Builder #N is permanent, sequential, and public.

→ **Start:** [Day 13 — Production Hygiene](./day-13-hygiene/learn.md)
