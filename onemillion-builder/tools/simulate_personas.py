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
    single = (ROOT / "single.md").read_text()
    subdir_agents = (ROOT / "AGENTS.md").read_text()
    agents = (REPO / "AGENTS.md").read_text()
    orchestrator = (REPO / "onemillion-agents/agents/orchestrator.md").read_text()
    teaching = (ROOT / "docs/teaching-protocol.md").read_text()
    day0 = (ROOT / "day-0-commit/README.md").read_text()
    day1 = (ROOT / "week-1-foundation/day-01-vision/build.md").read_text()
    day4 = (ROOT / "week-1-foundation/day-04-stack/build.md").read_text()
    day5 = (ROOT / "week-1-foundation/day-05-auth/build.md").read_text()
    day6 = (ROOT / "week-1-foundation/day-06-core-feature/build.md").read_text()
    day8 = (ROOT / "week-2-make-it-ai/day-08-first-ai-call/build.md").read_text()
    day10 = (ROOT / "week-2-make-it-ai/day-10-tool-use/build.md").read_text()
    day13 = (ROOT / "week-3-ship-and-sell/day-13-hygiene/build.md").read_text()
    day13_learn = (ROOT / "week-3-ship-and-sell/day-13-hygiene/learn.md").read_text()
    day14 = (ROOT / "week-3-ship-and-sell/day-14-domain/build.md").read_text()
    day15 = (ROOT / "week-3-ship-and-sell/day-15-monitoring/build.md").read_text()
    day18 = (ROOT / "week-3-ship-and-sell/day-18-demo/build.md").read_text()
    account = (ROOT / "docs/account-setup.md").read_text()
    harness_readme = (ROOT / "docs/harnesses/README.md").read_text()
    harness_docs = "\n".join(path.read_text() for path in (ROOT / "docs/harnesses").glob("*.md"))

    def missing(term: str, message: str) -> None:
        haystack = "\n".join([readme, start, single, day1, account]).lower()
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

    teaching_surface = "\n".join([agents, orchestrator, teaching, single, day0, harness_docs]).lower()
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

    day0_commitment_terms = {
        "https://www.linkedin.com/feed/": "Day 0 must provide the exact LinkedIn place to paste the public commitment.",
        "https://www.linkedin.com/in/siddharthdixit": "Day 0 must provide Sid's LinkedIn profile for tagging.",
        "https://x.com/compose/post": "Day 0 must provide the exact X composer link.",
        "copy this full linkedin post": "Day 0 must include a full copy-ready LinkedIn post.",
        "copy this full x post": "Day 0 must include a full copy-ready X post.",
        "copy this full private message": "Day 0 must include a full copy-ready private message.",
        "private message to 5 real people": "Day 0 must preserve the private commitment path.",
    }
    for term, message in day0_commitment_terms.items():
        if term not in day0_lower:
            frictions.append(message)

    provider_link_requirements = {
        "Day 4": (
            day4,
            [
                "https://github.com/signup",
                "https://github.com/new",
                "https://vercel.com/signup",
                "https://vercel.com/new",
                "https://vercel.com/docs/deployments/git",
            ],
        ),
        "Day 5": (
            day5,
            [
                "https://database.new",
                "https://supabase.com/dashboard",
                "https://vercel.com/dashboard",
                "https://vercel.com/docs/projects/environment-variables",
            ],
        ),
        "Day 8": (
            day8,
            [
                "https://console.anthropic.com/",
                "https://docs.anthropic.com/en/api/overview",
                "https://vercel.com/dashboard",
                "https://vercel.com/docs/projects/environment-variables",
            ],
        ),
        "Day 6": (day6, ["https://supabase.com/dashboard"]),
        "Day 10": (day10, ["https://supabase.com/dashboard"]),
        "Day 13": (day13 + "\n" + day13_learn, ["https://supabase.com/dashboard"]),
        "Day 14": (
            day14,
            [
                "https://vercel.com/dashboard",
                "https://vercel.com/docs/domains",
                "https://www.cloudflare.com/products/registrar/",
                "https://porkbun.com",
                "https://www.namecheap.com",
                "https://dnschecker.org",
                "https://supabase.com/dashboard",
                "https://supabase.com/docs/guides/auth/redirect-urls",
            ],
        ),
        "Day 15": (
            day15,
            [
                "https://sentry.io/signup/",
                "https://docs.sentry.io/platforms/javascript/guides/nextjs/",
                "https://vercel.com/dashboard",
                "https://vercel.com/docs/analytics",
                "https://uptimerobot.com/signUp",
                "https://help.uptimerobot.com/en/articles/11358364-how-to-create-your-first-monitor",
            ],
        ),
        "Day 18": (
            day18,
            [
                "https://www.loom.com/",
                "https://loomhelp.zendesk.com/hc/en-us/articles/360002208157-How-to-share-your-recording",
                "https://github.com/siddsdixit/teach-one-million/issues/new/choose",
                "https://www.linkedin.com/feed/",
                "https://www.linkedin.com/in/siddharthdixit",
                "https://x.com/compose/post",
            ],
        ),
    }
    for day_label, (text, urls) in provider_link_requirements.items():
        for url in urls:
            if url not in text:
                frictions.append(f"{day_label} must include exact provider link: {url}")

    landing_surface = "\n".join([readme, start, single, subdir_agents]).lower()
    landing_requirements = {
        "i am taking the onemillion course at": "Landing page must support the one-sentence harness start prompt.",
        "github signup": "Landing/start docs must guide learners who do not have GitHub yet.",
        "fork": "Landing/start docs must guide the required fork step.",
        "clone": "Landing/start docs must guide the required clone step.",
        "install": "Landing/start docs must guide the adapter/install step.",
        "single.md": "Landing/start docs must route harnesses to the full course flow.",
        "development pipeline": "Landing/start docs must frame the course around the OneMillion development pipeline.",
        "do not ask the learner to figure out the repo structure first": "Subdirectory AGENTS must tell harnesses to take over from the course URL.",
    }
    for term, message in landing_requirements.items():
        if term not in landing_surface:
            frictions.append(message)

    single_lower = single.lower()
    for term in [
        "idea -> research -> prd -> validate spec -> design -> plan -> build -> review -> test -> guard -> ship -> sell",
        "tools arrive just in time",
        "day 0: github workspace",
        "day 1: onemillion pipeline",
        "user stories",
        "use cases",
        "kpis",
    ]:
        if term not in single_lower:
            frictions.append(f"single.md missing pipeline/course-flow term: {term}")

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
