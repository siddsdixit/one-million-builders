"""
OneMillion Course Verification CLI

Usage:
    python verify.py day-X [--project-dir /path/to/project]

This is the automated portion of verification. It checks local artifacts, code
patterns, deployment URLs, and deployment/source matches where schemas define them.
For judgment-heavy quality checks, use the coding harness verifier too.

This script can update the orchestrator-owned `.onemillion/state.json` with `--write-report`.
"""

import json
import os
import re
import sys
import argparse
import datetime as dt
import html
import subprocess
import urllib.request
import glob as glob_module
from pathlib import Path
from typing import Any


# ANSI colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def normalize_text(text: str) -> str:
    text = html.unescape(text)
    text = re.sub(r"<script\b[^>]*>.*?</script>", " ", text, flags=re.I | re.S)
    text = re.sub(r"<style\b[^>]*>.*?</style>", " ", text, flags=re.I | re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip().lower()


def resolve_url(check: dict, builder_inputs: dict) -> str | None:
    url = None
    if check.get("url_source") == "ask_builder":
        url = builder_inputs.get("vercel_url")
    elif check.get("url_source") == "build_from_vercel_base":
        base = builder_inputs.get("vercel_url")
        if base:
            url = base.rstrip("/") + check.get("path_suffix", "")
    elif check.get("url"):
        url = check["url"]
    if url and not re.match(r"^https?://", url):
        url = "https://" + url
    return url


def fetch_url(url: str, method: str = "GET") -> tuple[int, str, str]:
    req = urllib.request.Request(
        url,
        method=method,
        headers={
            "User-Agent": "OneMillionVerifier/1.0",
            "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
        },
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        raw = resp.read(1_000_000)
        charset = resp.headers.get_content_charset() or "utf-8"
        return resp.status, resp.url, raw.decode(charset, errors="replace")


def candidate_files(check: dict, project_dir: Path) -> list[Path]:
    files: list[Path] = []
    if "path" in check:
        files.append(project_dir / check["path"])
    if "path_pattern" in check:
        files.extend(Path(p) for p in glob_module.glob(str(project_dir / check["path_pattern"]), recursive=True))
    for pattern in check.get("source_globs", []):
        files.extend(Path(p) for p in glob_module.glob(str(project_dir / pattern), recursive=True))
    for path in check.get("source_paths", []):
        files.append(project_dir / path)

    excluded = {str((project_dir / p).resolve()) for p in check.get("exclude", [])}
    unique: list[Path] = []
    seen: set[str] = set()
    for file in files:
        resolved = str(file.resolve())
        if resolved in seen or resolved in excluded or not file.exists() or not file.is_file():
            continue
        seen.add(resolved)
        unique.append(file)
    return unique


def extract_source_markers(paths: list[Path]) -> list[str]:
    markers: list[str] = []
    seen: set[str] = set()
    blocked_fragments = [
        "className",
        "import ",
        "export ",
        "use client",
        "http://",
        "https://",
        "node_modules",
        "NEXT_PUBLIC_",
        "process.env",
    ]
    string_re = re.compile(r'"([^"\n]{6,120})"|\'([^\'\n]{6,120})\'|`([^`]{6,160})`')
    jsx_text_re = re.compile(r">([^<>{}\n]{8,120})<")

    for path in paths:
        text = read_text(path)
        candidates: list[str] = []
        for match in string_re.findall(text):
            candidates.append(next(part for part in match if part))
        candidates.extend(jsx_text_re.findall(text))

        for raw in candidates:
            marker = re.sub(r"\s+", " ", raw).strip()
            if not marker:
                continue
            if any(fragment in marker for fragment in blocked_fragments):
                continue
            if len(marker) < 8 or not re.search(r"[A-Za-z]", marker):
                continue
            if not (" " in marker or len(marker) >= 14):
                continue
            if re.fullmatch(r"[A-Za-z0-9_./:-]+", marker):
                continue
            key = marker.lower()
            if key not in seen:
                seen.add(key)
                markers.append(marker)
    return markers


def check_file_exists(check: dict, project_dir: Path) -> tuple[bool, str]:
    path = project_dir / check["path"]
    if path.exists():
        return True, f"Found: {check['path']}"
    return False, f"Missing: {check['path']}"


def check_valid_json(check: dict, project_dir: Path) -> tuple[bool, str]:
    path = project_dir / check["path"]
    if not path.exists():
        return False, f"File missing: {check['path']}"
    try:
        with open(path) as f:
            json.load(f)
        return True, f"Valid JSON: {check['path']}"
    except json.JSONDecodeError as e:
        return False, f"Invalid JSON in {check['path']}: {e}"


def check_json_field(check: dict, project_dir: Path) -> tuple[bool, str]:
    path = project_dir / check["path"]
    if not path.exists():
        return False, f"File missing: {check['path']}"
    try:
        with open(path) as f:
            data = json.load(f)
        value = data.get(check["field"])
        if "allowed_values" in check:
            if value in check["allowed_values"]:
                return True, f"{check['field']}={value} (valid)"
            return False, f"{check['field']}={value} (must be one of {check['allowed_values']})"
        return False, "No validation rule"
    except Exception as e:
        return False, f"Error: {e}"


def check_json_field_min_length(check: dict, project_dir: Path) -> tuple[bool, str]:
    path = project_dir / check["path"]
    if not path.exists():
        return False, f"File missing: {check['path']}"
    try:
        with open(path) as f:
            data = json.load(f)
        value = data.get(check["field"], "")
        if len(value) >= check["min_length"]:
            return True, f"{check['field']} is {len(value)} chars (>={check['min_length']})"
        return False, f"{check['field']} is {len(value)} chars, needs {check['min_length']}+"
    except Exception as e:
        return False, f"Error: {e}"


def check_json_field_not_placeholder(check: dict, project_dir: Path) -> tuple[bool, str]:
    path = project_dir / check["path"]
    if not path.exists():
        return False, f"File missing: {check['path']}"
    try:
        data = json.loads(read_text(path))
        value = str(data.get(check["field"], "")).strip()
        blocked = {str(v).strip().lower() for v in check.get("blocked_values", [])}
        if value and value.lower() not in blocked:
            return True, f"{check['field']} is set"
        return False, f"{check['field']} is placeholder/empty"
    except Exception as e:
        return False, f"Error: {e}"


def check_json_field_iso_date(check: dict, project_dir: Path) -> tuple[bool, str]:
    path = project_dir / check["path"]
    if not path.exists():
        return False, f"File missing: {check['path']}"
    try:
        data = json.loads(read_text(path))
        value = str(data.get(check["field"], "")).strip()
        dt.date.fromisoformat(value[:10])
        return True, f"{check['field']} has ISO date: {value}"
    except Exception as e:
        return False, f"{check['field']} is not an ISO date: {e}"


def check_json_field_contains(check: dict, project_dir: Path) -> tuple[bool, str]:
    path = project_dir / check["path"]
    if not path.exists():
        return False, f"File missing: {check['path']}"
    try:
        data = json.loads(read_text(path))
        value = data.get(check["field"], {})
        if not isinstance(value, dict):
            return False, f"{check['field']} is not an object"
        missing = [key for key in check.get("required_keys", []) if key not in value]
        if not missing:
            return True, f"{check['field']} contains required keys"
        return False, f"{check['field']} missing keys: {missing}"
    except Exception as e:
        return False, f"Error: {e}"


def check_file_exists_glob(check: dict, project_dir: Path) -> tuple[bool, str]:
    patterns = check["patterns"]
    found = []
    excluded = {str((project_dir / p).resolve()) for p in check.get("exclude", [])}
    for pattern in patterns:
        matches = glob_module.glob(str(project_dir / pattern), recursive=True)
        found.extend(match for match in matches if str(Path(match).resolve()) not in excluded)
    min_count = check.get("min_match_count", 1)
    if len(found) >= min_count:
        return True, f"Found {len(found)} matching files"
    return False, f"Need {min_count}+ matching files (found {len(found)})"


def check_directory_exists(check: dict, project_dir: Path) -> tuple[bool, str]:
    path = project_dir / check["path"]
    if path.is_dir():
        return True, f"Directory exists: {check['path']}"
    return False, f"Directory missing: {check['path']}"


def check_file_contains(check: dict, project_dir: Path) -> tuple[bool, str]:
    path = project_dir / check.get("path", "")
    if "path_pattern" in check:
        # Glob for matching files
        matches = glob_module.glob(str(project_dir / check["path_pattern"]), recursive=True)
        if not matches:
            return False, f"No files matching {check['path_pattern']}"
        path = Path(matches[0])

    if not path.exists():
        return False, f"File missing: {path}"

    content = read_text(path)
    required = check.get("required_strings", [])
    missing = [s for s in required if s not in content]
    any_of = check.get("any_of_strings", [])
    matched_any = [s for s in any_of if s in content]
    if missing:
        return False, f"Missing in {path.name}: {missing}"
    if any_of and not matched_any:
        return False, f"Missing one of these in {path.name}: {any_of}"
    if any_of:
        return True, f"Required strings present in {path.name}; matched one of {matched_any}"
    return True, f"All required strings present in {path.name}"


def check_file_not_contains(check: dict, project_dir: Path) -> tuple[bool, str]:
    path = project_dir / check["path"]
    if not path.exists():
        return False, f"File missing: {check['path']}"
    content = read_text(path)
    blocked = check.get("blocked_strings", [])
    found_blocked = [s for s in blocked if s in content]
    if found_blocked:
        return False, f"Should not contain: {found_blocked}"
    return True, "No blocked strings found"


def check_regex_count(check: dict, project_dir: Path) -> tuple[bool, str]:
    path = project_dir / check["path"]
    if not path.exists():
        return False, f"File missing: {check['path']}"
    content = read_text(path)
    matches = re.findall(check["pattern"], content)
    exact = check.get("exact_count")
    min_count = check.get("min_count")
    if exact is not None:
        if len(matches) == exact:
            return True, f"Found exactly {exact} matches"
        return False, f"Found {len(matches)} matches (need exactly {exact})"
    if min_count is not None:
        if len(matches) >= min_count:
            return True, f"Found {len(matches)} matches (>={min_count})"
        return False, f"Found {len(matches)} matches (need {min_count}+)"
    return False, "No count rule specified"


def check_markdown_section_count(check: dict, project_dir: Path) -> tuple[bool, str]:
    path = project_dir / check["path"]
    if not path.exists():
        return False, f"File missing: {check['path']}"
    content = read_text(path)
    pattern = check["section_pattern"]
    count = content.count(pattern)
    min_count = check.get("min_count", 1)
    if count >= min_count:
        return True, f"Found {count} sections matching '{pattern}'"
    return False, f"Found {count} sections, need {min_count}+"


def check_markdown_required_sections(check: dict, project_dir: Path) -> tuple[bool, str]:
    path = project_dir / check["path"]
    if not path.exists():
        return False, f"File missing: {check['path']}"
    content = read_text(path).lower()
    missing = []
    for heading in check.get("required_headings", []):
        if not re.search(rf"^#+\s+.*{re.escape(heading.lower())}", content, flags=re.M):
            missing.append(heading)
    if not missing:
        return True, "Required markdown sections present"
    return False, f"Missing headings: {missing}"


def check_markdown_section_bullet_count(check: dict, project_dir: Path) -> tuple[bool, str]:
    path = project_dir / check["path"]
    if not path.exists():
        return False, f"File missing: {check['path']}"
    content = read_text(path)
    heading = check["section_heading_contains"]
    match = re.search(rf"^#+\s+.*{re.escape(heading)}.*$", content, flags=re.I | re.M)
    if not match:
        return False, f"Section not found: {heading}"
    rest = content[match.end():]
    next_heading = re.search(r"^#+\s+", rest, flags=re.M)
    section = rest[: next_heading.start()] if next_heading else rest
    bullet_count = len(re.findall(r"^\s*[-*]\s+", section, flags=re.M))
    min_bullets = check.get("min_bullets", 1)
    if bullet_count >= min_bullets:
        return True, f"Found {bullet_count} bullets in {heading}"
    return False, f"Found {bullet_count} bullets in {heading}, need {min_bullets}+"


def check_markdown_section_field(check: dict, project_dir: Path) -> tuple[bool, str]:
    path = project_dir / check["path"]
    if not path.exists():
        return False, f"File missing: {check['path']}"
    content = read_text(path)
    sections = re.split(rf"(?=^{re.escape(check['section_pattern'])})", content, flags=re.M)
    sections = [section for section in sections if section.startswith(check["section_pattern"])]
    if not sections:
        return False, f"No sections matching {check['section_pattern']}"
    required = check.get("required_subsection") or check.get("required_text")
    missing = [index + 1 for index, section in enumerate(sections) if required not in section]
    if not missing:
        return True, f"{required!r} present in {len(sections)} sections"
    return False, f"{required!r} missing in sections: {missing}"


def check_shell_command(check: dict, project_dir: Path) -> tuple[bool, str]:
    try:
        result = subprocess.run(
            check["command"],
            cwd=project_dir,
            shell=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=check.get("timeout_seconds", 10),
        )
    except Exception as e:
        return False, f"Command failed: {e}"
    output = result.stdout.strip()
    if result.returncode != 0:
        return False, f"Command exited {result.returncode}: {output[:300]}"
    pattern = check.get("expected_pattern")
    if pattern and not re.search(pattern, output):
        return False, f"Output did not match {pattern!r}: {output[:300]}"
    return True, output[:300] or "Command passed"


def check_http(check: dict, project_dir: Path, builder_inputs: dict) -> tuple[bool, str]:
    url = resolve_url(check, builder_inputs)
    if not url:
        return False, "Vercel URL not provided (use --vercel-url flag)"
    try:
        try:
            status, final_url, body = fetch_url(url, "GET")
        except Exception:
            status, final_url, body = fetch_url(url, "HEAD")
        if status in check["expected_status"]:
            evidence = f"{final_url} -> {status}"
            if body:
                evidence += f", fetched {len(body)} chars"
            return True, evidence
        return False, f"{final_url} -> {status} (expected {check['expected_status']})"
    except Exception as e:
        return False, f"{url} -> error: {e}"


def check_deployment_matches_source(check: dict, project_dir: Path, builder_inputs: dict) -> tuple[bool, str]:
    url = resolve_url(check, builder_inputs)
    if not url:
        return False, "Vercel URL not provided (use --vercel-url flag)"

    sources = candidate_files(check, project_dir)
    if not sources:
        return False, "No source files found to compare against deployment"

    markers = check.get("required_strings") or extract_source_markers(sources)
    if not markers:
        return False, "No meaningful local source markers found"

    try:
        status, final_url, body = fetch_url(url, "GET")
    except Exception as e:
        return False, f"{url} -> error: {e}"

    if status not in check.get("expected_status", [200, 304]):
        return False, f"{final_url} -> {status} (expected {check.get('expected_status', [200, 304])})"

    normalized_body = normalize_text(body)
    matched = []
    for marker in markers:
        if normalize_text(marker) in normalized_body:
            matched.append(marker)

    min_count = check.get("min_marker_count", 1)
    if len(matched) >= min_count:
        shown = "; ".join(matched[:3])
        return True, f"Deployment matches local source marker(s): {shown}"

    sample = "; ".join(markers[:5])
    return False, f"Deployment did not show enough local source markers. Checked examples: {sample}"


CHECK_HANDLERS = {
    "file_exists": check_file_exists,
    "valid_json": check_valid_json,
    "json_field": check_json_field,
    "json_field_min_length": check_json_field_min_length,
    "file_exists_glob": check_file_exists_glob,
    "directory_exists": check_directory_exists,
    "file_contains": check_file_contains,
    "file_not_contains": check_file_not_contains,
    "regex_count": check_regex_count,
    "markdown_section_count": check_markdown_section_count,
    "markdown_required_sections": check_markdown_required_sections,
    "markdown_section_bullet_count": check_markdown_section_bullet_count,
    "markdown_section_field": check_markdown_section_field,
    "json_field_not_placeholder": check_json_field_not_placeholder,
    "json_field_iso_date": check_json_field_iso_date,
    "json_field_contains": check_json_field_contains,
    "shell_command": check_shell_command,
}


def run_check(check: dict, project_dir: Path, builder_inputs: dict) -> tuple[bool, str]:
    check_type = check["type"]
    if check_type == "http_check":
        return check_http(check, project_dir, builder_inputs)
    if check_type == "deployment_matches_source":
        return check_deployment_matches_source(check, project_dir, builder_inputs)
    handler = CHECK_HANDLERS.get(check_type)
    if not handler:
        return False, f"Unsupported check type: {check_type}"
    return handler(check, project_dir)


def main():
    parser = argparse.ArgumentParser(description="OneMillion Day Verifier")
    parser.add_argument("day", help="Day to verify (e.g., 'day-1' or '1')")
    parser.add_argument("--project-dir", default=os.getcwd(), help="Project directory")
    parser.add_argument("--vercel-url", help="Your Vercel deployment URL")
    parser.add_argument("--deployment-url", help="Alias for --vercel-url")
    parser.add_argument("--schema-dir", default=None, help="Path to verify/schema/ directory")
    parser.add_argument("--write-report", action="store_true", help="Update .onemillion/state.json")
    args = parser.parse_args()

    # Parse day arg
    day_num = args.day.replace("day-", "").lstrip("0") or "0"
    schema_dir = Path(args.schema_dir) if args.schema_dir else Path(__file__).parent.parent / "schema"
    schema_path = schema_dir / f"day-{int(day_num):02d}.json"

    if not schema_path.exists():
        print(f"{RED}Schema not found: {schema_path}{RESET}")
        print(f"Available schemas: {sorted(schema_dir.glob('day-*.json'))}")
        sys.exit(1)

    with open(schema_path) as f:
        schema = json.load(f)

    project_dir = Path(args.project_dir).resolve()
    builder_inputs = {"vercel_url": args.vercel_url or args.deployment_url}

    print(f"\n{BLUE}# Day {schema['day']} Verification — {schema['title']}{RESET}\n")

    all_passed = True
    sections = ["structural_checks", "code_quality_checks", "remote_checks"]
    report_lines = [
        f"# Day {schema['day']} Verification Report",
        "",
        f"- Title: {schema['title']}",
        f"- Project: `{project_dir}`",
        f"- Deployment: `{builder_inputs.get('vercel_url') or 'not provided'}`",
        "",
    ]

    for section in sections:
        if section not in schema or not schema[section]:
            continue
        print(f"{BLUE}## {section.replace('_', ' ').title()}{RESET}")
        report_lines.append(f"## {section.replace('_', ' ').title()}")
        for check in schema[section]:
            passed, msg = run_check(check, project_dir, builder_inputs)
            icon = f"{GREEN}✓{RESET}" if passed else f"{RED}✗{RESET}"
            print(f"  {icon} {check['id']}: {msg}")
            report_lines.append(f"- [{'x' if passed else ' '}] `{check['id']}`: {msg}")
            if not passed:
                all_passed = False
        print()
        report_lines.append("")

    if "manual_checks" in schema and schema["manual_checks"]:
        print(f"{YELLOW}## Manual Checks (answer in Claude Code instead — this script can't verify these){RESET}")
        report_lines.append("## Manual Checks")
        for check in schema["manual_checks"]:
            print(f"  ? {check['id']}: {check['ask']}")
            report_lines.append(f"- [ ] `{check['id']}`: {check['ask']}")
        print()
        report_lines.append("")

    if "quality_checks" in schema and schema["quality_checks"]:
        print(f"{YELLOW}## Quality Checks (use the Claude Code agent for these){RESET}")
        report_lines.append("## Quality Checks")
        for check in schema["quality_checks"]:
            print(f"  ? {check['id']}: {check['criteria']}")
            report_lines.append(f"- [ ] `{check['id']}`: {check['criteria']}")
        print()
        report_lines.append("")

    print()
    if all_passed:
        print(f"{GREEN}✓ Structural checks PASSED.{RESET} Run the Claude Code agent for full verification including quality + manual checks.")
        report_lines.extend(["## Result", "PASS - automated checks passed.", ""])
    else:
        print(f"{RED}✗ Some structural checks FAILED.{RESET} Fix the issues above before running the full verifier.")
        report_lines.extend(["## Result", "NEEDS REVISION - automated checks failed.", ""])

    if args.write_report:
        report_dir = project_dir / ".onemillion"
        report_dir.mkdir(exist_ok=True)
        report_path = report_dir / "state.json"
        if report_path.exists():
            try:
                state = json.loads(report_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                state = {}
        else:
            state = {}

        state.setdefault("course", "OneMillion Builder")
        state.setdefault("verification", {})
        state["verification"].setdefault("days", {})
        state["verification"]["days"][str(int(day_num))] = {
            "day": int(day_num),
            "title": schema["title"],
            "result": "PASS" if all_passed else "NEEDS_REVISION",
            "checked_at": dt.datetime.now(dt.timezone.utc).isoformat(),
            "project": str(project_dir),
            "deployment": builder_inputs.get("vercel_url"),
            "report": report_lines,
        }
        if all_passed:
            previous = state.get("last_verified_day")
            if not isinstance(previous, int) or int(day_num) > previous:
                state["last_verified_day"] = int(day_num)
        report_path.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
        print(f"Updated orchestrator state: {report_path}")

    sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    main()
