# OneMillion Plugin

**Optional native extension path for the OneMillion agent system.**

The course does not depend on the plugin for the first local learning flow. The primary course architecture is harness-neutral:

```text
AGENTS.md + course-manifest.json + onemillion-agents/
```

That lets learners start in Claude Code, Cursor, Codex, Gemini, Antigravity, Copilot, or another coding harness.

The plugin remains the future first-class product experience: native modes, cloud sync, account features, and packaged extension delivery.

---

## Current Course Path

```text
Paste GitHub link or clone repo
→ harness reads AGENTS.md
→ harness becomes OneMillion learning orchestrator
→ learner progresses one day at a time
```

No OneMillion login is required for this local path.

---

## Plugin Path

The native plugin gives builders guided modes:

```text
idea → spec → design → plan → build → test → guard → ship → sell
```

Utility modes:

```text
ask · debug · refactor · orchestrator · research · review · revise
```

---

## Where The Real Source Lives

Local source of truth on Sid's machine:

```text
/Users/siddsdixit/Documents/omc/Plugin
```

Important folders there:

```text
source/agents/          # canonical agent prompts
source/skills/          # canonical skill references
platforms/claude-code/  # generated Claude Code plugin output
platforms/cursor/       # generated Cursor rules output
platforms/roo-code/     # generated Roo Code modes/skills output
```

Docs source:

```text
/Users/siddsdixit/Documents/omc/Docs
```

Published docs target:

```text
https://docs.onemillion.build
```

---

## Development Notes

From `/Users/siddsdixit/Documents/omc/Plugin`:

```bash
npm run build
```

Builds platform outputs from `source/`.

```bash
SUPABASE_SERVICE_KEY=... npm run sync:supabase
```

Syncs modes/skills to Supabase for extension delivery.

---

← [Back to teach-one-million](../README.md)
