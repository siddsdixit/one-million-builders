#!/usr/bin/env python3
"""
OneMillion course simulator.

Runs a synthetic learner QA pass against the course repo without touching GitHub.
It creates throwaway clones/workspaces under /tmp and checks:

- landing/course material is internally valid
- installer blocks unsafe states
- installer succeeds in a fork-like local clone
- Day 0/Day 1 artifacts can be created and verified
- Day 4 design artifacts can be created and verified
- Day 6 deployment/source matching verifier works on a local mock deployment
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import socket
import subprocess
import sys
import tempfile
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent


class Result:
    def __init__(self, name: str, passed: bool, details: str = "") -> None:
        self.name = name
        self.passed = passed
        self.details = details.strip()


def run(
    cmd: list[str],
    cwd: Path,
    *,
    check: bool = False,
    env: dict[str, str] | None = None,
    timeout: int = 30,
) -> subprocess.CompletedProcess[str]:
    merged_env = os.environ.copy()
    if env:
        merged_env.update(env)
    return subprocess.run(
        cmd,
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=check,
        env=merged_env,
        timeout=timeout,
    )


def record(results: list[Result], name: str, passed: bool, details: str = "") -> None:
    results.append(Result(name, passed, details))


def copy_repo(destination: Path) -> None:
    ignore = shutil.ignore_patterns(
        ".git",
        "remotion/node_modules",
        "remotion/.cache",
        "remotion/out",
        "__pycache__",
        "*.pyc",
        ".DS_Store",
    )
    shutil.copytree(REPO, destination, ignore=ignore)


def init_fork_like_repo(path: Path) -> None:
    run(["git", "init", "-b", "main"], path, check=True)
    run(["git", "config", "user.email", "simulator@example.com"], path, check=True)
    run(["git", "config", "user.name", "OneMillion Simulator"], path, check=True)
    run(["git", "add", "."], path, check=True)
    run(["git", "commit", "-m", "simulated learner fork"], path, check=True)
    run(["git", "remote", "add", "origin", "https://github.com/simulated-learner/one-million-builders.git"], path, check=True)
    run(["git", "remote", "add", "upstream", "https://github.com/siddsdixit/one-million-builders.git"], path, check=True)


def create_fake_gh_bin(bin_dir: Path, authenticated: bool = False) -> None:
    script = bin_dir / "gh"
    if authenticated:
        body = """#!/usr/bin/env bash
set -euo pipefail
if [[ "$1" == "auth" && "$2" == "status" ]]; then exit 0; fi
if [[ "$1" == "api" && "$2" == "user" ]]; then echo "simulated-learner"; exit 0; fi
if [[ "$1" == "repo" && "$2" == "star" ]]; then exit 0; fi
if [[ "$1" == "repo" && "$2" == "view" ]]; then exit 0; fi
if [[ "$1" == "repo" && "$2" == "fork" ]]; then exit 0; fi
echo "fake gh unsupported: $*" >&2
exit 1
"""
    else:
        body = """#!/usr/bin/env bash
if [[ "$1" == "auth" && "$2" == "status" ]]; then exit 1; fi
echo "fake gh unauthenticated" >&2
exit 1
"""
    script.write_text(body)
    script.chmod(0o755)


def test_course_quality(results: list[Result]) -> None:
    proc = run(["python3", "course/tools/course_quality_check.py"], REPO)
    record(results, "course_quality_check", proc.returncode == 0, proc.stdout)


def test_installer_blocks_plain_folder(results: list[Result], tmp: Path) -> None:
    plain = tmp / "plain-folder"
    copy_repo(plain)
    fake_bin = tmp / "fake-gh-off"
    fake_bin.mkdir()
    create_fake_gh_bin(fake_bin, authenticated=False)
    env = {
        "PATH": f"{fake_bin}:{os.environ['PATH']}",
        "ONEMILLION_SKIP_TOOL_INSTALL": "1",
        "ONEMILLION_INSTALL_GLOBAL_ADAPTERS": "0",
        "HOME": str(tmp / "home-plain"),
    }
    proc = run(["bash", "course/install-agents.sh"], plain, env=env)
    passed = proc.returncode != 0 and "not a git clone" in proc.stdout and "Clone your fork" in proc.stdout
    record(results, "installer_blocks_downloaded_or_plain_folder", passed, proc.stdout)


def test_installer_blocks_upstream_origin(results: list[Result], tmp: Path) -> None:
    repo = tmp / "upstream-origin"
    copy_repo(repo)
    init_fork_like_repo(repo)
    run(["git", "remote", "set-url", "origin", "https://github.com/siddsdixit/one-million-builders.git"], repo, check=True)
    fake_bin = tmp / "fake-gh-off-2"
    fake_bin.mkdir()
    create_fake_gh_bin(fake_bin, authenticated=False)
    env = {
        "PATH": f"{fake_bin}:{os.environ['PATH']}",
        "ONEMILLION_SKIP_TOOL_INSTALL": "1",
        "ONEMILLION_INSTALL_GLOBAL_ADAPTERS": "0",
        "HOME": str(tmp / "home-upstream"),
    }
    proc = run(["bash", "course/install-agents.sh"], repo, env=env)
    passed = proc.returncode != 0 and "origin still points to Sid" in proc.stdout
    record(results, "installer_blocks_upstream_origin", passed, proc.stdout)


def test_installer_succeeds_in_fork_like_clone(results: list[Result], tmp: Path) -> Path:
    repo = tmp / "fork-like"
    copy_repo(repo)
    init_fork_like_repo(repo)
    fake_bin = tmp / "fake-gh-off-3"
    fake_bin.mkdir()
    create_fake_gh_bin(fake_bin, authenticated=False)
    env = {
        "PATH": f"{fake_bin}:{os.environ['PATH']}",
        "ONEMILLION_SKIP_TOOL_INSTALL": "1",
        "ONEMILLION_INSTALL_GLOBAL_ADAPTERS": "0",
        "HOME": str(tmp / "home-fork"),
    }
    proc = run(["bash", "course/install-agents.sh"], repo, env=env)
    expected = [
        ".claude/agents/orchestrator.md",
        ".cursor/rules/onemillion-course.mdc",
        ".agents/rules/onemillion-course.md",
        ".agents/skills/tech_stack/SKILL.md",
        ".codex/config.toml",
        ".codex/agents/orchestrator.toml",
        ".opencode/agents/orchestrator.md",
        ".opencode/skills/tech_stack/SKILL.md",
        ".gemini/settings.json",
        "opencode.json",
        ".gemini/GEMINI.md",
        ".github/copilot-instructions.md",
        ".onemillion/state.json",
        ".onemillion/tooling-preflight.md",
    ]
    missing = [path for path in expected if not (repo / path).exists()]
    count_checks = {
        ".claude/agents": len(list((repo / ".claude/agents").glob("*.md"))),
        ".claude/skills": len(list((repo / ".claude/skills").glob("*/SKILL.md"))),
        ".codex/agents": len(list((repo / ".codex/agents").glob("*.toml"))),
        ".agents/skills": len(list((repo / ".agents/skills").glob("*/SKILL.md"))),
        ".opencode/agents": len(list((repo / ".opencode/agents").glob("*.md"))),
        ".opencode/skills": len(list((repo / ".opencode/skills").glob("*/SKILL.md"))),
    }
    too_few = {path: count for path, count in count_checks.items() if count < 5}
    passed = proc.returncode == 0 and not missing and not too_few
    details = proc.stdout
    if missing:
        details += "\nMissing: " + ", ".join(missing)
    if too_few:
        details += "\nToo few generated files: " + ", ".join(f"{path}={count}" for path, count in too_few.items())
    details += "\nGenerated adapter counts: " + ", ".join(f"{path}={count}" for path, count in count_checks.items())
    record(results, "installer_succeeds_in_fork_like_clone", passed, details)
    return repo


def test_day0_state(results: list[Result], repo: Path) -> None:
    state_path = repo / ".onemillion/state.json"
    try:
        state = json.loads(state_path.read_text())
        passed = (
            state.get("current_day") == 0
            and state.get("current_phase") == "preflight"
            and "simulated-learner/one-million-builders" in state.get("preflight", {}).get("origin_remote", "")
            and "siddsdixit/one-million-builders" in state.get("preflight", {}).get("upstream_remote", "")
        )
        record(results, "day0_preflight_state_created", passed, json.dumps(state, indent=2))
    except Exception as exc:
        record(results, "day0_preflight_state_created", False, str(exc))


def create_day1_project(path: Path) -> Path:
    product = path / "my-onemillion-build"
    (product / ".onemillion").mkdir(parents=True)
    (product / ".onemillion/project.json").write_text(
        json.dumps(
            {
                "product_type": "web_app",
                "idea": "Independent yoga studio owners forget to follow up with clients who do not rebook after a class. FollowUpPilot drafts approval-based rebooking messages so owners can recover missed revenue without sounding robotic.",
                "target_user": "independent yoga studio owners",
                "builder_name": "Sim Learner",
                "started_at": "2026-05-30",
            },
            indent=2,
        )
    )
    (product / ".onemillion/prd.md").write_text(
        """# FollowUpPilot PRD

## Product Summary
FollowUpPilot helps independent yoga studio owners recover missed rebookings by drafting approval-based follow-up messages.

## User And Pain Point
Independent yoga studio owners lose revenue when students attend once and do not rebook. Follow-up is manual and easy to forget.

## Unmet Need
Owners need a simple way to see who needs follow-up and send a personal message without starting from scratch.

## Data Sources And Formats
- Class attendance CSV exports
- Client names and emails
- Message notes entered by the owner

## Ideal Solution
A simple dashboard that finds missed rebooking opportunities and drafts messages for owner approval.

## Usage Moment
The owner opens it after classes each week and reviews follow-up drafts.

## User Stories
- As a yoga studio owner, I want to upload attendance data so that I can see who did not rebook.
- As a yoga studio owner, I want to review drafted messages so that I stay in control.
- As a yoga studio owner, I want to mark follow-ups sent so that I know what is complete.

## Success Criteria
An owner can identify missed rebookings, review a draft, and mark it sent.

## KPIs
- Owner creates one follow-up list.
- Owner approves one drafted message.
- Owner returns after the next class.

## Competitive Alternatives And Market Notes
Likely alternatives include spreadsheets, booking-system reports, email templates, and manual reminders. These are first-pass assumptions for Day 2 validation.

## TAM / SAM / SOM
TAM is all small service businesses that rely on repeat bookings. SAM is independent fitness and wellness studios. SOM is the first reachable set of yoga studio owners the builder can interview or contact. This is directional and must be validated.

## Assumptions To Validate On Day 2
- Owners can export or access attendance data.
- Missed rebooking follow-up is painful enough.
- Owners want approval-based drafts instead of full automation.
"""
    )
    return product


def test_day1_verifier(results: list[Result], tmp: Path) -> None:
    product = create_day1_project(tmp)
    proc = run(
        [
            "python3",
            str(REPO / "course/docs/verification/scripts/verify.py"),
            "1",
            "--project-dir",
            str(product),
            "--schema-dir",
            str(REPO / "course/docs/verification/schema"),
            "--write-report",
        ],
        REPO,
    )
    state_path = product / ".onemillion/state.json"
    state = json.loads(state_path.read_text()) if state_path.exists() else {}
    passed = proc.returncode == 0 and state.get("last_verified_day") == 1
    record(results, "day1_artifacts_pass_schema_verifier", passed, proc.stdout)


def create_day4_design_project(tmp: Path) -> Path:
    product = tmp / "day4-design-product"
    om = product / ".onemillion"
    screens = om / "screens"
    mockup = om / "mockup"
    screens.mkdir(parents=True)
    mockup.mkdir(parents=True)
    (om / "design-spec.md").write_text(
        """# Design Specification

## Design Direction
Clean operational dashboard for studio owners who need fast follow-up decisions.

## Primary User Flow
Owner opens dashboard, reviews at-risk clients, approves a follow-up, and sees a success state.

## Screens
- Dashboard
- Client detail
- Follow-up approval form

## Content States
- Loading: skeleton cards and table rows
- Empty: no at-risk clients message with import CTA
- Error: retry panel with plain-language issue
- Partial: one to three clients
- Full: seeded dashboard with trends, cards, and table
- Success: snackbar after approval

## Responsive Behavior
Mobile uses bottom navigation and one-column cards. Desktop uses sidebar navigation, data table, and split detail panel.
"""
    )
    (om / "design-system.md").write_text(
        """# Design System

## Color
MUI / Material Design 3 seed color: #0f766e.

## Typography
Heading font: Space Grotesk. Body font: Plus Jakarta Sans.

## Spacing
4, 8, 12, 16, 24, 32, 48, 64.

## Components
MUI Button, Card, Chip, Table, Drawer, TextField, Skeleton, Snackbar, Dialog.

## Motion
150ms hover, 250ms page transitions, reduced-motion support.

## Accessibility
AA contrast, focus-visible rings, labels, aria-labels for icon buttons, keyboard navigation.
"""
    )
    (om / "globals.css").write_text(":root { --md-sys-color-primary: #0f766e; }\n")
    (screens / "dashboard.md").write_text("# Dashboard\n\nLoading, Empty, Error, Partial, Full, Success states.\n")
    (screens / "client-detail.md").write_text("# Client Detail\n\nResponsive desktop split panel and mobile stacked layout.\n")
    (om / "seed-data.json").write_text(
        json.dumps(
            {
                "users": [{"name": "Maya Patel", "role": "studio owner"}],
                "clients": [{"name": "Jordan Lee", "status": "at risk"}],
            }
        )
    )
    (mockup / "index.html").write_text("<html><body><h1>Studio follow-up dashboard</h1></body></html>")
    return product


def test_day4_design_verifier(results: list[Result], tmp: Path) -> None:
    product = create_day4_design_project(tmp)
    proc = run(
        [
            "python3",
            str(REPO / "course/docs/verification/scripts/verify.py"),
            "4",
            "--project-dir",
            str(product),
            "--schema-dir",
            str(REPO / "course/docs/verification/schema"),
            "--write-report",
        ],
        REPO,
    )
    state_path = product / ".onemillion/state.json"
    state = json.loads(state_path.read_text()) if state_path.exists() else {}
    passed = proc.returncode == 0 and state.get("last_verified_day") == 4
    record(results, "day4_design_artifacts_pass_schema_verifier", passed, proc.stdout)


def create_day5_architecture_project(tmp: Path) -> Path:
    product = tmp / "day5-architecture-product"
    om = product / ".onemillion"
    sprints = om / "sprints"
    sprints.mkdir(parents=True)
    (om / "architecture.md").write_text(
        """# Architecture

## Product Type
web app, desktop-first responsive app for studio owners.

## Backend Path
Supabase-only with Next.js route handlers/server actions. FastAPI is not justified for the MVP.

## Tenancy
single-user ownership for MVP using owner_id. organization_id can be added later if studio teams become required.

## Security
Supabase Auth, Row Level Security, owner_id checks, no service role key in browser, ANTHROPIC_API_KEY server-side only, rate/cost limits for AI.

## Data Model
clients, follow_ups, messages, owner_id, created_at, updated_at, deleted_at.

## API
Next.js server actions for create/list/update/delete, JSON error format, cursor pagination.

## Frontend
Next.js, React, MUI, dashboard, client detail, follow-up approval form.

## Deployment
Vercel app plus Supabase project.

## Scalability
Designed for first 100 studio owners, thousands of clients, indexed owner_id/status/date filters, simple AI request limits.
"""
    )
    (sprints / "S0-foundation.md").write_text(
        """# Sprint S0 - Foundation

## Context
Create app shell.

## Product Decisions Used
- Product type: web app
- Backend path: Supabase + Next.js route handlers/server actions
- Tenancy model: single-user
- Security boundary: owner_id

## Frontend Tasks
Create Next.js + MUI app shell.

## Design Notes
Use dashboard screen spec.

## Acceptance Criteria
- [ ] Given the app runs, when the owner opens it, then the dashboard shell appears.

## Verification Gate
1. Run local app -> dashboard shell appears.

## Git Commit
`feat: foundation`
"""
    )
    return product


def test_day5_architecture_verifier(results: list[Result], tmp: Path) -> None:
    product = create_day5_architecture_project(tmp)
    proc = run(
        [
            "python3",
            str(REPO / "course/docs/verification/scripts/verify.py"),
            "5",
            "--project-dir",
            str(product),
            "--schema-dir",
            str(REPO / "course/docs/verification/schema"),
            "--write-report",
        ],
        REPO,
    )
    state_path = product / ".onemillion/state.json"
    state = json.loads(state_path.read_text()) if state_path.exists() else {}
    passed = proc.returncode == 0 and state.get("last_verified_day") == 5
    record(results, "day5_architecture_artifacts_pass_schema_verifier", passed, proc.stdout)


def test_day6_deployment_source_match(results: list[Result], tmp: Path) -> None:
    product = tmp / "deploy-match-product"
    (product / "app").mkdir(parents=True)
    (product / "package.json").write_text(
        json.dumps({"dependencies": {"next": "15.0.0", "react": "19.0.0", "@mui/material": "6.0.0"}})
    )
    (product / ".gitignore").write_text("node_modules\n.env.local\n")
    marker = "Hello from Sim Learner's OneMillion build"
    (product / "app/page.tsx").write_text(
        """import { Button } from '@mui/material';

"""
        f"""export default function Page() {{
  return <main><h1>{marker}</h1><p>Day 6 deployed live.</p><Button>Start</Button></main>;
}}
"""
    )
    init_fork_like_repo(product)

    web_root = tmp / "mock-deployment"
    web_root.mkdir()
    (web_root / "index.html").write_text(f"<html><body><h1>{marker}</h1><p>Day 6 deployed live.</p></body></html>")

    class Handler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(web_root), **kwargs)

        def log_message(self, format: str, *args) -> None:
            return

    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        port = sock.getsockname()[1]

    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        proc = run(
            [
                "python3",
                str(REPO / "course/docs/verification/scripts/verify.py"),
                "6",
                "--project-dir",
                str(product),
                "--schema-dir",
                str(REPO / "course/docs/verification/schema"),
                "--deployment-url",
                f"http://127.0.0.1:{port}/",
            ],
            REPO,
        )
        passed = proc.returncode == 0 and "deployment_matches_homepage_source" in proc.stdout
        record(results, "day6_deployment_source_match_verifier", passed, proc.stdout)
    finally:
        server.shutdown()


def test_manifest_paths(results: list[Result]) -> None:
    manifest = json.loads((ROOT / "course-manifest.json").read_text())
    missing: list[str] = []
    for day in manifest["days"]:
        for key in ["lesson", "build", "resources", "verifier"]:
            rel = day[key]
            if not (REPO / rel).exists():
                missing.append(rel)
    record(results, "manifest_day_paths_exist", not missing, "\n".join(missing))


def print_report(results: list[Result]) -> int:
    print("# OneMillion Course Simulation Report\n")
    passed_count = 0
    for result in results:
        icon = "PASS" if result.passed else "FAIL"
        if result.passed:
            passed_count += 1
        print(f"## {icon}: {result.name}")
        if result.details:
            details = result.details.strip()
            if len(details) > 2000:
                details = details[:2000] + "\n... [truncated]"
            print()
            print("```text")
            print(details)
            print("```")
        print()
    print(f"Summary: {passed_count}/{len(results)} checks passed.")
    return 0 if passed_count == len(results) else 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Simulate a OneMillion learner QA path")
    parser.add_argument("--keep", action="store_true", help="Keep temp simulation directory")
    args = parser.parse_args()

    results: list[Result] = []
    tmp_obj = tempfile.TemporaryDirectory(prefix="onemillion-sim-")
    tmp = Path(tmp_obj.name)
    try:
        test_course_quality(results)
        test_manifest_paths(results)
        test_installer_blocks_plain_folder(results, tmp)
        test_installer_blocks_upstream_origin(results, tmp)
        fork_repo = test_installer_succeeds_in_fork_like_clone(results, tmp)
        test_day0_state(results, fork_repo)
        test_day1_verifier(results, tmp)
        test_day4_design_verifier(results, tmp)
        test_day5_architecture_verifier(results, tmp)
        test_day6_deployment_source_match(results, tmp)
        code = print_report(results)
        if args.keep:
            print(f"Kept simulation directory: {tmp}")
            tmp_obj.cleanup = lambda: None  # type: ignore[method-assign]
        return code
    finally:
        if not args.keep:
            tmp_obj.cleanup()


if __name__ == "__main__":
    sys.exit(main())
