# Week 2 — Make It AI

<p align="center">
  <a href="../README.md">Course Home</a> &bull;
  <a href="../week-1-foundation/README.md">Previous Week</a> &bull;
  <a href="../week-3-ship-and-sell/README.md">Next Week</a> &bull;
  <a href="../docs/recover.md">Recover</a>
</p>

**Outcome by end of Week 2:** Your Week 1 app now has a real AI feature — streaming, tool-using, personalized to user data. Your product is AI-native, not AI-decorative.

This is where OneMillion stops being "yet another web app course" and becomes the real thing. By end of Week 2 your users are interacting with Claude inside your product, getting real answers grounded in their real data.

---

## The Six Days

| Day | Title | What you ship | Time |
|-----|-------|---------------|------|
| **7** | [What Is An AI Feature](./day-07-ai-spec/learn.md) | An AI feature spec + product type confirmation | 30–60 min |
| **8** | [First AI Call + Prompt Design](./day-08-first-ai-call/learn.md) | Your first real Claude call producing real output | 1–2 hr |
| **9** | [Streaming UI](./day-09-streaming/learn.md) | AI text appearing live, token-by-token, in your UI | 45–90 min |
| **10** | [Tool Use](./day-10-tool-use/learn.md) | AI that can read AND write to your database | 1–2.5 hr |
| **11** | [RAG (Retrieval)](./day-11-rag/learn.md) | AI that answers using YOUR user's data, not generic | 1–2 hr |
| **12** | [Lock The AI Feature](./day-12-lock-the-ai/learn.md) | AI feature locked with acceptance criteria + cost budget | 45–90 min |

---

## Agent Modes This Week

Use the portable OneMillion agents based on the work:

```text
/build → /test → /debug → /refactor
```

Build implements the AI feature. Test verifies behavior. Debug fixes broken flows. Refactor keeps the implementation clean without changing behavior.

---

## The 5 Pillars This Week

| Pillar | Where it shows up |
|--------|------------------|
| **Spec before code** | Day 7 (AI feature spec), Day 12 (acceptance criteria) |
| **Multi-agent decomposition** | Day 10 (each tool is a small, focused agent capability) |
| **Validation gates** | End of every day + Day 12 (lock criteria) |
| **Production hygiene** | Day 8 (API key never in client code), Day 11 (RAG with RLS) |
| **Human review loop** | Every day: "What to spot-check in what Claude generated" |

---

## What You Need Before Week 2

- ✅ Week 1 complete — working web app deployed with auth + CRUD
- ✅ Your coding harness can read `AGENTS.md` and edit your product workspace
- ✅ Your Week 1 product is in a state where adding AI fits the PRD

---

## When You're Done With Week 2

You are ready for Week 3 if:
- An AI feature in your app that does something real for your user
- A streaming UI (text appears as it's generated, not all at once)
- The AI can take at least one action via tools (e.g., write to your DB)
- The AI's answers are grounded in your user's actual data (RAG)
- A `ai-acceptance-criteria.md` file with measurable quality checks
- All 12 days verified ✅

Then Week 3 takes it to production: hardening, custom domain, monitoring, landing page, real users.

→ **Start:** [Day 7 — What Is An AI Feature](./day-07-ai-spec/learn.md)
