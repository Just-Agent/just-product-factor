#!/usr/bin/env python3
"""Compose a multi-Skill review plan from product-factor-skills manifests.

This utility is intentionally dependency-free. It does not run a full audit; it
creates a repeatable handoff package that tells an Agent which Skills to read,
what order to use them in, and what outputs to produce.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
from typing import Iterable

STOPWORDS = {
    "the", "and", "for", "with", "this", "that", "from", "into", "project",
    "repository", "repo", "skill", "factor", "audit", "review", "refactor", "use",
    "to", "of", "in", "on", "a", "an", "is", "are", "be", "can", "should",
}

DOMAIN_HINTS = {
    "5-factor-evals": ["eval", "evaluation", "benchmark", "golden", "regression", "test", "release gate"],
    "6-factor-docs": ["docs", "documentation", "readme", "quickstart", "guide", "example", "tutorial"],
    "7-factor-mcp": ["mcp", "tool schema", "server", "client", "permission", "integration"],
    "8-factor-github-actions": ["github actions", "workflow", "ci", "cd", "deploy", "release", "cache"],
    "9-factor-rag": ["rag", "retrieval", "embedding", "chunk", "vector", "citation", "context"],
    "10-factor-html": ["html", "landing", "seo", "accessibility", "responsive", "page", "css"],
    "11-factor-cli": ["cli", "command", "terminal", "--help", "argparse", "packaging"],
    "12-factor-agents": ["agent", "tool call", "memory", "prompt", "workflow", "human-in-the-loop"],
    "12-factor-app": ["app", "api", "service", "saas", "config", "docker", "deploy"],
    "13-factor-product-readiness": ["product", "launch", "open-source", "onboarding", "roadmap", "release readiness"],
    "14-factor-security-privacy": ["security", "privacy", "secret", "token", "credential", "permission", "pii", "data"],
    "15-factor-observability": ["observability", "log", "logging", "metric", "trace", "debug", "artifact", "failure"],
}


def tokenize(text: str) -> set[str]:
    return {t for t in re.findall(r"[a-z0-9][a-z0-9-]+", text.lower()) if t not in STOPWORDS and len(t) > 1}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def collect_manifests(root: Path) -> dict[str, dict]:
    manifests: dict[str, dict] = {}
    for manifest_path in sorted((root / "skills").glob("*/skill.json")):
        manifest = load_json(manifest_path)
        manifest["path"] = str(manifest_path.parent.relative_to(root))
        manifests[manifest["name"]] = manifest
    return manifests


def read_target_signals(target: Path | None, limit: int = 160) -> str:
    if target is None or not target.exists():
        return ""
    chunks: list[str] = []
    count = 0
    for path in sorted(target.rglob("*")):
        if count >= limit:
            break
        rel = str(path.relative_to(target))
        chunks.append(rel)
        if path.is_file() and path.suffix.lower() in {".md", ".json", ".yml", ".yaml", ".toml", ".py", ".ts", ".js", ".html", ".txt"}:
            try:
                chunks.append(path.read_text(encoding="utf-8", errors="ignore")[:3000])
            except OSError:
                pass
        count += 1
    return "\n".join(chunks)


def split_skills(value: str | None) -> list[str]:
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


def rank_skills(manifests: dict[str, dict], request: str, target_blob: str, limit: int) -> list[dict]:
    text = f"{request}\n{target_blob}".lower()
    tokens = tokenize(text)
    results: list[dict] = []
    for name, manifest in manifests.items():
        searchable = " ".join([
            name,
            manifest.get("title", ""),
            manifest.get("summary", ""),
            manifest.get("category", ""),
            " ".join(manifest.get("tags", [])),
            " ".join(manifest.get("recommended_trigger_phrases", [])),
        ])
        skill_tokens = tokenize(searchable)
        overlap = sorted(tokens & skill_tokens)
        score = len(overlap) * 3
        reasons: list[str] = []
        if overlap:
            reasons.append("matched terms: " + ", ".join(overlap[:8]))
        if name in text:
            score += 30
            reasons.append("explicit skill name mentioned")
        for phrase in manifest.get("recommended_trigger_phrases", []):
            if phrase.lower() in text:
                score += 30
                reasons.append("matched trigger phrase")
                break
        request_l = request.lower()
        for hint in DOMAIN_HINTS.get(name, []):
            if hint in request_l:
                score += 45
                reasons.append(f"request hint: {hint}")
            elif hint in text:
                score += 10
                reasons.append(f"project signal: {hint}")
        if score > 0:
            results.append({"name": name, "score": score, "reasons": reasons[:5]})
    results.sort(key=lambda item: (-item["score"], item["name"]))
    return results[:limit]


def normalize_selected(manifests: dict[str, dict], requested: Iterable[str], ranked: list[dict], max_skills: int) -> list[str]:
    selected: list[str] = []
    for name in requested:
        if name not in manifests:
            raise SystemExit(f"Unknown Skill: {name}")
        if name not in selected:
            selected.append(name)
    for item in ranked:
        name = item["name"]
        if name not in selected:
            selected.append(name)
        if len(selected) >= max_skills:
            break
    if not selected:
        selected = ["13-factor-product-readiness"] if "13-factor-product-readiness" in manifests else sorted(manifests)[0:1]
    return selected[:max_skills]


def render_plan(root: Path, manifests: dict[str, dict], selected: list[str], request: str, target: str | None, ranked: list[dict]) -> str:
    version = (root / "VERSION").read_text(encoding="utf-8").strip() if (root / "VERSION").exists() else "unknown"
    lines = [
        "# Multi-Skill Factor Review Plan",
        "",
        f"Repository version: `{version}`",
        f"Generated: `{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}`",
        "",
    ]
    if request:
        lines += ["## Request", "", request, ""]
    if target:
        lines += ["## Target", "", f"`{target}`", ""]
    lines += [
        "## Selected Skills",
        "",
        "| Order | Skill | Category | Role | Summary |",
        "|---:|---|---|---|---|",
    ]
    for index, name in enumerate(selected, 1):
        manifest = manifests[name]
        role = "Primary" if index == 1 else "Secondary"
        summary = manifest.get("summary", "").replace("|", "\\|")
        lines.append(f"| {index} | `{name}` | `{manifest.get('category', '')}` | {role} | {summary} |")
    lines += ["", "## Review Order", ""]
    for index, name in enumerate(selected, 1):
        path = manifests[name].get("path", f"skills/{name}")
        lines += [
            f"### {index}. `{name}`",
            "",
            f"1. Read `{path}/skill.json`.",
            f"2. Read `{path}/SKILL.md`.",
            f"3. Apply `{path}/checklist.md` and `{path}/scoring-rubric.md`.",
            f"4. Write findings using `{path}/audit-report-template.md`.",
            f"5. Add fixes to the combined refactor plan using `{path}/refactor-plan-template.md`.",
            "",
        ]
    lines += [
        "## Combined Output Contract",
        "",
        "Return these sections in order:",
        "",
        "1. Selected Skills and why.",
        "2. Project diagnosis.",
        "3. Per-Skill scorecards.",
        "4. Cross-Skill conflicts and dependencies.",
        "5. Critical blockers.",
        "6. Prioritized refactor plan.",
        "7. Validation plan and validation limits.",
        "8. Next iteration roadmap.",
        "",
        "## Ranked Candidates",
        "",
        "| Rank | Skill | Score | Reasons |",
        "|---:|---|---:|---|",
    ]
    for index, item in enumerate(ranked, 1):
        reasons = "; ".join(item.get("reasons", [])) or "manual or fallback selection"
        lines.append(f"| {index} | `{item['name']}` | {item['score']} | {reasons} |")
    lines.append("")
    return "\n".join(lines)


def render_prompt(selected: list[str], request: str, target: str | None) -> str:
    lines = [
        "# Agent Handoff Prompt",
        "",
        "Use product-factor-skills to perform a composed multi-Skill review.",
        "",
    ]
    if request:
        lines += ["User request:", "", request, ""]
    if target:
        lines += ["Target project:", "", f"`{target}`", ""]
    lines += [
        "Selected Skills:",
        "",
    ]
    for name in selected:
        lines.append(f"- `{name}`")
    lines += [
        "",
        "Instructions:",
        "",
        "1. Use the first Skill as the primary review lens.",
        "2. Use the remaining Skills as secondary passes.",
        "3. Read each selected Skill's `skill.json`, `SKILL.md`, checklist, scoring rubric, and templates.",
        "4. Produce a single combined audit report and a single prioritized refactor plan.",
        "5. Record validation evidence and limits honestly.",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Compose a multi-Skill Factor review plan")
    parser.add_argument("request", nargs="?", default="", help="User request or project description")
    parser.add_argument("--root", default=".", help="product-factor-skills repository root")
    parser.add_argument("--target", default=None, help="Optional target project path to inspect lightly")
    parser.add_argument("--skills", default=None, help="Comma-separated Skill names to force into the plan")
    parser.add_argument("--max-skills", type=int, default=4, help="Maximum number of Skills in the composed plan")
    parser.add_argument("--out", default="./tmp/composed-factor-review", help="Output directory")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    manifests = collect_manifests(root)
    target_path = Path(args.target).resolve() if args.target else None
    target_blob = read_target_signals(target_path)
    ranked = rank_skills(manifests, args.request, target_blob, args.max_skills + 2)
    forced = split_skills(args.skills)
    selected = normalize_selected(manifests, forced, ranked, args.max_skills)

    out = Path(args.out).resolve()
    out.mkdir(parents=True, exist_ok=True)
    target_display = str(target_path) if target_path else None

    plan_md = render_plan(root, manifests, selected, args.request, target_display, ranked)
    prompt_md = render_prompt(selected, args.request, target_display)
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "version": (root / "VERSION").read_text(encoding="utf-8").strip() if (root / "VERSION").exists() else "unknown",
        "request": args.request,
        "target": target_display,
        "selected_skills": selected,
        "ranked_candidates": ranked,
        "output_files": ["review-plan.md", "review-plan.json", "handoff-prompt.md"],
    }

    (out / "review-plan.md").write_text(plan_md, encoding="utf-8")
    (out / "handoff-prompt.md").write_text(prompt_md, encoding="utf-8")
    (out / "review-plan.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"PASS: composed {len(selected)} Skill review plan at {out}")
    for name in selected:
        print(f"- {name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
