#!/usr/bin/env python3
"""Generate a new Factor Skill skeleton using only Python standard library."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

REQUIRED_FILES = {
    "SKILL.md": """# {title} Skill\n\n## Name\n\n{name}\n\n## Purpose\n\n{summary}\n\n## When to use\n\n- Use when reviewing projects in the `{category}` domain.\n- Use when the user needs a repeatable audit, scorecard, and refactor plan.\n\n## When not to use\n\n- Do not use for unrelated domains.\n- Do not use when the user only needs a short conceptual explanation.\n\n## Inputs\n\nAsk for or inspect README, source files, config, examples, tests, docs, workflows, logs, and release notes.\n\n## Workflow\n\n1. Identify the project goal and user-facing promise.\n2. Inspect available files.\n3. Apply `checklist.md`.\n4. Score with `scoring-rubric.md`.\n5. Produce an audit report using `audit-report-template.md`.\n6. Produce a refactor plan using `refactor-plan-template.md`.\n7. Validate changes if the environment allows.\n\n## Review dimensions\n\n- Product clarity\n- Architecture\n- Configuration\n- Runtime behavior\n- Error handling\n- Documentation\n- Examples\n- Release readiness\n\n## Scoring\n\nUse `scoring-rubric.md`.\n\n## Output format\n\nReturn summary, scorecard, critical findings, recommended changes, refactor plan, validation plan, and next iteration suggestions.\n\n## Example calls\n\nSee `usage-examples.md`.\n\n## Version\n\n{version}\n""",
    "checklist.md": """# {title} Checklist\n\n- [ ] The project goal is clear.\n- [ ] The target user is clear.\n- [ ] The installation or setup path is clear.\n- [ ] Configuration is explicit and documented.\n- [ ] Errors have actionable messages.\n- [ ] Examples are copyable.\n- [ ] Validation commands are documented.\n- [ ] Release readiness is addressed.\n""",
    "scoring-rubric.md": """# {title} Scoring Rubric\n\nScore each dimension from 0 to 5.\n\n| Dimension | Score | Notes |\n|---|---:|---|\n| Product clarity | 0-5 | Is the promise obvious? |\n| Architecture | 0-5 | Is the structure maintainable? |\n| Usability | 0-5 | Can a new user start quickly? |\n| Validation | 0-5 | Can the project be tested? |\n| Release readiness | 0-5 | Is it ready to publish/deploy? |\n\nOverall score = average * 20.\n""",
    "audit-report-template.md": """# {title} Audit Report\n\n## Summary\n\n## Scorecard\n\n## Critical findings\n\n## Recommended changes\n\n## Validation results\n\n## Next iteration\n""",
    "refactor-plan-template.md": """# {title} Refactor Plan\n\n## Goal\n\n## Priority 1: release blockers\n\n## Priority 2: usability improvements\n\n## Priority 3: maintainability improvements\n\n## Validation plan\n""",
    "usage-examples.md": """# {title} Usage Examples\n\n```text\nUse the {name} skill to review this project.\n```\n\n```text\nUse the {name} skill to refactor this project for release readiness.\n```\n""",
}


def valid_name(name: str) -> bool:
    return bool(re.match(r"^(\d+-factor-[a-z0-9-]+|xx-factor-[a-z0-9-]+)$", name))


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a Factor Skill skeleton")
    parser.add_argument("name", help="Skill folder name, e.g. xx-factor-cli")
    parser.add_argument("--title", default=None, help="Human readable title")
    parser.add_argument("--category", default="general", help="Skill category")
    parser.add_argument("--summary", default="Audit and refactor a product engineering domain with a repeatable Factor Skill.")
    parser.add_argument("--version", default=None, help="Version, defaults to repository VERSION")
    parser.add_argument("--root", default=".", help="Repository root")
    parser.add_argument("--dry-run", action="store_true", help="Print target path without writing")
    args = parser.parse_args()

    if not valid_name(args.name):
        print("ERROR: name must look like 6-factor-cli or xx-factor-cli", file=sys.stderr)
        return 2

    root = Path(args.root).resolve()
    version = args.version
    if version is None:
        version_path = root / "VERSION"
        version = version_path.read_text(encoding="utf-8").strip() if version_path.exists() else "v0.1.0"

    title = args.title or args.name
    target = root / "skills" / args.name
    if args.dry_run:
        print(f"Would create: {target}")
        return 0

    if target.exists():
        print(f"ERROR: {target} already exists", file=sys.stderr)
        return 1

    target.mkdir(parents=True)
    data = {
        "name": args.name,
        "title": title,
        "category": args.category,
        "summary": args.summary,
        "version": version,
    }
    for filename, template in REQUIRED_FILES.items():
        (target / filename).write_text(template.format(**data), encoding="utf-8")

    manifest = {
        "name": args.name,
        "version": version,
        "title": title,
        "summary": args.summary,
        "category": args.category,
        "agent_callable": True,
        "status": "draft",
        "recommended_trigger_phrases": [f"Use the {args.name} skill to review this project."],
        "required_files": list(REQUIRED_FILES.keys()) + ["skill.json"],
        "expected_inputs": ["README", "source files", "configuration", "examples", "tests", "logs"],
        "expected_outputs": ["audit report", "scorecard", "refactor plan", "validation plan"],
        "tags": ["Factor Skill", args.category, "project audit", "project refactor"],
        "review_protocol": [
            "Identify project goal.",
            "Inspect available files.",
            "Apply checklist and scoring rubric.",
            "Return audit report and refactor plan.",
        ],
    }
    (target / "skill.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Created {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
