# Start Here

Use the coding harness you already like: Claude Code, Cursor, Codex, Gemini, Antigravity, Copilot, or another tool that can read a GitHub repo and work in files.

The course is designed around a universal bootstrap file:

```text
AGENTS.md
```

That file tells your harness how to become your OneMillion learning orchestrator. The day-by-day map lives in `course-manifest.json`.

---

## Fast Path

Paste this into your favorite coding harness:

```text
I am starting the OneMillion course.

Course repo:
https://github.com/siddsdixit/teach-one-million

Read AGENTS.md and the course manifest.
Become my OneMillion learning orchestrator.
Start me at Day 1.
Teach me one day at a time.
When I say "day done", verify the day and advance me.
Do not skip the learning or do the external tool steps for me.
```

If your harness can read GitHub links reliably, it will guide you from there.

---

## Reliable Path

If the fast path feels vague or your harness cannot read the link well, clone the repo:

```bash
git clone https://github.com/siddsdixit/teach-one-million.git
cd teach-one-million
```

Open that folder in your coding harness.

Then say:

```text
Read AGENTS.md and start the OneMillion course.
```

---

## Optional Native Adapter Install

Some harnesses work better when their native rules/agents are installed locally.

From the cloned repo:

```bash
./onemillion-builder/install-agents.sh
```

This adds local adapters for Claude Code, Cursor, Antigravity, Gemini, and GitHub Copilot.

You do not need this if your harness is already following `AGENTS.md`.

---

## What Happens Next

The orchestrator starts Day 1 with the Idea agent.

You will:

- compare possible ideas
- choose a specific user
- name a painful moment
- create your first `.onemillion/` artifacts
- stop only when Day 1 is actually complete

You are not here to watch an AI build alone. You are here to learn how to direct agents.
