#!/usr/bin/env python3
"""
Persona-based OneMillion course simulator.

This is a Codex-friendly synthetic QA runner. It does not use real GitHub,
Vercel, Supabase, or Anthropic accounts. Instead it creates throwaway local
learner workspaces and tests whether key target personas can get through the
course entry path and Day 1 artifacts without the course contradicting itself.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

import simulate_course as core


ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
PERSONAS_PATH = ROOT / "tools" / "personas.json"


@dataclass
class PersonaResult:
    persona_id: str
    label: str
    passed: bool
    checks: list[str]
    frictions: list[str]
    artifacts: list[str]


def run(cmd: list[str], cwd: Path, timeout: int = 30) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=timeout,
    )


def load_personas(path: Path = PERSONAS_PATH) -> list[dict]:
    return json.loads(path.read_text())


def create_persona_project(persona: dict, repo: Path) -> Path:
    product_dir = repo / "my-onemillion-build"
    (product_dir / ".onemillion").mkdir(parents=True, exist_ok=True)
    (product_dir / ".onemillion" / "progress.md").write_text(
        f"""# OneMillion Progress

## Builder

- **Builder name:** {persona['name']}
- **Product name:** {persona['label']} Build
- **Target user:** {persona['target_user']}
- **Current day:** Day 1
- **Last verified day:** None

## Links

- **GitHub repo:** [add on Day 4]
- **Live URL:** [add on Day 4]
- **Supabase project:** [add on Day 5]
- **Vercel project:** [add on Day 4]
- **Demo Loom:** [add on Day 18]

## Current State

- **What works now:** Day 1 setup in progress
- **Current blocker:** None
- **Next smallest action:** Finish project.json
"""
    )
    (product_dir / ".onemillion" / "project.json").write_text(
        json.dumps(
            {
                "product_type": persona["product_type"],
                "idea": persona["idea"],
                "builder_name": persona["name"],
                "started_at": "2026-05-30",
            },
            indent=2,
        )
    )
    return product_dir


def scan_persona_friction(persona: dict) -> list[str]:
    frictions: list[str] = []
    readme = (ROOT / "README.md").read_text()
    start = (ROOT / "START-HERE.md").read_text()
    agents = (REPO / "AGENTS.md").read_text()
    orchestrator = (REPO / "onemillion-agents/agents/orchestrator.md").read_text()
    teaching = (ROOT / "docs/teaching-protocol.md").read_text()
    day0 = (ROOT / "day-0-commit/README.md").read_text()
    day1 = (ROOT / "week-1-foundation/day-01-vision/build.md").read_text()
    account = (ROOT / "docs/account-setup.md").read_text()
    harness_readme = (ROOT / "docs/harnesses/README.md").read_text()
    harness_docs = "\n".join(path.read_text() for path in (ROOT / "docs/harnesses").glob("*.md"))

    def missing(term: str, message: str) -> None:
        haystack = "\n".join([readme, start, day1, account]).lower()
        if term.lower() not in haystack:
            frictions.append(message)

    if "terminal" in persona["likely_blockers"]:
        missing("Git Bash", "Terminal-new learner needs Mac/Windows terminal naming and fallback.")
        missing("exact command", "Terminal-new learner needs exact-command reassurance.")

    if "GitHub fork/clone" in persona["likely_blockers"]:
        missing("https://github.com/signup", "GitHub-new learner needs direct signup link.")
        missing("https://github.com/siddsdixit/teach-one-million/fork", "GitHub-new learner needs direct fork link.")

    if "too many external accounts" in persona["likely_blockers"]:
        if account.count("https://") < 8:
            frictions.append("Account setup playbook may not expose enough direct setup links.")

    if "scope creep" in persona["likely_blockers"]:
        missing("exactly 3", "PM persona needs explicit MVP scope constraint visible before PRD day.")

    if "not wanting to touch deployment details" in persona["likely_blockers"]:
        missing("Vercel", "PM persona needs deployment expectation up front.")

    if "generic UI output" in persona["likely_blockers"]:
        missing("design review", "Designer persona needs visible design review/quality moment.")

    if "course feels too beginner" in persona["likely_blockers"]:
        missing("Engineers", "Engineer persona needs explicit signal that advanced builders can go deeper.")

    if "security concerns around generated code" in persona["likely_blockers"]:
        missing("security", "Engineer persona needs security/guardrail signal.")

    if "API keys and pricing anxiety" in persona["likely_blockers"]:
        missing("pricing", "Career changer needs pricing/cost anxiety addressed or linked.")
        missing("API key", "Career changer needs API-key setup surfaced.")

    if "getting stuck alone" in persona["likely_blockers"]:
        missing("Recover Your Place", "Career changer needs recovery path visible.")

    if re.search(r"\bcd ~\b", day1):
        frictions.append("Day 1 tells learners to create product folder in home directory; course orchestrator expects product_dir in/near the course repo.")

    if "my-onemillion-build" not in start:
        frictions.append("Start guide does not make the product workspace relationship obvious.")

    if "git clone https://github.com/siddsdixit/teach-one-million.git" in harness_readme:
        frictions.append("Harness README tells learners to clone upstream instead of their fork.")

    if re.search(r"start Day 1", harness_docs, flags=re.IGNORECASE):
        frictions.append("Harness docs skip the mandatory Day 0 preflight.")

    teaching_surface = "\n".join([agents, orchestrator, teaching, day0, harness_docs]).lower()
    required_teaching_terms = {
        "proper greeting": "Harness teaching protocol must require a proper greeting.",
        "explain the course": "Harness teaching protocol must explain what the course is before assigning work.",
        "ai/human contract": "Harness teaching protocol must explain the AI/human contract.",
        "copy-ready": "Harness teaching protocol must provide copy-ready learner actions.",
        "what counts as done": "Harness teaching protocol must define the completion gate in learner language.",
        "do not give bare task assignments": "Harness teaching protocol must ban bare 'do Day X' assignments.",
    }
    for term, message in required_teaching_terms.items():
        if term not in teaching_surface:
            frictions.append(message)

    day0_lower = day0.lower()
    for term in ["welcome to onemillion", "what this course is", "today is day 0", "what counts as done for day 0"]:
        if term not in day0_lower:
            frictions.append(f"Day 0 opening script missing required teaching phrase: {term}")

    return frictions


def simulate_persona(persona: dict, tmp: Path) -> PersonaResult:
    persona_root = tmp / persona["id"]
    repo = persona_root / "course"
    core.copy_repo(repo)
    core.init_fork_like_repo(repo)

    fake_bin = persona_root / "fake-gh-off"
    fake_bin.mkdir(parents=True)
    core.create_fake_gh_bin(fake_bin, authenticated=False)
    env = {"PATH": f"{fake_bin}:{os.environ['PATH']}"}
    install = core.run(["bash", "onemillion-builder/install-agents.sh"], repo, env=env)

    checks: list[str] = []
    artifacts: list[str] = []
    passed = True

    if install.returncode == 0:
        checks.append("installer passed in fork-like clone")
    else:
        checks.append("installer failed in fork-like clone")
        passed = False

    state_path = repo / ".onemillion/state.json"
    if state_path.exists():
        state = json.loads(state_path.read_text())
        if state.get("current_day") == 0 and state.get("product_dir") == "my-onemillion-build":
            checks.append("Day 0 state created with product_dir")
            artifacts.append(str(state_path.relative_to(repo)))
        else:
            checks.append("Day 0 state shape is wrong")
            passed = False
    else:
        checks.append("Day 0 state missing")
        passed = False

    claude_command = repo / ".claude/commands/onemillion.md"
    if claude_command.exists():
        checks.append("Claude /onemillion command adapter installed")
        artifacts.append(str(claude_command.relative_to(repo)))
    else:
        checks.append("Claude /onemillion command adapter missing")
        passed = False

    product = create_persona_project(persona, repo)
    verify = run(
        [
            "python3",
            str(REPO / "onemillion-builder/docs/verification/scripts/verify.py"),
            "1",
            "--project-dir",
            str(product),
            "--schema-dir",
            str(REPO / "onemillion-builder/docs/verification/schema"),
            "--write-report",
        ],
        REPO,
    )
    if verify.returncode == 0:
        checks.append("Day 1 schema verifier passed")
        artifacts.append(str((product / ".onemillion/project.json").relative_to(repo)))
        artifacts.append(str((product / ".onemillion/verification-day-01.md").relative_to(repo)))
    else:
        checks.append("Day 1 schema verifier failed")
        passed = False

    frictions = scan_persona_friction(persona)
    if frictions:
        passed = False

    return PersonaResult(
        persona_id=persona["id"],
        label=f"{persona['name']} - {persona['label']}",
        passed=passed,
        checks=checks,
        frictions=frictions,
        artifacts=artifacts,
    )


def render_report(results: list[PersonaResult]) -> str:
    passed = sum(1 for result in results if result.passed)
    lines = [
        "# Persona Course Simulation Report",
        "",
        f"Summary: {passed}/{len(results)} personas passed without unresolved friction.",
        "",
    ]
    for result in results:
        status = "PASS" if result.passed else "NEEDS ATTENTION"
        lines.extend(
            [
                f"## {status}: {result.label}",
                "",
                "Checks:",
            ]
        )
        lines.extend(f"- {check}" for check in result.checks)
        if result.artifacts:
            lines.append("")
            lines.append("Artifacts created:")
            lines.extend(f"- `{artifact}`" for artifact in result.artifacts)
        if result.frictions:
            lines.append("")
            lines.append("Friction found:")
            lines.extend(f"- {friction}" for friction in result.frictions)
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run persona-based OneMillion course simulation")
    parser.add_argument("--personas", default=str(PERSONAS_PATH), help="Path to personas.json")
    parser.add_argument("--report", default="", help="Optional path to write markdown report")
    parser.add_argument("--keep", action="store_true", help="Keep temp simulation directory")
    args = parser.parse_args()

    tmp_obj = tempfile.TemporaryDirectory(prefix="onemillion-personas-")
    tmp = Path(tmp_obj.name)
    try:
        results = [simulate_persona(persona, tmp) for persona in load_personas(Path(args.personas))]
        report = render_report(results)
        print(report)
        if args.report:
            Path(args.report).write_text(report)
        if args.keep:
            print(f"Kept simulation directory: {tmp}")
            tmp_obj.cleanup = lambda: None  # type: ignore[method-assign]
        return 0 if all(result.passed for result in results) else 1
    finally:
        if not args.keep:
            tmp_obj.cleanup()


if __name__ == "__main__":
    sys.exit(main())
