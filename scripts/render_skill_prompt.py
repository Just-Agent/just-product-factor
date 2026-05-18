#!/usr/bin/env python3
"""Render a copyable Agent prompt for a selected Factor Skill.

The script uses only the Python standard library so it can run in small
Agent sandboxes and CI jobs.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

DEFAULT_SECTIONS = [
    "SKILL.md",
    "checklist.md",
    "scoring-rubric.md",
    "audit-report-template.md",
    "refactor-plan-template.md",
    "usage-examples.md",
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore").strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Render a Factor Skill prompt pack")
    parser.add_argument("skill", help="Skill name, for example 12-factor-agents")
    parser.add_argument("--root", default=".", help="Repository root")
    parser.add_argument("--target", default="<target-project>", help="Target project path or description")
    parser.add_argument("--out", default=None, help="Optional output markdown file")
    parser.add_argument("--sections", nargs="*", default=DEFAULT_SECTIONS, help="Skill files to include")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    skill_dir = root / "skills" / args.skill
    if not skill_dir.is_dir():
        print(f"ERROR: skill not found: {args.skill}", file=sys.stderr)
        return 2

    manifest_path = skill_dir / "skill.json"
    manifest = json.loads(read(manifest_path)) if manifest_path.exists() else {}
    title = manifest.get("title", args.skill)
    triggers = manifest.get("recommended_trigger_phrases", [])

    parts: list[str] = []
    parts.append(f"# Rendered Factor Skill Prompt: {title}\n")
    parts.append("## Task\n")
    parts.append(
        f"Use the `{args.skill}` Factor Skill to audit and improve `{args.target}`. "
        "Inspect available files, apply the checklist and scoring rubric, produce an audit report, "
        "produce a prioritized refactor plan, and record validation results or validation limits honestly.\n"
    )

    if triggers:
        parts.append("## Recommended trigger phrases\n")
        for item in triggers:
            parts.append(f"- {item}")
        parts.append("")

    for filename in args.sections:
        path = skill_dir / filename
        if not path.exists():
            continue
        parts.append(f"## Source: skills/{args.skill}/{filename}\n")
        parts.append(read(path))
        parts.append("")

    output = "\n".join(parts).rstrip() + "\n"
    if args.out:
        out = Path(args.out).resolve()
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(output, encoding="utf-8")
        print(out)
    else:
        print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
