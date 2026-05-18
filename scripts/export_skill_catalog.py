#!/usr/bin/env python3
"""Export a human-readable and machine-readable catalog from Skill manifests.

This script uses only Python standard library so it can run in constrained CI
or Agent execution environments.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from datetime import datetime, timezone


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - CLI utility
        raise SystemExit(f"Could not parse {path}: {exc}") from exc


def collect_skills(root: Path) -> list[dict]:
    skills_dir = root / "skills"
    if not skills_dir.exists():
        raise SystemExit(f"Missing skills directory: {skills_dir}")
    skills: list[dict] = []
    for skill_dir in sorted(p for p in skills_dir.iterdir() if p.is_dir()):
        manifest_path = skill_dir / "skill.json"
        if not manifest_path.exists():
            continue
        manifest = load_json(manifest_path)
        manifest["path"] = str(skill_dir.relative_to(root))
        skills.append(manifest)
    return skills


def write_markdown(root: Path, skills: list[dict], out: Path) -> None:
    version = (root / "VERSION").read_text(encoding="utf-8").strip() if (root / "VERSION").exists() else "unknown"
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    lines = [
        "# Product Factor Skills Catalog",
        "",
        f"Generated: {generated_at}",
        f"Repository version: `{version}`",
        "",
        "| Skill | Category | Summary | Example trigger |",
        "|---|---|---|---|",
    ]
    for item in skills:
        triggers = item.get("recommended_trigger_phrases") or []
        trigger = triggers[0] if triggers else ""
        summary = str(item.get("summary", "")).replace("|", "\\|")
        lines.append(f"| `{item.get('name', '')}` | `{item.get('category', '')}` | {summary} | {trigger} |")
    lines.append("")
    lines.append("## Usage")
    lines.append("")
    lines.append("Read this catalog before selecting a Skill, then open the selected `skill.json` and `SKILL.md`.")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_json(root: Path, skills: list[dict], out: Path) -> None:
    version = (root / "VERSION").read_text(encoding="utf-8").strip() if (root / "VERSION").exists() else "unknown"
    payload = {
        "name": "product-factor-skills-catalog",
        "version": version,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "skill_count": len(skills),
        "skills": skills,
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Export a catalog from product-factor-skills manifests")
    parser.add_argument("root", nargs="?", default=".", help="Repository root")
    parser.add_argument("--markdown", default="docs/generated-skill-catalog.md", help="Markdown output path")
    parser.add_argument("--json", default="docs/generated-skill-catalog.json", help="JSON output path")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    skills = collect_skills(root)
    write_markdown(root, skills, Path(args.markdown).resolve())
    write_json(root, skills, Path(args.json).resolve())
    print(f"PASS: exported {len(skills)} skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
