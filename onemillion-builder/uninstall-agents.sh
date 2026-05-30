#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

rm -rf "$ROOT_DIR/.claude/agents" "$ROOT_DIR/.claude/skills"
rm -f "$ROOT_DIR/.cursor/rules/onemillion-course.mdc"
rm -f "$ROOT_DIR/.agents/rules/onemillion-course.md"
rm -f "$ROOT_DIR/.gemini/GEMINI.md"
rm -f "$ROOT_DIR/.github/copilot-instructions.md"
rm -f "$ROOT_DIR/.github/instructions/onemillion-course.instructions.md"

echo "OneMillion harness adapters removed."

