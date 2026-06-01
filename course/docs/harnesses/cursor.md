# Cursor

Open the cloned repo in Cursor.

Run the installer first:

```bash
./course/install-agents.sh
```

Cursor should then read `AGENTS.md` and `.cursor/rules/onemillion-course.mdc`.

Start with:

```text
I am starting the OneMillion course. Read AGENTS.md, course/course-manifest.json, course/docs/teaching-protocol.md, and course/days/single.md. Start Day 0. First verify fork, clone, origin, and upstream. Properly greet me, explain the course, explain the OneMillion development pipeline, provide copy-ready actions, and define what done means.
```

If Cursor does not pick up the rule, mention these files explicitly:

```text
Read AGENTS.md, course/course-manifest.json, course/docs/teaching-protocol.md, course/days/single.md, and course/agents/agents/orchestrator.md.
```
