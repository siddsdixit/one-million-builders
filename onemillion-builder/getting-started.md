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

---

## The First Prompt

Paste this into your harness:

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

---

## If Your Harness Needs Local Files

Clone the repo:

```bash
git clone https://github.com/siddsdixit/teach-one-million.git
cd teach-one-million
```

Open the folder in your coding harness.

Then say:

```text
Read AGENTS.md and start Day 1.
```

---

## Optional Native Adapter Install

From inside the cloned repo:

```bash
./onemillion-builder/install-agents.sh
```

This installs local adapter files:

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
onemillion-builder/course-manifest.json
onemillion-agents/
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

→ [Day 0 — Public Commitment](day-0-commit/README.md)<br>
→ [Day 1 — Vision + Mental Map](week-1-foundation/day-01-vision/learn.md)
