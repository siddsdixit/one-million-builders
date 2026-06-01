# Codex

Open Codex from the cloned repo:

```bash
cd one-million-builders
codex
```

Then say:

```text
I am starting the OneMillion course. Read AGENTS.md, course/course-manifest.json, course/docs/teaching-protocol.md, and course/days/single.md. Start Day 0. First verify fork, clone, origin, and upstream. Properly greet me, explain the course, explain the OneMillion development pipeline, provide copy-ready actions, and define what done means.
```

Codex should use `AGENTS.md` as the bootstrap, then read the course manifest, full course flow, and orchestrator agent.

Codex does not need a separate generated adapter. The installer still verifies the fork/clone setup and prepares shared local state, but Codex reads the root `AGENTS.md` directly.
