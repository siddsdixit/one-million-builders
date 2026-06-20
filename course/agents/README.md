# OneMillion Agents

Portable agent instructions for the OneMillion builder course.

These files are the source that any coding harness can read:

- Claude Code can use copied agents and skills in `.claude/`.
- Cursor can read them through `AGENTS.md` or generated `.cursor/rules/`.
- Codex can read `AGENTS.md`, project custom agents in `.codex/agents/`, and skills in `.agents/skills/`.
- OpenCode can read `AGENTS.md`, project agents in `.opencode/agents/`, and skills in `.opencode/skills/`.
- Gemini CLI can read `.gemini/GEMINI.md` and `.gemini/settings.json`, which point back to this library.
- Antigravity can use the generated plugin/rule files that copy this library.

The course does not depend on a login or one hosted extension for the first version. The reliable path is:

```text
clone repo → run ./course/install-agents.sh → open in favorite coding harness → start Day 0
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
