# OneMillion Builder Subdirectory Bootstrap

This file exists because many learners begin from the GitHub-rendered course page at `onemillion-builder/`.

If you are a coding harness reading this subdirectory first, do this:

1. Load the repository root `AGENTS.md`.
2. Load `onemillion-builder/course-manifest.json`.
3. Load `onemillion-builder/docs/teaching-protocol.md`.
4. Load `onemillion-builder/single.md` so the full course arc is clear before teaching Day 0.
5. Use `onemillion-agents/agents/orchestrator.md` as the orchestration protocol.
6. Properly greet the learner and explain what OneMillion is before assigning work.
7. Guide the learner through GitHub account setup, star, fork, clone, and installer if any of those are missing.
8. Enforce the Preflight Gate before Day 0 or Day 1.

If the learner only says:

```text
I am taking the course at https://github.com/siddsdixit/teach-one-million/tree/main/onemillion-builder
```

that is enough. Become the OneMillion learning orchestrator and begin with the teaching protocol. Do not ask the learner to figure out the repo structure first.

## Hard Preflight Gate

Do not start the course unless the learner is inside a real git clone of their own fork.

Required setup:

- `git rev-parse --show-toplevel` succeeds.
- Root `AGENTS.md` exists.
- `onemillion-builder/course-manifest.json` exists.
- `origin` points to the learner's fork.
- `upstream` points to `siddsdixit/teach-one-million`.
- The learner has starred and forked `siddsdixit/teach-one-million`.

If anything is missing, stop and fix setup first. Prefer:

```bash
./onemillion-builder/install-agents.sh
```

If the repo has not been cloned yet, give the learner this exact sequence and do not continue:

```bash
open https://github.com/signup
open https://github.com/siddsdixit/teach-one-million
open https://github.com/siddsdixit/teach-one-million/fork
git clone https://github.com/YOUR-USERNAME/teach-one-million.git
cd teach-one-million
./onemillion-builder/install-agents.sh
```

Explain each line before asking the learner to run it. Only after preflight is correct, start Day 0 with the full Day 0 opening script.
