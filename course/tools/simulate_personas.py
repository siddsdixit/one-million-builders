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


@dataclass
class DayMatrixResult:
    persona_id: str
    label: str
    day: int
    day_dir: str
    passed: bool
    checks: list[str]
    frictions: list[str]


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


def day_dirs() -> list[tuple[int, Path]]:
    dirs: list[tuple[int, Path]] = [(0, ROOT / "days/day-00-orientation")]
    for path in sorted((ROOT / "days").glob("day-[0-9][0-9]-*")):
        day = int(path.name.split("-", 2)[1])
        if day != 0:
            dirs.append((day, path))
    return dirs


def read_day_surface(path: Path) -> str:
    parts: list[str] = []
    for name in ["README.md", "learn.md", "build.md", "stuck.md", "resources.md", "loom.md"]:
        file = path / name
        if file.exists():
            parts.append(file.read_text())
    return "\n".join(parts)


def has_any(text: str, terms: list[str]) -> bool:
    lower = text.lower()
    return any(term.lower() in lower for term in terms)


def simulate_persona_day(persona: dict, day: int, path: Path) -> DayMatrixResult:
    text = read_day_surface(path)
    lower = text.lower()
    checks: list[str] = []
    frictions: list[str] = []

    def require(condition: bool, check: str, friction: str) -> None:
        if condition:
            checks.append(check)
        else:
            frictions.append(friction)

    require((path / "README.md").exists(), "day README exists", "missing day README cockpit")
    require((path / "stuck.md").exists(), "stuck guide exists", "missing day stuck guide")
    if day > 0:
        for name in ["learn.md", "build.md", "resources.md", "loom.md"]:
            require((path / name).exists(), f"{name} exists", f"missing {name}")
        require("teach me" in lower or "plain language" in lower, "plain-language tutor prompt present", "missing plain-language tutor instruction")
        require("do not advance" in lower or "completion gate" in lower, "completion gate guard present", "missing completion-gate guard")
    else:
        require("welcome" in lower and "day 0" in lower, "welcome orientation present", "missing Day 0 welcome orientation")

    blockers = set(persona.get("likely_blockers", []))
    criteria = set(persona.get("success_criteria", []))

    if "terminal vocabulary" in blockers:
        if day in {0, 1, 6, 7, 12}:
            require(
                has_any(text, ["exact command", "copy", "paste", "recover", "stuck"]),
                "terminal-new learner support present",
                "terminal-new learner needs exact copy/paste or recovery support",
            )

    if "GitHub fork/clone" in blockers:
        if day == 0:
            require(has_any(text, ["fork", "clone", "github"]), "GitHub fork/clone support present", "Day 0 lacks GitHub fork/clone guidance")
        if day == 6:
            require("github" in lower and "vercel" in lower, "GitHub-to-Vercel deploy support present", "Day 6 lacks GitHub/Vercel deploy guidance")

    if "too many external accounts" in blockers:
        if day in {6, 7, 12, 16, 18}:
            require(
                has_any(text, ["account-setup", "exact", "https://"]),
                "external-account setup support present",
                "external-account day needs exact link or account setup playbook",
            )

    if "fear of breaking things" in blockers or "getting stuck alone" in blockers or "imposter syndrome" in blockers:
        require(
            "stuck" in lower or "recover" in lower,
            "recovery path present",
            "learner needs a visible recovery path",
        )

    if "scope creep" in blockers or "clear scope locks" in criteria:
        if day in {1, 2, 3, 5, 8, 11, 12}:
            require(
                has_any(text, ["mvp", "scope", "ignore today", "one useful", "do not add"]),
                "scope-control language present",
                "scope-sensitive persona needs explicit scope control",
            )

    if "not wanting to touch deployment details" in blockers:
        if day in {6, 16}:
            require("vercel" in lower and has_any(text, ["live", "deploy"]), "deployment path explicit", "deployment-heavy day needs explicit Vercel/live path")

    if "generic UI output" in blockers or "unclear visual quality bar" in blockers or "feeling the app is too ugly to share" in blockers:
        if day in {4, 13, 18}:
            require(
                has_any(text, ["mui", "design", "mockup", "polish", "screens", "visual"]),
                "design quality support present",
                "design-sensitive persona needs visible design quality support",
            )

    if "course feels too beginner" in blockers or "wants to skip gates" in blockers:
        require(
            has_any(text, ["verify", "completion gate", "quality", "architecture", "guard"]),
            "verification rigor present",
            "experienced learner needs visible rigor or verification",
        )

    if "security concerns around generated code" in blockers:
        if day in {5, 7, 10, 11, 12, 14, 15, 16}:
            require(
                has_any(text, ["security", "rls", "secret", "privacy", "auth"]),
                "security guardrail present",
                "security-sensitive persona needs security/auth/privacy guardrails",
            )

    if "API keys and pricing anxiety" in blockers:
        if day in {11, 12, 15}:
            require(has_any(text, ["api key", "secret", "cost", "pricing"]), "API key/cost support present", "API-key anxious persona needs key and cost guidance")

    if "confidentiality" in persona.get("id", "") or "confidential" in persona.get("background", "").lower():
        if day in {5, 7, 10, 11, 12, 14, 16}:
            require(
                has_any(text, ["private", "privacy", "rls", "redact", "redaction", "secret", "approval"]),
                "confidential-data boundary present",
                "confidential EA needs privacy/RLS/redaction/approval boundary",
            )
        if day in {11, 12}:
            require(
                has_any(text, ["redact", "redaction"]) and has_any(text, ["approve", "approval", "review"]),
                "AI redaction and approval support present",
                "confidential EA needs explicit AI redaction and approval support",
            )

    if "assistant" in persona.get("target_user", "").lower() or "assistant" in persona.get("background", "").lower():
        if day in {1, 2, 4, 8, 11, 12, 17}:
            require(
                has_any(text, ["approval", "review", "draft", "send", "follow-up", "assistant", "workflow"]),
                "assistant workflow language present",
                "assistant persona needs draft/review/follow-up workflow language",
            )

    return DayMatrixResult(
        persona_id=persona["id"],
        label=f"{persona['name']} - {persona['label']}",
        day=day,
        day_dir=str(path.relative_to(ROOT)),
        passed=not frictions,
        checks=checks,
        frictions=frictions,
    )


def simulate_persona_day_matrix(personas: list[dict]) -> list[DayMatrixResult]:
    results: list[DayMatrixResult] = []
    for persona in personas:
        for day, path in day_dirs():
            results.append(simulate_persona_day(persona, day, path))
    return results


def render_day_matrix_report(results: list[DayMatrixResult]) -> str:
    passed = sum(1 for result in results if result.passed)
    by_persona: dict[str, list[DayMatrixResult]] = {}
    for result in results:
        by_persona.setdefault(result.label, []).append(result)

    lines = [
        "# Persona Day-By-Day Simulation Report",
        "",
        f"Summary: {passed}/{len(results)} persona-day checks passed.",
        "",
        "This is a synthetic course-surface matrix. It checks every persona against Day 0-18 learner materials for setup clarity, recovery paths, scope control, account guidance, security/privacy guardrails, and persona-specific friction. It does not create real GitHub, Vercel, Supabase, Loom, or AI-provider accounts.",
        "",
    ]
    for label, persona_results in by_persona.items():
        persona_passed = sum(1 for result in persona_results if result.passed)
        lines.extend([f"## {label}", "", f"Persona summary: {persona_passed}/{len(persona_results)} days passed.", ""])
        for result in persona_results:
            status = "PASS" if result.passed else "NEEDS ATTENTION"
            lines.append(f"- Day {result.day}: {status} (`{result.day_dir}`)")
            if result.frictions:
                for friction in result.frictions:
                    lines.append(f"  - {friction}")
        lines.append("")
    return "\n".join(lines)


def create_persona_project(persona: dict, repo: Path) -> Path:
    product_dir = repo / "my-onemillion-build"
    (product_dir / ".onemillion").mkdir(parents=True, exist_ok=True)
    (product_dir / ".onemillion" / "project.json").write_text(
        json.dumps(
            {
                "product_type": persona["product_type"],
                "idea": persona["idea"],
                "target_user": persona["target_user"],
                "builder_name": persona["name"],
                "started_at": "2026-05-30",
            },
            indent=2,
        )
    )
    (product_dir / ".onemillion" / "prd.md").write_text(
        f"""# {persona['label']} Build PRD

## Product Summary
{persona['idea']}

## User And Pain Point
The primary user is {persona['target_user']}. The pain is a repeated workflow that is currently handled manually.

## Unmet Need
The user needs a simpler way to capture context, see what matters, and complete the next action.

## Data Sources And Formats
- User-entered notes
- Spreadsheet rows
- Copied email or message text

## Ideal Solution
A focused product that organizes the workflow and produces reviewable next actions.

## Usage Moment
The user opens the product when the workflow becomes painful and uses it to decide what to do next.

## User Stories
- As a {persona['target_user']}, I want to capture the work in one place so that I do not lose track.
- As a {persona['target_user']}, I want to see what needs attention so that I can act quickly.
- As a {persona['target_user']}, I want to review suggested next steps so that I stay in control.

## Success Criteria
The user can complete the core workflow from capture to action in one session.

## KPIs
- User creates 3+ records in first session.
- User completes one core workflow.
- User returns the next week.

## Competitive Alternatives And Market Notes
Likely alternatives include spreadsheets, notes apps, email flags, and manual reminders. These are first-pass assumptions for Day 2 validation.

## TAM / SAM / SOM
TAM is everyone with the broad workflow pain. SAM is the reachable segment matching this user profile. SOM is the first small audience the builder can personally reach. These are directional assumptions for Day 2.

## Assumptions To Validate On Day 2
- The pain is frequent enough.
- The data sources are available.
- The user will try a focused product.
"""
    )
    return product_dir


def scan_persona_friction(persona: dict) -> list[str]:
    frictions: list[str] = []
    readme = (ROOT / "README.md").read_text()
    start = (ROOT / "START-HERE.md").read_text()
    single = (ROOT / "days/single.md").read_text()
    subdir_agents = (ROOT / "AGENTS.md").read_text()
    agents = (REPO / "AGENTS.md").read_text()
    orchestrator = (REPO / "course/agents/agents/orchestrator.md").read_text()
    teaching = (ROOT / "docs/teaching-protocol.md").read_text()
    day0 = (ROOT / "days/day-00-orientation/README.md").read_text()
    day1 = (ROOT / "days/day-01-idea/build.md").read_text()
    day4 = (ROOT / "days/day-04-design/build.md").read_text()
    day5 = (ROOT / "days/day-05-plan-architecture/build.md").read_text()
    day6 = (ROOT / "days/day-06-app-shell/build.md").read_text()
    day7 = (ROOT / "days/day-07-auth-db/build.md").read_text()
    day8 = (ROOT / "days/day-08-core-build/build.md").read_text()
    day10 = (ROOT / "days/day-10-qa-tests/build.md").read_text()
    day12 = (ROOT / "days/day-12-first-ai-build/build.md").read_text()
    day13 = (ROOT / "days/day-13-product-polish/build.md").read_text()
    day13_learn = (ROOT / "days/day-13-product-polish/learn.md").read_text()
    day14 = (ROOT / "days/day-14-security-trust-review/build.md").read_text()
    day15 = (ROOT / "days/day-15-qa-production-readiness/build.md").read_text()
    day16 = (ROOT / "days/day-16-ship-production/build.md").read_text()
    day18 = (ROOT / "days/day-18-demo/build.md").read_text()
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
        missing("https://github.com/siddsdixit/one-million-builders/fork", "GitHub-new learner needs direct fork link.")

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

    if "git clone https://github.com/siddsdixit/one-million-builders.git" in harness_readme:
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
        "Day 6": (
            day6,
            [
                "https://github.com/signup",
                "https://github.com/new",
                "https://vercel.com/signup",
                "https://vercel.com/new",
                "https://vercel.com/docs/deployments/git",
            ],
        ),
        "Day 7": (
            day7,
            [
                "https://database.new",
                "https://supabase.com/dashboard",
                "https://vercel.com/dashboard",
                "https://vercel.com/docs/projects/environment-variables",
            ],
        ),
        "Day 8": (day8, ["https://supabase.com/dashboard"]),
        "Day 12": (
            day12,
            [
                "https://console.anthropic.com/",
                "https://docs.anthropic.com/en/api/overview",
                "https://vercel.com/dashboard",
                "https://vercel.com/docs/projects/environment-variables",
            ],
        ),
        "Day 10": (day10, ["https://vercel.com/dashboard", "https://supabase.com/dashboard"]),
        "Day 13": (day13 + "\n" + day13_learn, ["https://supabase.com/dashboard"]),
        "Day 14": (
            day14,
            [
                "https://supabase.com/dashboard",
                "https://supabase.com/docs/guides/database/postgres/row-level-security",
            ],
        ),
        "Day 15": (
            day15,
            [
                "https://supabase.com/dashboard",
                "https://vercel.com/dashboard",
                "https://console.anthropic.com/",
            ],
        ),
        "Day 16": (
            day16,
            [
                "https://vercel.com/dashboard",
                "https://vercel.com/docs/domains",
                "https://www.cloudflare.com/products/registrar/",
                "https://porkbun.com",
                "https://www.namecheap.com",
                "https://dnschecker.org",
                "https://sentry.io/signup/",
                "https://docs.sentry.io/platforms/javascript/guides/nextjs/",
                "https://vercel.com/dashboard",
                "https://vercel.com/docs/analytics",
                "https://dashboard.uptimerobot.com/login",
                "https://help.uptimerobot.com/en/articles/11358364-how-to-create-your-first-monitor",
            ],
        ),
        "Day 18": (
            day18,
            [
                "https://www.loom.com/",
                "https://loomhelp.zendesk.com/hc/en-us/articles/360002208157-How-to-share-your-recording",
                "https://github.com/siddsdixit/one-million-builders/issues/new/choose",
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
        "day 0: orientation",
        "day 1: idea agent",
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
    env = {
        "PATH": f"{fake_bin}:{os.environ['PATH']}",
        "ONEMILLION_SKIP_TOOL_INSTALL": "1",
        "ONEMILLION_INSTALL_GLOBAL_ADAPTERS": "0",
        "HOME": str(persona_root / "home"),
    }
    install = core.run(["bash", "course/install-agents.sh"], repo, env=env)

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
    if verify.returncode == 0:
        checks.append("Day 1 schema verifier passed")
        artifacts.append(str((product / ".onemillion/project.json").relative_to(repo)))
        artifacts.append(str((product / ".onemillion/prd.md").relative_to(repo)))
        artifacts.append(str((product / ".onemillion/state.json").relative_to(repo)))
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
    parser.add_argument("--all-days", action="store_true", help="Run every persona against Day 0-18 learner surfaces")
    parser.add_argument("--keep", action="store_true", help="Keep temp simulation directory")
    args = parser.parse_args()

    personas = load_personas(Path(args.personas))
    if args.all_days:
        results = simulate_persona_day_matrix(personas)
        report = render_day_matrix_report(results)
        print(report)
        if args.report:
            Path(args.report).write_text(report)
        return 0 if all(result.passed for result in results) else 1

    tmp_obj = tempfile.TemporaryDirectory(prefix="onemillion-personas-")
    tmp = Path(tmp_obj.name)
    try:
        results = [simulate_persona(persona, tmp) for persona in personas]
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
