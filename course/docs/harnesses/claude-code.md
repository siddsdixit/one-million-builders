# Claude Code

## Fast Path

Open Claude Code in the cloned repo and say:

```text
/onemillion
```

If the command is unavailable, say:

```text
Read AGENTS.md, course/course-manifest.json, course/docs/teaching-protocol.md, and course/days/single.md. Become my OneMillion learning orchestrator. Start Day 0. First verify fork, clone, origin, and upstream. Properly greet me, explain the course, explain the OneMillion development pipeline, provide copy-ready actions, and define what done means.
```

## Optional Native Install

```bash
./course/install-agents.sh
```

This copies portable agents into `.claude/agents/`, shared skills into `.claude/skills/`, and adds a local `/onemillion` command at `.claude/commands/onemillion.md`.
