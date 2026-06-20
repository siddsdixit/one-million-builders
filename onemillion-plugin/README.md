# OneMillion Plugin

**Optional native extension path for the OneMillion agent system.**

Learners should not start here. The only learner landing page is:

```text
https://github.com/siddsdixit/one-million-builders/tree/main/course
```

The course does not depend on the plugin for the first local learning flow. The primary course architecture is harness-neutral:

```text
AGENTS.md + course/course-manifest.json + course/agents/
```

That lets learners start in Claude Code, Cursor, Codex, Gemini, Antigravity, Copilot, or another coding harness.

The plugin remains the future first-class product experience: native modes, cloud sync, account features, and packaged extension delivery.

---

## Current Course Path

```text
Open https://github.com/siddsdixit/one-million-builders/tree/main/course
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

## Maintainer Notes

This folder is for future native extension packaging. It is not part of the learner start path.

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

← [Course Landing](../course/README.md)
