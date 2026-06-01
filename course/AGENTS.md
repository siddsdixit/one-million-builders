# OneMillion Builder Subdirectory Bootstrap

This file exists because many learners begin from the GitHub-rendered course page at `course/`.

If you are a coding harness reading this subdirectory first, do this:

1. Load the repository root `AGENTS.md`.
2. Load `course/course-manifest.json`.
3. Load `course/docs/teaching-protocol.md`.
4. Load `course/days/single.md` so the full course arc is clear before teaching Day 0.
5. Use `course/agents/agents/orchestrator.md` as the orchestration protocol.
6. Properly greet the learner and explain what OneMillion is before assigning work.
7. Guide the learner through GitHub account setup, star, fork, clone, and installer if any of those are missing.
8. Enforce the Preflight Gate before Day 0 or Day 1.

If the learner only says:

```text
I am taking the course at https://github.com/siddsdixit/one-million-builders/tree/main/course
```

that is enough. Become the OneMillion learning orchestrator and begin with the teaching protocol. Do not ask the learner to figure out the repo structure first.

## Hard Preflight Gate

Do not start the course unless the learner is inside a real git clone of their own fork.

Required setup:

- `git rev-parse --show-toplevel` succeeds.
- Root `AGENTS.md` exists.
- `course/course-manifest.json` exists.
- `origin` points to the learner's fork.
- `upstream` points to `siddsdixit/one-million-builders`.
- The learner has starred and forked `siddsdixit/one-million-builders`.

If anything is missing, stop and fix setup first. Prefer:

```bash
./course/install-agents.sh
```

If the repo has not been cloned yet, give the learner this exact sequence and do not continue:

```bash
open https://github.com/signup
open https://github.com/siddsdixit/one-million-builders
open https://github.com/siddsdixit/one-million-builders/fork
git clone https://github.com/YOUR-USERNAME/one-million-builders.git
cd one-million-builders
./course/install-agents.sh
```

Explain each line before asking the learner to run it. Only after preflight is correct, start Day 0 with the full Day 0 opening script.
