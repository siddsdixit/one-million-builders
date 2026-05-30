"""
OneMillion Course Verification CLI

Usage:
    python verify.py day-X [--project-dir /path/to/project]

This is the structural-checks portion of verification. For full quality + AI-graded
checks, use the Claude Code agent at verify/agent/verify.md instead.

This script is mostly a fallback for builders who want a quick file-system check
without going through Claude.
"""

import json
import os
import re
import sys
import argparse
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


def check_file_exists_glob(check: dict, project_dir: Path) -> tuple[bool, str]:
    patterns = check["patterns"]
    found = []
    for pattern in patterns:
        matches = glob_module.glob(str(project_dir / pattern), recursive=True)
        found.extend(matches)
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

    content = path.read_text()
    required = check.get("required_strings", [])
    missing = [s for s in required if s not in content]
    if not missing:
        return True, f"All required strings present in {path.name}"
    return False, f"Missing in {path.name}: {missing}"


def check_file_not_contains(check: dict, project_dir: Path) -> tuple[bool, str]:
    path = project_dir / check["path"]
    if not path.exists():
        return False, f"File missing: {check['path']}"
    content = path.read_text()
    blocked = check.get("blocked_strings", [])
    found_blocked = [s for s in blocked if s in content]
    if found_blocked:
        return False, f"Should not contain: {found_blocked}"
    return True, "No blocked strings found"


def check_regex_count(check: dict, project_dir: Path) -> tuple[bool, str]:
    path = project_dir / check["path"]
    if not path.exists():
        return False, f"File missing: {check['path']}"
    content = path.read_text()
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
    content = path.read_text()
    pattern = check["section_pattern"]
    count = content.count(pattern)
    min_count = check.get("min_count", 1)
    if count >= min_count:
        return True, f"Found {count} sections matching '{pattern}'"
    return False, f"Found {count} sections, need {min_count}+"


def check_http(check: dict, project_dir: Path, builder_inputs: dict) -> tuple[bool, str]:
    url = None
    if check.get("url_source") == "ask_builder":
        url = builder_inputs.get("vercel_url")
        if not url:
            return False, "Vercel URL not provided (use --vercel-url flag)"
    elif check.get("url_source") == "build_from_vercel_base":
        base = builder_inputs.get("vercel_url")
        if not base:
            return False, "Vercel URL not provided"
        url = base.rstrip("/") + check["path_suffix"]
    if not url:
        return False, "No URL to check"
    try:
        req = urllib.request.Request(url, method="HEAD")
        with urllib.request.urlopen(req, timeout=10) as resp:
            if resp.status in check["expected_status"]:
                return True, f"{url} → {resp.status}"
            return False, f"{url} → {resp.status} (expected {check['expected_status']})"
    except Exception as e:
        return False, f"{url} → error: {e}"


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
}


def run_check(check: dict, project_dir: Path, builder_inputs: dict) -> tuple[bool, str]:
    check_type = check["type"]
    if check_type == "http_check":
        return check_http(check, project_dir, builder_inputs)
    handler = CHECK_HANDLERS.get(check_type)
    if not handler:
        return False, f"Unsupported check type: {check_type}"
    return handler(check, project_dir)


def main():
    parser = argparse.ArgumentParser(description="OneMillion Day Verifier (structural only)")
    parser.add_argument("day", help="Day to verify (e.g., 'day-1' or '1')")
    parser.add_argument("--project-dir", default=os.getcwd(), help="Project directory")
    parser.add_argument("--vercel-url", help="Your Vercel deployment URL")
    parser.add_argument("--schema-dir", default=None, help="Path to verify/schema/ directory")
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
    builder_inputs = {"vercel_url": args.vercel_url}

    print(f"\n{BLUE}# Day {schema['day']} Verification — {schema['title']}{RESET}\n")

    all_passed = True
    sections = ["structural_checks", "code_quality_checks", "remote_checks"]

    for section in sections:
        if section not in schema or not schema[section]:
            continue
        print(f"{BLUE}## {section.replace('_', ' ').title()}{RESET}")
        for check in schema[section]:
            passed, msg = run_check(check, project_dir, builder_inputs)
            icon = f"{GREEN}✓{RESET}" if passed else f"{RED}✗{RESET}"
            print(f"  {icon} {check['id']}: {msg}")
            if not passed:
                all_passed = False
        print()

    if "manual_checks" in schema and schema["manual_checks"]:
        print(f"{YELLOW}## Manual Checks (answer in Claude Code instead — this script can't verify these){RESET}")
        for check in schema["manual_checks"]:
            print(f"  ? {check['id']}: {check['ask']}")
        print()

    if "quality_checks" in schema and schema["quality_checks"]:
        print(f"{YELLOW}## Quality Checks (use the Claude Code agent for these){RESET}")
        for check in schema["quality_checks"]:
            print(f"  ? {check['id']}: {check['criteria']}")
        print()

    print()
    if all_passed:
        print(f"{GREEN}✓ Structural checks PASSED.{RESET} Run the Claude Code agent for full verification including quality + manual checks.")
    else:
        print(f"{RED}✗ Some structural checks FAILED.{RESET} Fix the issues above before running the full verifier.")

    sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    main()
