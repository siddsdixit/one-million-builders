#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

mkdir -p "$ROOT_DIR/.claude/agents" "$ROOT_DIR/.claude/skills"
mkdir -p "$ROOT_DIR/.cursor/rules" "$ROOT_DIR/.agents/rules" "$ROOT_DIR/.gemini" "$ROOT_DIR/.github/instructions"

cp "$ROOT_DIR"/onemillion-agents/agents/*.md "$ROOT_DIR/.claude/agents/"
cp -R "$ROOT_DIR"/onemillion-agents/skills/. "$ROOT_DIR/.claude/skills/"

cat > "$ROOT_DIR/.cursor/rules/onemillion-course.mdc" <<'RULE'
---
description: OneMillion course learning orchestrator
alwaysApply: true
---

Read `AGENTS.md` first. Use `onemillion-builder/course-manifest.json` and `onemillion-agents/agents/orchestrator.md` to teach the OneMillion course one day at a time.

When the learner says "day done", run the Day Done Protocol from `AGENTS.md`.
RULE

cat > "$ROOT_DIR/.agents/rules/onemillion-course.md" <<'RULE'
# OneMillion Course Rule

Read `AGENTS.md` first. Use `onemillion-builder/course-manifest.json` and `onemillion-agents/agents/orchestrator.md` to teach the course one day at a time.

Do not skip learning moments. The learner must still touch required external tools.
RULE

cat > "$ROOT_DIR/.gemini/GEMINI.md" <<'RULE'
# OneMillion Course

Read `../AGENTS.md` or the repository root `AGENTS.md` first.

Use the course manifest and portable agent files to become the OneMillion learning orchestrator.
RULE

cat > "$ROOT_DIR/.github/copilot-instructions.md" <<'RULE'
# OneMillion Course Instructions

Read `AGENTS.md` first. The learner is taking the OneMillion course. Use `onemillion-builder/course-manifest.json` and `onemillion-agents/agents/orchestrator.md` to teach one day at a time.
RULE

cat > "$ROOT_DIR/.github/instructions/onemillion-course.instructions.md" <<'RULE'
---
applyTo: "**"
---

Read `AGENTS.md` first and follow the OneMillion learning orchestrator protocol.
RULE

echo "OneMillion harness adapters installed."
echo
echo "Next:"
echo "  Open this repo in your coding harness."
echo "  Say: I am starting the OneMillion course. Read AGENTS.md and start Day 1."

