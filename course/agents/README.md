# OneMillion Agents

Portable agent instructions for the OneMillion builder course.

These files are the source that any coding harness can read:

- Claude Code can use them directly or copy them into `.claude/agents/`.
- Cursor can read them through `AGENTS.md` or generated `.cursor/rules/`.
- Codex can read `AGENTS.md` and these agent files.
- Gemini and Antigravity can use harness-specific rule files that point back here.

The course does not depend on a login or one hosted extension for the first version. The reliable path is:

```text
clone repo → open in favorite coding harness → ask it to read AGENTS.md → start Day 1
```

## Core Flow

```text
idea → spec → design → plan → build → test → guard → ship → sell
```

Utility agents:

```text
ask · debug · refactor · review · research · revise · orchestrator
```

## Important Files

- `agents/orchestrator.md` — course-specific teacher protocol.
- `agents/*.md` — phase agents imported from the OneMillion plugin source.
- `skills/*/SKILL.md` — support references used by the agents.

Source imported from:

```text
/Users/siddsdixit/Documents/omc/Plugin/source
```

