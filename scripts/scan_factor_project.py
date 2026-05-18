#!/usr/bin/env python3
"""Validate product-factor-skills repository structure.

This script intentionally uses only Python standard library.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

REQUIRED_ROOT = [
    "README.md",
    "SKILL.md",
    "VERSION",
    "CHANGELOG.md",
    "RELEASE_NOTES.md",
    "LICENSE",
    "ATTRIBUTION.md",
    "CONTRIBUTING.md",
    "ROADMAP.md",
    "product-factor-skills.json",
    "skills.json",
]

REQUIRED_DIRS = [
    "skills",
    "checklists",
    "templates",
    "examples",
    "guides",
    "scripts",
    "skill-factory",
    "docs",
    "logs",
    "schemas",
    ".github/workflows",
]

REQUIRED_SKILL_FILES = [
    "SKILL.md",
    "checklist.md",
    "audit-report-template.md",
    "refactor-plan-template.md",
    "scoring-rubric.md",
    "usage-examples.md",
    "skill.json",
]

REQUIRED_LOGS = [
    "logs/iteration-log.md",
    "logs/file-manifest.md",
    "logs/version-history.md",
]

REQUIRED_SUPPORT_FILES = [
    "docs/skill-routing-guide.md",
    "docs/output-contract.md",
    "guides/agent-review-loop.md",
    "templates/validation-summary-template.md",
    "templates/decision-log-template.md",
    "docs/skill-audit-runner.md",
    "docs/multi-skill-routing-matrix.md",
    "guides/repeatable-optimization-loop.md",
    "docs/skill-prompt-renderer.md",
    "docs/product-readiness-playbook.md",
    "scripts/run_skill_audit.py",
    "scripts/render_skill_prompt.py",
    "scripts/export_skill_catalog.py",
    "docs/skill-catalog-exporter.md",
    "docs/documentation-readiness-playbook.md",
    "examples/docs-audit-prompt.md",
    "scripts/select_factor_skill.py",
    "docs/skill-selection-engine.md",
    "examples/skill-selection-prompt.md",
    ".github/pull_request_template.md",
    ".github/ISSUE_TEMPLATE/bug_report.md",
    ".github/ISSUE_TEMPLATE/skill_request.md",
    "docs/security-privacy-playbook.md",
    "examples/security-privacy-audit-prompt.md",
    "templates/security-review-template.md",
    "SECURITY.md",
    "skills/15-factor-observability/SKILL.md",
    "docs/observability-playbook.md",
    "docs/multi-skill-composition-guide.md",
    "examples/observability-audit-prompt.md",
    "examples/composed-review-prompt.md",
    "templates/multi-skill-review-plan-template.md",
    "scripts/compose_factor_review.py",
]

README_KEYWORDS = [
    "Factor Skill",
    "Agent-native",
    "reusable standards",
    "project audit",
    "project refactor",
    "engineering checklist",
    "release readiness",
    "deployability",
    "maintainability",
    "Skill Factory",
    "repeatable optimization",
    "标准化审查",
    "可复用 Skill",
    "Agent 原生",
    "项目重构",
    "工程清单",
    "发布就绪",
    "可部署",
    "可维护",
    "可扩展",
    "技能工厂",
    "反复优化",
]

MIN_SKILLS = 12
VERSION_RE = re.compile(r"^v\d+\.\d+\.\d+$")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def exists(root: Path, rel: str) -> bool:
    return (root / rel).exists()


def load_json(path: Path, errors: list[str]):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - standard-library script
        errors.append(f"Invalid JSON: {path}: {exc}")
        return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan product-factor-skills structure")
    parser.add_argument("root", nargs="?", default=".", help="Repository root")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    missing: list[str] = []
    warnings: list[str] = []
    errors: list[str] = []

    for rel in REQUIRED_ROOT:
        if not exists(root, rel):
            missing.append(rel)

    for rel in REQUIRED_DIRS:
        if not exists(root, rel):
            missing.append(rel + "/")

    for rel in REQUIRED_LOGS:
        if not exists(root, rel):
            missing.append(rel)

    for rel in REQUIRED_SUPPORT_FILES:
        if not exists(root, rel):
            missing.append(rel)

    version = ""
    version_path = root / "VERSION"
    if version_path.exists():
        version = read_text(version_path).strip()
        if not VERSION_RE.match(version):
            errors.append(f"VERSION must look like vX.Y.Z, got: {version!r}")

    skills_dir = root / "skills"
    skill_dirs = sorted([p for p in skills_dir.iterdir() if p.is_dir()]) if skills_dir.exists() else []
    if len(skill_dirs) < MIN_SKILLS:
        missing.append(f"skills/* at least {MIN_SKILLS} skill directories")

    registry_path = root / "product-factor-skills.json"
    registry = load_json(registry_path, errors) if registry_path.exists() else None
    skills_index = load_json(root / "skills.json", errors) if (root / "skills.json").exists() else None
    registry_names = set()
    if isinstance(registry, dict):
        registry_names = {item.get("name") for item in registry.get("skills", []) if isinstance(item, dict)}
        if registry.get("version") != version:
            errors.append("product-factor-skills.json version does not match VERSION")
    if isinstance(skills_index, dict):
        index_names = {item.get("name") for item in skills_index.get("skills", []) if isinstance(item, dict)}
        if skills_index.get("version") != version:
            errors.append("skills.json version does not match VERSION")
        if registry_names and index_names != registry_names:
            errors.append("skills.json skill list does not match product-factor-skills.json")

    for skill in skill_dirs:
        for filename in REQUIRED_SKILL_FILES:
            if not (skill / filename).exists():
                missing.append(f"{skill.relative_to(root)}/{filename}")

        manifest_path = skill / "skill.json"
        manifest = load_json(manifest_path, errors) if manifest_path.exists() else None
        if isinstance(manifest, dict):
            if manifest.get("name") != skill.name:
                errors.append(f"{manifest_path.relative_to(root)} name does not match folder")
            if manifest.get("version") != version:
                errors.append(f"{manifest_path.relative_to(root)} version does not match VERSION")
            if manifest.get("agent_callable") is not True:
                warnings.append(f"{manifest_path.relative_to(root)} should set agent_callable=true")
            if not manifest.get("recommended_trigger_phrases"):
                errors.append(f"{manifest_path.relative_to(root)} missing recommended_trigger_phrases")
            if skill.name not in registry_names:
                errors.append(f"{skill.name} missing from product-factor-skills.json registry")

    readme = root / "README.md"
    if readme.exists():
        text = read_text(readme)
        for kw in README_KEYWORDS:
            if kw not in text:
                warnings.append(f"README missing keyword: {kw}")
        if version and version not in text:
            warnings.append(f"README does not mention current version {version}")

    workflow = root / ".github/workflows/validate.yml"
    if workflow.exists():
        workflow_text = read_text(workflow)
        if "scan_factor_project.py" not in workflow_text:
            errors.append("validate workflow does not run scan_factor_project.py")

    score = 100 - len(missing) * 5 - len(errors) * 4 - len(warnings) * 1
    score = max(0, score)

    if missing or errors:
        print("FAIL: product-factor-skills validation failed")
    else:
        print("PASS: product-factor-skills validation passed")

    if missing:
        print("\nMissing:")
        for item in missing:
            print(f"- {item}")

    if errors:
        print("\nErrors:")
        for item in errors:
            print(f"- {item}")

    if warnings:
        print("\nWarnings:")
        for item in warnings:
            print(f"- {item}")

    print(f"\nStructure score: {score}/100")
    print(f"Skills found: {len(skill_dirs)}")
    if version:
        print(f"Version: {version}")
    return 1 if missing or errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
