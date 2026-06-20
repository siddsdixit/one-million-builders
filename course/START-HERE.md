# Start Here

If you only remember one thing: **open the course in your fork, ask your coding harness to become the OneMillion learning orchestrator, then follow one day at a time.**

The learner path is intentionally small:

```text
START-HERE.md -> current day README.md -> build.md -> stuck.md if needed -> day done
```

Everything else in the repo supports that loop.

Use the coding harness you already like: Claude Code, Cursor, Codex, Gemini, Antigravity, Copilot, or another tool that can read a GitHub repo and work in files.

The simplest start is to paste this into your harness:

```text
I am taking the OneMillion course at:
https://github.com/siddsdixit/one-million-builders/tree/main/course
```

The harness should take over from there: greet you, explain the course, help you create GitHub if needed, guide fork/clone/install, then start Day 0.

The course is designed around a universal bootstrap file:

```text
AGENTS.md
```

That file tells your harness how to become your OneMillion learning orchestrator. The day-by-day map lives in `course-manifest.json`. The full narrative course flow lives in [single.md](days/single.md).

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
one-million-builders/
  course/
    README.md              # learner landing page
    course/                # Day 0-18 lessons and full flow
    agents/                # agent definitions and skills
    docs/                  # setup, harness, verification, examples
    tools/                 # local QA/simulation utilities
  my-onemillion-build/     # your product app, created on Day 1
  .onemillion/             # course state, created by the installer
```

Keep `my-onemillion-build` at the repo root unless your harness deliberately updates `.onemillion/state.json`. This lets the orchestrator, daily verifiers, and your product code stay in one forked workspace.

---

## Mandatory Preflight

Before Day 1:

1. Star `siddsdixit/one-million-builders`.
2. Fork `siddsdixit/one-million-builders` into your own GitHub account.
3. Clone **your fork**.

```bash
git clone https://github.com/YOUR-USERNAME/one-million-builders.git
cd one-million-builders
```

Your fork is your public course workspace. It proves your progress and gives your coding harness a real repo to work in.

---

## Start Prompt

Paste this into your favorite coding harness:

```text
I am starting the OneMillion course from my fork.

Course page:
https://github.com/siddsdixit/one-million-builders/tree/main/course

Read AGENTS.md and course/course-manifest.json.
Read course/docs/teaching-protocol.md.
Read course/days/single.md.
Become my OneMillion learning orchestrator.
First verify I starred, forked, and cloned the repo.
Then start Day 0. Do not start Day 1 until Day 0 passes.
Teach me one day at a time. Properly greet me, explain the course, explain the AI/human contract, introduce each day, provide copy-ready actions, and define what done means.
When I say "day done", verify the day and advance me.
Do not skip the learning or do the external tool steps for me.
```

If your harness cannot read GitHub links reliably, open your cloned fork locally and paste the same prompt.

## Daily Loop

Every day follows the same rhythm:

1. Open the current day `README.md`.
2. Read the outcome and decisions.
3. Ask your harness to teach the day.
4. Follow `build.md` one step at a time.
5. Use `stuck.md` if anything breaks or feels unclear.
6. Ask the harness to verify the completion gate.
7. Say `day done` only after the gate is true.
8. Commit meaningful progress.

This loop is more important than speed. Do not skip the review or done checklist.

---

## Preflight Installer

Run the installer from the forked clone before Day 0 is marked done. It enforces the fork-first preflight, creates the course state files, and installs local OneMillion harness adapters.

From the cloned repo:

```bash
./course/install-agents.sh
```

If GitHub CLI is installed and authenticated, this will star the upstream repo, create or verify your fork, set `origin` to your fork, set `upstream` to Sid's repo, create `.onemillion/state.json`, write `.onemillion/tooling-preflight.md`, and add local adapters for Claude Code, Codex, OpenCode, Cursor, Antigravity, Gemini CLI, and GitHub Copilot.

If GitHub CLI is not available, do the fork/star steps in the browser and set remotes manually, then rerun the installer. A generic harness can still follow `AGENTS.md`, but Day 0 should not be marked done until the installer has created the state/tooling files or the harness has explicitly repaired them from the manifest.

---

## What Happens Next

The orchestrator starts Day 0 with GitHub fork verification and the commitment. After Day 0 passes, it starts Day 1 with the Idea agent and teaches how to turn a raw idea into a first PRD.

You will:

- learn what the OneMillion development pipeline is and why the flow is spec-first
- learn what each OneMillion agent does
- learn what makes a good idea
- choose a specific user
- name a painful moment
- identify data sources, user stories, success criteria, and KPIs
- review a first PRD draft
- keep the first MVP to exactly 3 core jobs so you can finish
- create your first `.onemillion/` artifacts
- stop only when Day 1 is actually complete

You are not here to watch an AI build alone. You are here to learn how to direct agents.
