#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
UPSTREAM_REPO="siddsdixit/one-million-builders"
UPSTREAM_URL="https://github.com/${UPSTREAM_REPO}.git"
COURSE_PAGE="https://github.com/${UPSTREAM_REPO}/tree/main/course"
STATE_DIR="$ROOT_DIR/.onemillion"
TOOL_REPORT="$STATE_DIR/tooling-preflight.md"
SKIP_TOOL_INSTALL="${ONEMILLION_SKIP_TOOL_INSTALL:-0}"
INSTALL_GLOBAL_ADAPTERS="${ONEMILLION_INSTALL_GLOBAL_ADAPTERS:-1}"

TOOL_STATUS=()
TOOL_WARNINGS=()

status_line() {
  TOOL_STATUS+=("$1")
}

warning_line() {
  TOOL_WARNINGS+=("$1")
}

has_command() {
  command -v "$1" >/dev/null 2>&1
}

version_or_missing() {
  local binary="$1"
  local version_args="${2:---version}"
  if has_command "$binary"; then
    "$binary" $version_args 2>&1 | head -n 1
  else
    echo "missing"
  fi
}

node_major_version() {
  if ! has_command node; then
    echo "0"
    return
  fi
  node -p 'Number(process.versions.node.split(".")[0])' 2>/dev/null || echo "0"
}

install_with_npm_global() {
  local binary="$1"
  local package="$2"
  local label="$3"

  if has_command "$binary"; then
    status_line "- OK $label: $(version_or_missing "$binary")"
    return
  fi

  if [[ "$SKIP_TOOL_INSTALL" == "1" ]]; then
    status_line "- SKIP $label: $binary not installed; tool install disabled"
    return
  fi

  if ! has_command npm; then
    warning_line "- MISSING $label: npm is required to install $package"
    return
  fi

  echo "Installing $label..."
  if npm install -g "$package"; then
    status_line "- INSTALLED $label: $(version_or_missing "$binary")"
  else
    warning_line "- FAILED $label: run npm install -g $package"
  fi
}

install_with_brew() {
  local binary="$1"
  local formula="$2"
  local label="$3"

  if has_command "$binary"; then
    status_line "- OK $label: $(version_or_missing "$binary")"
    return
  fi

  if [[ "$SKIP_TOOL_INSTALL" == "1" ]]; then
    status_line "- SKIP $label: $binary not installed; tool install disabled"
    return
  fi

  if ! has_command brew; then
    warning_line "- MISSING $label: Homebrew is required for this global install path"
    return
  fi

  echo "Installing $label..."
  if brew install "$formula"; then
    status_line "- INSTALLED $label: $(version_or_missing "$binary")"
  else
    warning_line "- FAILED $label: run brew install $formula"
  fi
}

install_vercel_cli() {
  if has_command vercel; then
    status_line "- OK Vercel CLI: $(version_or_missing vercel)"
    return
  fi

  if [[ "$SKIP_TOOL_INSTALL" == "1" ]]; then
    status_line "- SKIP Vercel CLI: vercel not installed; tool install disabled"
    return
  fi

  if has_command pnpm; then
    echo "Installing Vercel CLI with pnpm..."
    if pnpm i -g vercel; then
      status_line "- INSTALLED Vercel CLI: $(version_or_missing vercel)"
    else
      warning_line "- FAILED Vercel CLI: run pnpm i -g vercel"
    fi
  elif has_command npm; then
    echo "Installing Vercel CLI with npm..."
    if npm install -g vercel; then
      status_line "- INSTALLED Vercel CLI: $(version_or_missing vercel)"
    else
      warning_line "- FAILED Vercel CLI: run npm install -g vercel"
    fi
  else
    warning_line "- MISSING Vercel CLI: install Node.js 20+ first, then install Vercel CLI"
  fi
}

install_antigravity_cli() {
  if has_command agy; then
    status_line "- OK Antigravity CLI: $(version_or_missing agy)"
    return
  fi

  if [[ "$SKIP_TOOL_INSTALL" == "1" ]]; then
    status_line "- SKIP Antigravity CLI: agy not installed; tool install disabled"
    return
  fi

  if ! has_command curl; then
    warning_line "- MISSING Antigravity CLI: curl is required for the official installer"
    return
  fi

  echo "Installing Antigravity CLI..."
  if curl -fsSL https://antigravity.google/cli/install.sh | bash; then
    export PATH="$HOME/.local/bin:$PATH"
    status_line "- INSTALLED Antigravity CLI: $(version_or_missing agy)"
  else
    warning_line "- FAILED Antigravity CLI: run curl -fsSL https://antigravity.google/cli/install.sh | bash"
  fi
}

install_course_tooling() {
  mkdir -p "$STATE_DIR"

  echo
  echo "Checking course tooling..."

  local node_major
  node_major="$(node_major_version)"

  if (( node_major >= 20 )); then
    status_line "- OK Node.js: $(version_or_missing node)"
  elif has_command node; then
    warning_line "- OLD Node.js: $(version_or_missing node). Use Node.js 20+ for Supabase CLI and modern Next.js."
  else
    warning_line "- MISSING Node.js: install Node.js 20+ before Day 6/7."
  fi

  if has_command git; then
    status_line "- OK Git: $(version_or_missing git)"
  else
    warning_line "- MISSING Git: install Git before starting the course."
  fi

  install_with_brew gh gh "GitHub CLI"
  install_with_npm_global claude @anthropic-ai/claude-code "Claude Code"
  install_with_npm_global codex @openai/codex "Codex CLI"
  install_with_npm_global gemini @google/gemini-cli "Gemini CLI"
  install_antigravity_cli
  install_vercel_cli
  install_with_brew supabase supabase/tap/supabase "Supabase CLI"

  if has_command docker; then
    status_line "- OK Docker-compatible runtime: $(version_or_missing docker)"
  else
    warning_line "- MISSING Docker-compatible runtime: Supabase local development needs Docker Desktop, OrbStack, Colima, Rancher Desktop, or Podman."
  fi

  if has_command npm; then
    status_line "- OK npm: $(version_or_missing npm)"
  else
    warning_line "- MISSING npm: install Node.js 20+ with npm."
  fi

  {
    echo "# OneMillion Tooling Preflight"
    echo
    echo "Generated by \`./course/install-agents.sh\`."
    echo
    echo "## Status"
    printf '%s\n' "${TOOL_STATUS[@]}"
    echo
    echo "## Manual Actions"
    if (( ${#TOOL_WARNINGS[@]} == 0 )); then
      echo "- None."
    else
      printf '%s\n' "${TOOL_WARNINGS[@]}"
    fi
    echo
    echo "## Official Install Notes Encoded"
    echo "- Codex CLI: npm package \`@openai/codex\` or official installer."
    echo "- Claude Code: npm package \`@anthropic-ai/claude-code\`."
    echo "- Gemini CLI: npm package \`@google/gemini-cli\`."
    echo "- Antigravity CLI: official \`agy\` installer."
    echo "- Vercel CLI: global \`vercel\` package."
    echo "- Supabase CLI: Homebrew global install; npm global install is intentionally not used."
  } > "$TOOL_REPORT"
}

upsert_marked_block() {
  local file="$1"
  local start_marker="$2"
  local end_marker="$3"
  local content_file="$4"
  mkdir -p "$(dirname "$file")"
  touch "$file"
  if grep -Fq "$start_marker" "$file"; then
    awk -v start="$start_marker" -v end="$end_marker" -v content_file="$content_file" '
      $0 == start { print start; while ((getline line < content_file) > 0) print line; print end; skip = 1; next }
      $0 == end { skip = 0; next }
      !skip { print }
    ' CONTENT_FILE="$content_file" "$file" > "$file.tmp"
    mv "$file.tmp" "$file"
  else
    {
      printf '\n%s\n' "$start_marker"
      cat "$content_file"
      printf '%s\n' "$end_marker"
    } >> "$file"
  fi
}

toml_escape_multiline() {
  sed 's/"""/\\""\\""/g' "$1"
}

install_global_harness_adapters() {
  if [[ "$INSTALL_GLOBAL_ADAPTERS" != "1" ]]; then
    status_line "- SKIP Global harness adapters: disabled by ONEMILLION_INSTALL_GLOBAL_ADAPTERS=0"
    return
  fi

  local global_prompt
  global_prompt="$(mktemp)"
  cat > "$global_prompt" <<'RULE'
OneMillion course support:
- When a workspace contains `AGENTS.md` and `course/course-manifest.json`, read them first.
- Treat `course/days/single.md` as the day-by-day curriculum.
- Treat `course/agents/agents/orchestrator.md` as the teaching protocol.
- Enforce the fork/clone/origin/upstream preflight before Day 0.
- Teach one day at a time and verify before advancing.
RULE

  mkdir -p "$HOME/.claude/commands"
  cat > "$HOME/.claude/commands/onemillion.md" <<'RULE'
# OneMillion

If the current workspace contains `AGENTS.md` and `course/course-manifest.json`, read those files first. Then read `course/docs/teaching-protocol.md`, `course/days/single.md`, and `course/agents/agents/orchestrator.md`.

Become the learner's OneMillion learning orchestrator. Enforce the Preflight Gate, start Day 0, teach one day at a time, and verify each `day done` before advancing.
RULE

  upsert_marked_block "$HOME/.gemini/GEMINI.md" "<!-- ONEMILLION START -->" "<!-- ONEMILLION END -->" "$global_prompt"

  mkdir -p "$HOME/.copilot"
  upsert_marked_block "$HOME/.copilot/copilot-instructions.md" "<!-- ONEMILLION START -->" "<!-- ONEMILLION END -->" "$global_prompt"

  local agy_plugin_dir="$HOME/.gemini/antigravity-cli/plugins/onemillion"
  mkdir -p "$agy_plugin_dir/agents" "$agy_plugin_dir/skills" "$agy_plugin_dir/rules"
  cp "$ROOT_DIR"/course/agents/agents/*.md "$agy_plugin_dir/agents/"
  cp -R "$ROOT_DIR"/course/agents/skills/. "$agy_plugin_dir/skills/"
  cat > "$agy_plugin_dir/plugin.json" <<'JSON'
{
  "name": "onemillion",
  "displayName": "OneMillion Builder Course",
  "version": "1.0.0",
  "description": "OneMillion course orchestrator, agents, skills, and workspace rules."
}
JSON
  cat > "$agy_plugin_dir/rules/onemillion-course.md" <<'RULE'
# OneMillion Course Rule

When the active workspace contains `AGENTS.md` and `course/course-manifest.json`, become the OneMillion learning orchestrator. Read the manifest, teaching protocol, single course flow, and orchestrator agent. Enforce fork-first setup, teach one day at a time, and verify before advancing.
RULE

  rm -f "$global_prompt"
  status_line "- OK Global Claude command: $HOME/.claude/commands/onemillion.md"
  status_line "- OK Global Gemini/Antigravity rule: $HOME/.gemini/GEMINI.md"
  status_line "- OK Global Antigravity plugin: $agy_plugin_dir"
  status_line "- OK Global Copilot CLI instructions: $HOME/.copilot/copilot-instructions.md"
}

echo "OneMillion course setup"
echo "Course page: $COURSE_PAGE"
echo

if ! git -C "$ROOT_DIR" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  if command -v gh >/dev/null 2>&1 && gh auth status >/dev/null 2>&1; then
    GH_USER_FROM_ZIP="$(gh api user --jq .login)"
    FORK_REPO_FROM_ZIP="${GH_USER_FROM_ZIP}/one-million-builders"
    FORK_URL_FROM_ZIP="https://github.com/${FORK_REPO_FROM_ZIP}.git"
    TARGET_DIR="$(cd "$ROOT_DIR/.." && pwd)/one-million-builders-${GH_USER_FROM_ZIP}"

    echo "This directory is not a git clone. Creating/verifying your fork and cloning it instead."
    gh repo star "$UPSTREAM_REPO" >/dev/null 2>&1 || true
    if ! gh repo view "$FORK_REPO_FROM_ZIP" >/dev/null 2>&1; then
      gh repo fork "$UPSTREAM_REPO" --clone=false >/dev/null
    fi

    if [[ ! -d "$TARGET_DIR/.git" ]]; then
      git clone "$FORK_URL_FROM_ZIP" "$TARGET_DIR"
    fi

    "$TARGET_DIR/course/install-agents.sh"
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

     git clone https://github.com/YOUR-USERNAME/one-million-builders.git
     cd one-million-builders
     ./course/install-agents.sh
EOF
  exit 1
fi

if [[ ! -f "$ROOT_DIR/AGENTS.md" || ! -f "$ROOT_DIR/course/course-manifest.json" ]]; then
  cat <<EOF
Stop: this clone does not look like the OneMillion course repo.

Expected files:
  AGENTS.md
  course/course-manifest.json

Clone your fork of https://github.com/$UPSTREAM_REPO and run this script from
that repo root:

  ./course/install-agents.sh
EOF
  exit 1
fi

GH_USER=""
FORK_REPO=""
FORK_URL=""

if command -v gh >/dev/null 2>&1 && gh auth status >/dev/null 2>&1; then
  GH_USER="$(gh api user --jq .login)"
  FORK_REPO="${GH_USER}/one-million-builders"
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
  git remote set-url origin https://github.com/YOUR-USERNAME/one-million-builders.git
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
  git remote set-url origin https://github.com/YOUR-USERNAME/one-million-builders.git
  git remote add upstream $UPSTREAM_URL

Then run:
  ./course/install-agents.sh
EOF
  exit 1
fi

if [[ "$ORIGIN_URL" == *"siddsdixit/one-million-builders"* ]]; then
  cat <<EOF
Stop: origin still points to Sid's upstream repo.

Your origin must be your fork, not $UPSTREAM_REPO.

Fix:
  1. Fork https://github.com/$UPSTREAM_REPO
  2. Run:
     git remote set-url origin https://github.com/YOUR-USERNAME/one-million-builders.git
     ./course/install-agents.sh
EOF
  exit 1
fi

if [[ "$UPSTREAM_REMOTE_URL" != *"siddsdixit/one-million-builders"* ]]; then
  cat <<EOF
Stop: upstream does not point to Sid's course repo.

Fix:
  git remote set-url upstream $UPSTREAM_URL
  ./course/install-agents.sh
EOF
  exit 1
fi

mkdir -p "$ROOT_DIR/.claude/agents" "$ROOT_DIR/.claude/skills" "$ROOT_DIR/.claude/commands"
mkdir -p "$ROOT_DIR/.cursor/rules" "$ROOT_DIR/.agents/rules" "$ROOT_DIR/.agents/skills"
mkdir -p "$ROOT_DIR/.codex/agents"
mkdir -p "$ROOT_DIR/.opencode/agents" "$ROOT_DIR/.opencode/skills"
mkdir -p "$ROOT_DIR/.gemini" "$ROOT_DIR/.github/instructions"

cp "$ROOT_DIR"/course/agents/agents/*.md "$ROOT_DIR/.claude/agents/"
cp -R "$ROOT_DIR"/course/agents/skills/. "$ROOT_DIR/.claude/skills/"
cp -R "$ROOT_DIR"/course/agents/skills/. "$ROOT_DIR/.agents/skills/"
cp -R "$ROOT_DIR"/course/agents/skills/. "$ROOT_DIR/.opencode/skills/"

for AGENT_FILE in "$ROOT_DIR"/course/agents/agents/*.md; do
  AGENT_BASENAME="$(basename "$AGENT_FILE" .md)"
  CODEX_AGENT_NAME="${AGENT_BASENAME//-/_}"
  cat > "$ROOT_DIR/.codex/agents/${AGENT_BASENAME}.toml" <<EOF
name = "$CODEX_AGENT_NAME"
description = "OneMillion $AGENT_BASENAME agent. Use for the matching course phase or when the orchestrator delegates this role."
developer_instructions = """
$(toml_escape_multiline "$AGENT_FILE")
"""
EOF

  OPENCODE_MODE="subagent"
  if [[ "$AGENT_BASENAME" == "onemillion" || "$AGENT_BASENAME" == "orchestrator" ]]; then
    OPENCODE_MODE="primary"
  fi

  cat > "$ROOT_DIR/.opencode/agents/${AGENT_BASENAME}.md" <<EOF
---
description: OneMillion $AGENT_BASENAME agent. Use for the matching course phase or when the orchestrator delegates this role.
mode: $OPENCODE_MODE
permission:
  edit: ask
  bash: ask
  skill:
    "*": allow
---

$(cat "$AGENT_FILE")
EOF
done

cat > "$ROOT_DIR/.codex/config.toml" <<'RULE'
[agents]
max_threads = 6
max_depth = 1
RULE

cat > "$ROOT_DIR/opencode.json" <<'JSON'
{
  "$schema": "https://opencode.ai/config.json",
  "instructions": [
    "AGENTS.md",
    "course/docs/teaching-protocol.md",
    "course/days/single.md",
    "course/agents/agents/orchestrator.md"
  ],
  "permission": {
    "skill": {
      "*": "allow"
    }
  }
}
JSON

cat > "$ROOT_DIR/.claude/commands/onemillion.md" <<'RULE'
# OneMillion

Read `AGENTS.md`, `course/course-manifest.json`, `course/docs/teaching-protocol.md`, `course/days/single.md`, and `course/agents/agents/orchestrator.md`.

Become the learner's OneMillion learning orchestrator.

First enforce the Preflight Gate:

- real git worktree
- `origin` points to the learner's fork
- `upstream` points to `siddsdixit/one-million-builders`
- Day 0 orientation/reflection plus public or private commitment before Day 1

Then teach one day at a time. When the learner says `day done`, follow the Day Done Protocol in `AGENTS.md`; do not advance until the current gate passes.

Do not give bare task assignments. Start with a proper greeting, explain what OneMillion is, explain the AI/human contract, introduce the current day, provide copy-ready actions, define done, and tell the learner when to say `day done`. When naming an external provider, include the exact full clickable URL from `course/docs/account-setup.md`.
RULE

cat > "$ROOT_DIR/.cursor/rules/onemillion-course.mdc" <<'RULE'
---
description: OneMillion course learning orchestrator
alwaysApply: true
---

Read `AGENTS.md` first. Use `course/course-manifest.json`, `course/docs/teaching-protocol.md`, `course/days/single.md`, and `course/agents/agents/orchestrator.md` to teach the OneMillion course one day at a time.

Before Day 0 or Day 1, enforce the Preflight Gate in `AGENTS.md`. If the repo is not a git clone with an `origin` fork and `upstream` set to `siddsdixit/one-million-builders`, stop and fix the setup first.

When the learner says "day done", run the Day Done Protocol from `AGENTS.md`.

Do not give bare task assignments. Properly greet the learner, explain the course, introduce the current day, provide copy-ready actions, and define what done means. When naming an external provider, include the exact full clickable URL from `course/docs/account-setup.md`.
RULE

cat > "$ROOT_DIR/.agents/rules/onemillion-course.md" <<'RULE'
# OneMillion Course Rule

Read `AGENTS.md` first. Use `course/course-manifest.json`, `course/docs/teaching-protocol.md`, `course/days/single.md`, and `course/agents/agents/orchestrator.md` to teach the course one day at a time.

Before Day 0 or Day 1, enforce the Preflight Gate in `AGENTS.md`. If the repo is not a git clone with an `origin` fork and `upstream` set to `siddsdixit/one-million-builders`, stop and fix the setup first.

Do not skip learning moments. The learner must still touch required external tools.
Do not give bare task assignments. Properly greet the learner, explain the course, introduce the current day, provide copy-ready actions, and define what done means. When naming an external provider, include the exact full clickable URL from `course/docs/account-setup.md`.
RULE

cat > "$ROOT_DIR/.gemini/GEMINI.md" <<'RULE'
# OneMillion Course

Read the repository root `AGENTS.md` first.

Use the course manifest and portable agent files to become the OneMillion learning orchestrator.
Follow `course/docs/teaching-protocol.md`.
Read `course/days/single.md` for the full development pipeline and day-by-day flow.
Use `course/agents/agents/` as the OneMillion source agent library.
Use `course/agents/skills/` as the OneMillion source skill library.

Before Day 0 or Day 1, enforce the Preflight Gate in `AGENTS.md`. If the repo is not a git clone with an `origin` fork and `upstream` set to `siddsdixit/one-million-builders`, stop and fix the setup first.
Do not give bare task assignments. Properly greet the learner, explain the course, introduce the current day, provide copy-ready actions, and define what done means. When naming an external provider, include the exact full clickable URL from `course/docs/account-setup.md`.
RULE

cat > "$ROOT_DIR/.gemini/settings.json" <<'JSON'
{
  "contextFileName": [
    "GEMINI.md",
    "AGENTS.md"
  ]
}
JSON

cat > "$ROOT_DIR/.github/copilot-instructions.md" <<'RULE'
# OneMillion Course Instructions

Read `AGENTS.md` first. The learner is taking the OneMillion course. Use `course/course-manifest.json`, `course/docs/teaching-protocol.md`, `course/days/single.md`, and `course/agents/agents/orchestrator.md` to teach one day at a time.

Before Day 0 or Day 1, enforce the Preflight Gate in `AGENTS.md`. If the repo is not a git clone with an `origin` fork and `upstream` set to `siddsdixit/one-million-builders`, stop and fix the setup first.
Do not give bare task assignments. Properly greet the learner, explain the course, introduce the current day, provide copy-ready actions, and define what done means. When naming an external provider, include the exact full clickable URL from `course/docs/account-setup.md`.
RULE

cat > "$ROOT_DIR/.github/instructions/onemillion-course.instructions.md" <<'RULE'
---
applyTo: "**"
---

Read `AGENTS.md` first and follow the OneMillion learning orchestrator protocol. Also follow `course/docs/teaching-protocol.md` and `course/days/single.md`.

Before Day 0 or Day 1, enforce the Preflight Gate in `AGENTS.md`. If the repo is not a git clone with an `origin` fork and `upstream` set to `siddsdixit/one-million-builders`, stop and fix the setup first.
Do not give bare task assignments. Properly greet the learner, explain the course, introduce the current day, provide copy-ready actions, and define what done means. When naming an external provider, include the exact full clickable URL from `course/docs/account-setup.md`.
RULE

install_global_harness_adapters
install_course_tooling

REQUIRED_INSTALL_PATHS=(
  "AGENTS.md"
  "course/course-manifest.json"
  "course/docs/teaching-protocol.md"
  "course/days/single.md"
  "course/agents/agents/orchestrator.md"
  ".claude/agents/orchestrator.md"
  ".claude/skills/tech_stack/SKILL.md"
  ".claude/commands/onemillion.md"
  ".cursor/rules/onemillion-course.mdc"
  ".agents/rules/onemillion-course.md"
  ".agents/skills/tech_stack/SKILL.md"
  ".codex/config.toml"
  ".codex/agents/orchestrator.toml"
  ".opencode/agents/orchestrator.md"
  ".opencode/skills/tech_stack/SKILL.md"
  "opencode.json"
  ".gemini/GEMINI.md"
  ".gemini/settings.json"
  ".github/copilot-instructions.md"
  ".github/instructions/onemillion-course.instructions.md"
)

if [[ "$INSTALL_GLOBAL_ADAPTERS" == "1" ]]; then
  REQUIRED_INSTALL_PATHS+=(
    "$HOME/.claude/commands/onemillion.md"
    "$HOME/.gemini/GEMINI.md"
    "$HOME/.copilot/copilot-instructions.md"
    "$HOME/.gemini/antigravity-cli/plugins/onemillion/plugin.json"
  )
fi

MISSING_PATHS=()
for REQUIRED_PATH in "${REQUIRED_INSTALL_PATHS[@]}"; do
  if [[ "$REQUIRED_PATH" == "$HOME/"* ]]; then
    CHECK_PATH="$REQUIRED_PATH"
  else
    CHECK_PATH="$ROOT_DIR/$REQUIRED_PATH"
  fi
  if [[ ! -e "$CHECK_PATH" ]]; then
    MISSING_PATHS+=("$REQUIRED_PATH")
  fi
done

CLAUDE_AGENT_COUNT="$(find "$ROOT_DIR/.claude/agents" -maxdepth 1 -type f -name "*.md" | wc -l | tr -d ' ')"
CLAUDE_SKILL_COUNT="$(find "$ROOT_DIR/.claude/skills" -mindepth 2 -maxdepth 2 -type f -name "SKILL.md" | wc -l | tr -d ' ')"
CODEX_AGENT_COUNT="$(find "$ROOT_DIR/.codex/agents" -maxdepth 1 -type f -name "*.toml" | wc -l | tr -d ' ')"
CODEX_SKILL_COUNT="$(find "$ROOT_DIR/.agents/skills" -mindepth 2 -maxdepth 2 -type f -name "SKILL.md" | wc -l | tr -d ' ')"
OPENCODE_AGENT_COUNT="$(find "$ROOT_DIR/.opencode/agents" -maxdepth 1 -type f -name "*.md" | wc -l | tr -d ' ')"
OPENCODE_SKILL_COUNT="$(find "$ROOT_DIR/.opencode/skills" -mindepth 2 -maxdepth 2 -type f -name "SKILL.md" | wc -l | tr -d ' ')"

if (( CLAUDE_AGENT_COUNT < 10 )); then
  MISSING_PATHS+=(".claude/agents/*.md expected at least 10 files, found $CLAUDE_AGENT_COUNT")
fi

if (( CLAUDE_SKILL_COUNT < 5 )); then
  MISSING_PATHS+=(".claude/skills/*/SKILL.md expected at least 5 files, found $CLAUDE_SKILL_COUNT")
fi

if (( CODEX_AGENT_COUNT < 10 )); then
  MISSING_PATHS+=(".codex/agents/*.toml expected at least 10 files, found $CODEX_AGENT_COUNT")
fi

if (( CODEX_SKILL_COUNT < 5 )); then
  MISSING_PATHS+=(".agents/skills/*/SKILL.md expected at least 5 files, found $CODEX_SKILL_COUNT")
fi

if (( OPENCODE_AGENT_COUNT < 10 )); then
  MISSING_PATHS+=(".opencode/agents/*.md expected at least 10 files, found $OPENCODE_AGENT_COUNT")
fi

if (( OPENCODE_SKILL_COUNT < 5 )); then
  MISSING_PATHS+=(".opencode/skills/*/SKILL.md expected at least 5 files, found $OPENCODE_SKILL_COUNT")
fi

if (( ${#MISSING_PATHS[@]} > 0 )); then
  echo "Stop: harness adapter install verification failed."
  echo
  printf 'Missing or incomplete: %s\n' "${MISSING_PATHS[@]}"
  exit 1
fi

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

echo "OneMillion harness adapters installed."
echo
echo "Verified harness support:"
echo "  Codex / generic AGENTS.md: AGENTS.md"
echo "  Claude Code: .claude/agents, .claude/skills, .claude/commands/onemillion.md"
echo "  Codex: AGENTS.md, .codex/agents, .agents/skills"
echo "  Cursor: .cursor/rules/onemillion-course.mdc"
echo "  OpenCode: AGENTS.md, opencode.json, .opencode/agents, .opencode/skills"
echo "  Gemini CLI: .gemini/GEMINI.md and .gemini/settings.json"
echo "  Antigravity / generic agent harnesses: .agents/rules/onemillion-course.md"
echo "  GitHub Copilot: .github/copilot-instructions.md and .github/instructions/onemillion-course.instructions.md"
if [[ "$INSTALL_GLOBAL_ADAPTERS" == "1" ]]; then
  echo "  Global Claude command: $HOME/.claude/commands/onemillion.md"
  echo "  Global Gemini/Antigravity rule: $HOME/.gemini/GEMINI.md"
  echo "  Global Antigravity plugin: $HOME/.gemini/antigravity-cli/plugins/onemillion"
  echo "  Global Copilot CLI instructions: $HOME/.copilot/copilot-instructions.md"
fi
echo
echo "Tooling preflight:"
echo "  $TOOL_REPORT"
echo
echo "Next:"
echo "  cd $ROOT_DIR"
echo "  Open this directory in your coding harness."
echo
echo "Paste this:"
cat <<'EOF'
I am starting the OneMillion course from my fork.

Read AGENTS.md and course/course-manifest.json.
Read course/docs/teaching-protocol.md.
Read course/days/single.md.
Become my OneMillion learning orchestrator.
First enforce the Preflight Gate. If anything is wrong with clone/fork/upstream/downstream setup, stop and fix it before Day 0.
Then start Day 0. Do not start Day 1 until Day 0 passes.
Teach me one day at a time. Properly greet me, explain the course, explain the AI/human contract, introduce each day, provide copy-ready actions, and define what done means.
When I say "day done", verify the day and advance me.
Do not skip the learning or do the external tool steps for me.
EOF
