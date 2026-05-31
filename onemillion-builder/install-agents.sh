#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
UPSTREAM_REPO="siddsdixit/teach-one-million"
UPSTREAM_URL="https://github.com/${UPSTREAM_REPO}.git"
COURSE_PAGE="https://github.com/${UPSTREAM_REPO}/tree/main/onemillion-builder"
STATE_DIR="$ROOT_DIR/.onemillion"

echo "OneMillion course setup"
echo "Course page: $COURSE_PAGE"
echo

if ! git -C "$ROOT_DIR" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  if command -v gh >/dev/null 2>&1 && gh auth status >/dev/null 2>&1; then
    GH_USER_FROM_ZIP="$(gh api user --jq .login)"
    FORK_REPO_FROM_ZIP="${GH_USER_FROM_ZIP}/teach-one-million"
    FORK_URL_FROM_ZIP="https://github.com/${FORK_REPO_FROM_ZIP}.git"
    TARGET_DIR="$(cd "$ROOT_DIR/.." && pwd)/teach-one-million-${GH_USER_FROM_ZIP}"

    echo "This directory is not a git clone. Creating/verifying your fork and cloning it instead."
    gh repo star "$UPSTREAM_REPO" >/dev/null 2>&1 || true
    if ! gh repo view "$FORK_REPO_FROM_ZIP" >/dev/null 2>&1; then
      gh repo fork "$UPSTREAM_REPO" --clone=false >/dev/null
    fi

    if [[ ! -d "$TARGET_DIR/.git" ]]; then
      git clone "$FORK_URL_FROM_ZIP" "$TARGET_DIR"
    fi

    "$TARGET_DIR/onemillion-builder/install-agents.sh"
    echo
    echo "Start directory:"
    echo "  cd $TARGET_DIR"
    exit 0
  fi

  cat <<EOF
Stop: this directory is not a git clone.

The OneMillion course must run from a forked GitHub repo so your progress,
commits, and final Builder Claim have a real proof trail.

Do this first:
  1. Star $COURSE_PAGE
  2. Fork https://github.com/$UPSTREAM_REPO
  3. Clone your fork:

     git clone https://github.com/YOUR-USERNAME/teach-one-million.git
     cd teach-one-million
     ./onemillion-builder/install-agents.sh
EOF
  exit 1
fi

if [[ ! -f "$ROOT_DIR/AGENTS.md" || ! -f "$ROOT_DIR/onemillion-builder/course-manifest.json" ]]; then
  cat <<EOF
Stop: this clone does not look like the OneMillion course repo.

Expected files:
  AGENTS.md
  onemillion-builder/course-manifest.json

Clone your fork of https://github.com/$UPSTREAM_REPO and run this script from
that repo root:

  ./onemillion-builder/install-agents.sh
EOF
  exit 1
fi

GH_USER=""
FORK_REPO=""
FORK_URL=""

if command -v gh >/dev/null 2>&1 && gh auth status >/dev/null 2>&1; then
  GH_USER="$(gh api user --jq .login)"
  FORK_REPO="${GH_USER}/teach-one-million"
  FORK_URL="https://github.com/${FORK_REPO}.git"

  echo "Starring upstream repo..."
  gh repo star "$UPSTREAM_REPO" >/dev/null 2>&1 || true

  echo "Creating or verifying fork: $FORK_REPO"
  if ! gh repo view "$FORK_REPO" >/dev/null 2>&1; then
    gh repo fork "$UPSTREAM_REPO" --clone=false >/dev/null
  fi

  echo "Configuring git remotes..."
  if git -C "$ROOT_DIR" remote get-url origin >/dev/null 2>&1; then
    git -C "$ROOT_DIR" remote set-url origin "$FORK_URL"
  else
    git -C "$ROOT_DIR" remote add origin "$FORK_URL"
  fi

  if git -C "$ROOT_DIR" remote get-url upstream >/dev/null 2>&1; then
    git -C "$ROOT_DIR" remote set-url upstream "$UPSTREAM_URL"
  else
    git -C "$ROOT_DIR" remote add upstream "$UPSTREAM_URL"
  fi
else
  cat <<EOF
GitHub CLI is not installed or not authenticated.

Manual preflight is still mandatory before Day 1:
  1. Star https://github.com/$UPSTREAM_REPO
  2. Fork it into your GitHub account
  3. Make sure this clone points at your fork as origin
  4. Add Sid's repo as upstream

Example:
  git remote set-url origin https://github.com/YOUR-USERNAME/teach-one-million.git
  git remote add upstream $UPSTREAM_URL

Then run this script again after:
  gh auth login
EOF
fi

ORIGIN_URL="$(git -C "$ROOT_DIR" remote get-url origin 2>/dev/null || true)"
UPSTREAM_REMOTE_URL="$(git -C "$ROOT_DIR" remote get-url upstream 2>/dev/null || true)"

if [[ -z "$ORIGIN_URL" || -z "$UPSTREAM_REMOTE_URL" ]]; then
  cat <<EOF
Stop: git remotes are not ready.

This course needs both:
  origin   -> your fork
  upstream -> $UPSTREAM_URL

Fix:
  git remote set-url origin https://github.com/YOUR-USERNAME/teach-one-million.git
  git remote add upstream $UPSTREAM_URL

Then run:
  ./onemillion-builder/install-agents.sh
EOF
  exit 1
fi

if [[ "$ORIGIN_URL" == *"siddsdixit/teach-one-million"* ]]; then
  cat <<EOF
Stop: origin still points to Sid's upstream repo.

Your origin must be your fork, not $UPSTREAM_REPO.

Fix:
  1. Fork https://github.com/$UPSTREAM_REPO
  2. Run:
     git remote set-url origin https://github.com/YOUR-USERNAME/teach-one-million.git
     ./onemillion-builder/install-agents.sh
EOF
  exit 1
fi

if [[ "$UPSTREAM_REMOTE_URL" != *"siddsdixit/teach-one-million"* ]]; then
  cat <<EOF
Stop: upstream does not point to Sid's course repo.

Fix:
  git remote set-url upstream $UPSTREAM_URL
  ./onemillion-builder/install-agents.sh
EOF
  exit 1
fi

mkdir -p "$ROOT_DIR/.claude/agents" "$ROOT_DIR/.claude/skills" "$ROOT_DIR/.claude/commands"
mkdir -p "$ROOT_DIR/.cursor/rules" "$ROOT_DIR/.agents/rules" "$ROOT_DIR/.gemini" "$ROOT_DIR/.github/instructions"

cp "$ROOT_DIR"/onemillion-agents/agents/*.md "$ROOT_DIR/.claude/agents/"
cp -R "$ROOT_DIR"/onemillion-agents/skills/. "$ROOT_DIR/.claude/skills/"

cat > "$ROOT_DIR/.claude/commands/onemillion.md" <<'RULE'
# OneMillion

Read `AGENTS.md`, `onemillion-builder/course-manifest.json`, `onemillion-builder/docs/teaching-protocol.md`, and `onemillion-agents/agents/orchestrator.md`.

Become the learner's OneMillion learning orchestrator.

First enforce the Preflight Gate:

- real git worktree
- `origin` points to the learner's fork
- `upstream` points to `siddsdixit/teach-one-million`
- Day 0 public or private commitment before Day 1

Then teach one day at a time. When the learner says `day done`, follow the Day Done Protocol in `AGENTS.md`; do not advance until the current gate passes.

Do not give bare task assignments. Start with a proper greeting, explain what OneMillion is, explain the AI/human contract, introduce the current day, provide copy-ready actions, define done, and tell the learner when to say `day done`.
RULE

cat > "$ROOT_DIR/.cursor/rules/onemillion-course.mdc" <<'RULE'
---
description: OneMillion course learning orchestrator
alwaysApply: true
---

Read `AGENTS.md` first. Use `onemillion-builder/course-manifest.json`, `onemillion-builder/docs/teaching-protocol.md`, and `onemillion-agents/agents/orchestrator.md` to teach the OneMillion course one day at a time.

Before Day 0 or Day 1, enforce the Preflight Gate in `AGENTS.md`. If the repo is not a git clone with an `origin` fork and `upstream` set to `siddsdixit/teach-one-million`, stop and fix the setup first.

When the learner says "day done", run the Day Done Protocol from `AGENTS.md`.

Do not give bare task assignments. Properly greet the learner, explain the course, introduce the current day, provide copy-ready actions, and define what done means.
RULE

cat > "$ROOT_DIR/.agents/rules/onemillion-course.md" <<'RULE'
# OneMillion Course Rule

Read `AGENTS.md` first. Use `onemillion-builder/course-manifest.json`, `onemillion-builder/docs/teaching-protocol.md`, and `onemillion-agents/agents/orchestrator.md` to teach the course one day at a time.

Before Day 0 or Day 1, enforce the Preflight Gate in `AGENTS.md`. If the repo is not a git clone with an `origin` fork and `upstream` set to `siddsdixit/teach-one-million`, stop and fix the setup first.

Do not skip learning moments. The learner must still touch required external tools.
Do not give bare task assignments. Properly greet the learner, explain the course, introduce the current day, provide copy-ready actions, and define what done means.
RULE

cat > "$ROOT_DIR/.gemini/GEMINI.md" <<'RULE'
# OneMillion Course

Read `../AGENTS.md` or the repository root `AGENTS.md` first.

Use the course manifest and portable agent files to become the OneMillion learning orchestrator.
Follow `../onemillion-builder/docs/teaching-protocol.md` or the repository root `onemillion-builder/docs/teaching-protocol.md`.

Before Day 0 or Day 1, enforce the Preflight Gate in `AGENTS.md`. If the repo is not a git clone with an `origin` fork and `upstream` set to `siddsdixit/teach-one-million`, stop and fix the setup first.
Do not give bare task assignments. Properly greet the learner, explain the course, introduce the current day, provide copy-ready actions, and define what done means.
RULE

cat > "$ROOT_DIR/.github/copilot-instructions.md" <<'RULE'
# OneMillion Course Instructions

Read `AGENTS.md` first. The learner is taking the OneMillion course. Use `onemillion-builder/course-manifest.json`, `onemillion-builder/docs/teaching-protocol.md`, and `onemillion-agents/agents/orchestrator.md` to teach one day at a time.

Before Day 0 or Day 1, enforce the Preflight Gate in `AGENTS.md`. If the repo is not a git clone with an `origin` fork and `upstream` set to `siddsdixit/teach-one-million`, stop and fix the setup first.
Do not give bare task assignments. Properly greet the learner, explain the course, introduce the current day, provide copy-ready actions, and define what done means.
RULE

cat > "$ROOT_DIR/.github/instructions/onemillion-course.instructions.md" <<'RULE'
---
applyTo: "**"
---

Read `AGENTS.md` first and follow the OneMillion learning orchestrator protocol. Also follow `onemillion-builder/docs/teaching-protocol.md`.

Before Day 0 or Day 1, enforce the Preflight Gate in `AGENTS.md`. If the repo is not a git clone with an `origin` fork and `upstream` set to `siddsdixit/teach-one-million`, stop and fix the setup first.
Do not give bare task assignments. Properly greet the learner, explain the course, introduce the current day, provide copy-ready actions, and define what done means.
RULE

mkdir -p "$STATE_DIR"
if [[ ! -f "$STATE_DIR/state.json" ]]; then
  cat > "$STATE_DIR/state.json" <<EOF
{
  "course": "OneMillion Builder",
  "current_day": 0,
  "current_phase": "preflight",
  "next_agent": "orchestrator",
  "product_dir": "my-onemillion-build",
  "status": "preflight_complete",
  "last_verified_day": null,
  "preflight": {
    "canonical_landing_page": "$COURSE_PAGE",
    "upstream_repo": "$UPSTREAM_REPO",
    "fork_repo": "${FORK_REPO:-manual}",
    "origin_remote": "$(git -C "$ROOT_DIR" remote get-url origin 2>/dev/null || true)",
    "upstream_remote": "$(git -C "$ROOT_DIR" remote get-url upstream 2>/dev/null || true)"
  }
}
EOF
fi

if [[ ! -f "$STATE_DIR/progress.md" ]]; then
  cat > "$STATE_DIR/progress.md" <<EOF
# OneMillion Progress

- Current day: 0
- Current phase: preflight complete
- Next action: open this repo in your coding harness and start Day 0.
- Course page: $COURSE_PAGE
EOF
fi

echo "OneMillion harness adapters installed."
echo
echo "Next:"
echo "  cd $ROOT_DIR"
echo "  Open this directory in your coding harness."
echo
echo "Paste this:"
cat <<'EOF'
I am starting the OneMillion course from my fork.

Read AGENTS.md and onemillion-builder/course-manifest.json.
Read onemillion-builder/docs/teaching-protocol.md.
Become my OneMillion learning orchestrator.
First enforce the Preflight Gate. If anything is wrong with clone/fork/upstream/downstream setup, stop and fix it before Day 0.
Then start Day 0 and Day 1.
Teach me one day at a time. Properly greet me, explain the course, explain the AI/human contract, introduce each day, provide copy-ready actions, and define what done means.
When I say "day done", verify the day and advance me.
Do not skip the learning or do the external tool steps for me.
EOF
