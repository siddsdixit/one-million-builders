# Getting Started

OneMillion runs inside your coding harness.

You can use:

- Claude Code
- Cursor
- Codex
- Gemini
- Antigravity
- GitHub Copilot / VS Code
- another agentic coding tool that can read files and edit a workspace

The course repo contains the instructions, agents, manifest, examples, and daily lessons. Your harness becomes the teacher by reading them.

When a step asks for an external account, API key, dashboard setting, permission, or public link, open [Account Setup Playbook](account-setup.md). It gives the exact provider link and the QA check for that setup.

Start from the rendered course page:

```text
https://github.com/siddsdixit/one-million-builders/tree/main/course
```

---

## Mandatory GitHub Preflight

You must do these before Day 0 or Day 1:

1. Star `siddsdixit/one-million-builders`.
2. Fork `siddsdixit/one-million-builders`.
3. Clone your fork.

```bash
git clone https://github.com/YOUR-USERNAME/one-million-builders.git
cd one-million-builders
./course/install-agents.sh
```

Open your fork in your coding harness. If the repo is a downloaded zip, a loose folder, or Sid's upstream clone, the harness should stop and fix the setup before teaching.

The course and your product stay together:

```text
one-million-builders/
  course/      # course
  course/agents/       # agents
  my-onemillion-build/     # your app
```

Day 1 creates `my-onemillion-build` inside the cloned course repo. Day 4 turns that folder into the real Next.js app. Do not create it in `~/` unless your harness also updates `.onemillion/state.json` and the verifier commands.

---

## The First Prompt

Paste this into your harness:

```text
I am starting the OneMillion course from my fork.

Course page:
https://github.com/siddsdixit/one-million-builders/tree/main/course

Read AGENTS.md and course/course-manifest.json.
Read course/docs/teaching-protocol.md.
Read course/days/single.md.
Become my OneMillion learning orchestrator.
First enforce the Preflight Gate. If anything is wrong with clone/fork/origin/upstream setup, stop and fix it before Day 0.
Then start Day 0. Do not start Day 1 until Day 0 passes.
Teach me one day at a time. Properly greet me, explain the course, explain the AI/human contract, introduce each day, provide copy-ready actions, and define what done means.
When I say "day done", verify the day and advance me.
Do not skip the learning or do the external tool steps for me.
```

---

## Optional Native Adapter Install

From inside the cloned repo:

```bash
./course/install-agents.sh
```

If GitHub CLI is installed and authenticated, the installer stars the upstream repo, creates or verifies your fork, sets `origin` to your fork, sets `upstream` to Sid's repo, and starts local course state. It also installs local adapter files:

```text
.claude/agents/
.claude/commands/
.cursor/rules/
.agents/rules/
.gemini/GEMINI.md
.github/copilot-instructions.md
```

The universal source remains:

```text
AGENTS.md
course/course-manifest.json
course/days/single.md
course/agents/
```

---

## What You Still Learn Hands-On

The harness does not replace the work.

You will still learn and touch:

- GitHub for source control
- Vercel for deployment
- Supabase for auth, database, and Row Level Security
- AI API/server routes for your product feature
- monitoring tools
- Loom for Demo Day
- outreach and user feedback

The agent teaches and guides. You make decisions and do the real external-tool steps.

---

## Harness-Specific Guides

- [Claude Code](harnesses/claude-code.md)
- [Cursor](harnesses/cursor.md)
- [Codex](harnesses/codex.md)
- [Gemini](harnesses/gemini.md)
- [Antigravity](harnesses/antigravity.md)
- [GitHub Copilot](harnesses/copilot.md)

---

## Next

→ [Day 0 — Orientation + Commitment + GitHub Workspace](../days/day-00-orientation/README.md)<br>
→ [Day 1 — Idea Agent + PRD Draft](../days/day-01-idea/learn.md)
