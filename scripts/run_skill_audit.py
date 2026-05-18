#!/usr/bin/env python3
"""Generate a lightweight Factor Skill audit package for a target project.

The script uses only Python standard library. It does not replace a real Agent
review; it prepares a structured audit folder that an Agent or maintainer can
fill in consistently.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from datetime import datetime, timezone

REQUIRED_SKILL_FILES = [
    "SKILL.md",
    "skill.json",
    "checklist.md",
    "scoring-rubric.md",
    "audit-report-template.md",
    "refactor-plan-template.md",
    "usage-examples.md",
]

COMMON_PROJECT_SIGNALS = [
    "README.md",
    "CHANGELOG.md",
    "RELEASE_NOTES.md",
    "VERSION",
    "package.json",
    "pyproject.toml",
    "requirements.txt",
    "Dockerfile",
    ".github/workflows",
    "docs",
    "examples",
    "tests",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def load_json(path: Path) -> dict:
    try:
        return json.loads(read_text(path))
    except Exception as exc:  # noqa: BLE001 - user-facing utility
        raise SystemExit(f"Could not parse JSON file {path}: {exc}") from exc


def find_project_signals(target: Path) -> list[str]:
    signals: list[str] = []
    for rel in COMMON_PROJECT_SIGNALS:
        if (target / rel).exists():
            signals.append(rel)
    return signals


def list_top_files(target: Path, limit: int = 80) -> list[str]:
    files: list[str] = []
    skip_dirs = {".git", "node_modules", ".venv", "venv", "dist", "build", "__pycache__"}
    for path in sorted(target.rglob("*")):
        if len(files) >= limit:
            break
        if any(part in skip_dirs for part in path.relative_to(target).parts):
            continue
        if path.is_file():
            files.append(str(path.relative_to(target)))
    return files


def ensure_skill_pack(repo: Path, skill: str) -> Path:
    skill_dir = repo / "skills" / skill
    if not skill_dir.exists():
        available = sorted(p.name for p in (repo / "skills").glob("*") if p.is_dir())
        raise SystemExit(f"Skill not found: {skill}. Available: {', '.join(available)}")
    missing = [name for name in REQUIRED_SKILL_FILES if not (skill_dir / name).exists()]
    if missing:
        raise SystemExit(f"Skill pack is incomplete: {skill}; missing: {', '.join(missing)}")
    return skill_dir


def write_audit_files(repo: Path, target: Path, skill: str, out_dir: Path) -> None:
    skill_dir = ensure_skill_pack(repo, skill)
    manifest = load_json(skill_dir / "skill.json")
    out_dir.mkdir(parents=True, exist_ok=True)

    signals = find_project_signals(target)
    top_files = list_top_files(target)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    (out_dir / "audit-brief.md").write_text(f"""# Factor Skill Audit Brief

Generated: {now}

## Selected Skill

- Skill: `{manifest.get('name', skill)}`
- Category: `{manifest.get('category', 'unknown')}`
- Summary: {manifest.get('summary', '')}

## Target Project

- Path: `{target}`
- Signals found: {', '.join(signals) if signals else 'none detected'}

## Recommended Agent Workflow

1. Read `{skill_dir.relative_to(repo)}/skill.json`.
2. Read `{skill_dir.relative_to(repo)}/SKILL.md`.
3. Inspect the target project files listed below.
4. Apply `{skill_dir.relative_to(repo)}/checklist.md`.
5. Score with `{skill_dir.relative_to(repo)}/scoring-rubric.md`.
6. Fill `audit-report.md`, `refactor-plan.md`, `validation-summary.md`, and `decision-log.md`.

## Top Project Files

""", encoding="utf-8")
    with (out_dir / "audit-brief.md").open("a", encoding="utf-8") as fh:
        for item in top_files:
            fh.write(f"- `{item}`\n")

    (out_dir / "audit-report.md").write_text(read_text(skill_dir / "audit-report-template.md"), encoding="utf-8")
    (out_dir / "refactor-plan.md").write_text(read_text(skill_dir / "refactor-plan-template.md"), encoding="utf-8")

    validation_template = repo / "templates" / "validation-summary-template.md"
    if validation_template.exists():
        (out_dir / "validation-summary.md").write_text(read_text(validation_template), encoding="utf-8")
    else:
        (out_dir / "validation-summary.md").write_text("# Validation Summary\n\n", encoding="utf-8")

    decision_template = repo / "templates" / "decision-log-template.md"
    if decision_template.exists():
        (out_dir / "decision-log.md").write_text(read_text(decision_template), encoding="utf-8")
    else:
        (out_dir / "decision-log.md").write_text("# Decision Log\n\n", encoding="utf-8")

    machine_summary = {
        "generated_at": now,
        "skill": manifest.get("name", skill),
        "category": manifest.get("category", "unknown"),
        "target_project": str(target),
        "signals_found": signals,
        "top_files": top_files,
        "outputs": [
            "audit-brief.md",
            "audit-report.md",
            "refactor-plan.md",
            "validation-summary.md",
            "decision-log.md",
        ],
    }
    (out_dir / "audit-summary.json").write_text(json.dumps(machine_summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a Factor Skill audit package")
    parser.add_argument("--repo", default=".", help="product-factor-skills repository root")
    parser.add_argument("--target", required=True, help="Project directory to audit")
    parser.add_argument("--skill", required=True, help="Skill name, e.g. 12-factor-agents")
    parser.add_argument("--out", default="factor-audit", help="Output directory")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    target = Path(args.target).resolve()
    out_dir = Path(args.out).resolve()

    if not repo.exists():
        raise SystemExit(f"Repository root not found: {repo}")
    if not target.exists():
        raise SystemExit(f"Target project not found: {target}")

    write_audit_files(repo, target, args.skill, out_dir)
    print(f"PASS: audit package generated at {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
