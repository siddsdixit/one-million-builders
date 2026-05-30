# Start Here

Use the coding harness you already like: Claude Code, Cursor, Codex, Gemini, Antigravity, Copilot, or another tool that can read a GitHub repo and work in files.

This page assumes you start from the canonical course page:

```text
https://github.com/siddsdixit/teach-one-million/tree/main/onemillion-builder
```

The course is designed around a universal bootstrap file:

```text
AGENTS.md
```

That file tells your harness how to become your OneMillion learning orchestrator. The day-by-day map lives in `course-manifest.json`.

When a day asks you to create an account, create a key, set permissions, or verify a dashboard, use [Account Setup Playbook](docs/account-setup.md). It gives exact links and QA checks.

The first rule is the Preflight Gate: the course must run from your forked git clone with `origin` pointing to your fork and `upstream` pointing to Sid's repo.

Tiny Git glossary:

| Word | Meaning |
|---|---|
| **Fork** | Your copy of Sid's repo on GitHub. |
| **Clone** | The copy of your fork on your laptop. |
| **Origin** | The Git remote that points to your fork. |
| **Upstream** | The Git remote that points back to Sid's original repo. |
| **Downstream** | Your fork/local work receiving course updates from upstream. |

Your product workspace lives inside that cloned course repo:

```text
teach-one-million/
  onemillion-builder/      # course lessons, verifiers, harness instructions
  onemillion-agents/       # agent definitions the harness uses to teach
  my-onemillion-build/     # your product app, created on Day 1
  .onemillion/             # course state, created by the installer
```

Keep `my-onemillion-build` at the repo root unless your harness deliberately updates `.onemillion/state.json`. This lets the orchestrator, daily verifiers, and your product code stay in one forked workspace.

---

## Mandatory Preflight

Before Day 1:

1. Star `siddsdixit/teach-one-million`.
2. Fork `siddsdixit/teach-one-million` into your own GitHub account.
3. Clone **your fork**.

```bash
git clone https://github.com/YOUR-USERNAME/teach-one-million.git
cd teach-one-million
```

Your fork is your public course workspace. It proves your progress and gives your coding harness a real repo to work in.

---

## Start Prompt

Paste this into your favorite coding harness:

```text
I am starting the OneMillion course from my fork.

Course page:
https://github.com/siddsdixit/teach-one-million/tree/main/onemillion-builder

Read AGENTS.md and onemillion-builder/course-manifest.json.
Become my OneMillion learning orchestrator.
First verify I starred, forked, and cloned the repo.
Then start Day 0 and Day 1.
Teach me one day at a time.
When I say "day done", verify the day and advance me.
Do not skip the learning or do the external tool steps for me.
```

If your harness cannot read GitHub links reliably, open your cloned fork locally and paste the same prompt.

---

## Optional Native Adapter Install

Some harnesses work better when their native rules/agents are installed locally. The installer also enforces the fork-first preflight.

From the cloned repo:

```bash
./onemillion-builder/install-agents.sh
```

If GitHub CLI is installed and authenticated, this will star the upstream repo, create or verify your fork, set `origin` to your fork, set `upstream` to Sid's repo, create `.onemillion/state.json`, and add local adapters for Claude Code, Cursor, Antigravity, Gemini, and GitHub Copilot.

If GitHub CLI is not available, the installer stops until your git remotes are correct. You do not need native adapters if your harness is already following `AGENTS.md`, but the clone/fork/upstream preflight is still mandatory.

---

## What Happens Next

The orchestrator starts Day 1 with the Idea agent.

You will:

- compare possible ideas
- choose a specific user
- name a painful moment
- keep the first MVP to exactly 3 core jobs so you can finish
- create your first `.onemillion/` artifacts
- stop only when Day 1 is actually complete

You are not here to watch an AI build alone. You are here to learn how to direct agents.
