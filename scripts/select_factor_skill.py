#!/usr/bin/env python3
"""Recommend primary and secondary Factor Skills from a request or project signals.

The selector is intentionally simple and dependency-free. It reads skill.json
manifests, scores category/summary/tags/trigger matches, and optionally adds
lightweight file-signal matches from a target path.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
from typing import Iterable

STOPWORDS = {
    "the", "and", "for", "with", "this", "that", "from", "into", "project",
    "repository", "repo", "skill", "factor", "audit", "review", "refactor", "use",
    "to", "of", "in", "on", "a", "an", "is", "are", "be", "can", "should"
}

FILE_SIGNALS = {
    "8-factor-github-actions": [".github/workflows", "workflow", "action", "deploy", "ci", "release"],
    "10-factor-html": [
        ".html", "index.html", "landing", "css", "accessibility", "seo",
        "ui", "frontend", "react", "next", "next.js", "vite", "tailwind",
        "dashboard", "responsive", "visual", "screen", "mobile ui"
    ],
    "11-factor-cli": ["cli", "bin", "argparse", "commander", "click", "--help"],
    "12-factor-agents": ["agent", "tool", "memory", "prompt", "workflow", "human-in-the-loop"],
    "12-factor-app": ["app", "api", "service", "server", "config", "docker", "deploy", "frontend app", "web app", "mobile app"],
    "9-factor-rag": ["rag", "retrieval", "embedding", "chunk", "vector", "citation"],
    "7-factor-mcp": ["mcp", "tool schema", "server", "client", "permission"],
    "13-factor-product-readiness": ["roadmap", "release", "onboarding", "launch", "README", "CHANGELOG", "product flow", "mobile app"],
    "6-factor-docs": ["docs", "guide", "quickstart", "README", "example", "tutorial"],
    "5-factor-evals": ["eval", "evaluation", "test", "benchmark", "golden", "regression", "failure"],
    "14-factor-security-privacy": ["security", "privacy", "secret", "token", "credential", "permission", "workflow", "pii", "data retention", "supply-chain"],
    "15-factor-observability": ["observability", "log", "logging", "metric", "metrics", "trace", "tracing", "debug", "debugging", "artifact", "failure", "diagnostic", "validation summary"]
}


def tokenize(text: str) -> set[str]:
    return {t for t in re.findall(r"[a-z0-9][a-z0-9-]+", text.lower()) if t not in STOPWORDS and len(t) > 1}


def load_manifest(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def collect_manifests(root: Path) -> list[dict]:
    items: list[dict] = []
    for manifest_path in sorted((root / "skills").glob("*/skill.json")):
        item = load_manifest(manifest_path)
        item["path"] = str(manifest_path.parent.relative_to(root))
        items.append(item)
    return items


def iter_project_signal_text(target: Path, limit: int = 200) -> Iterable[str]:
    if not target.exists():
        return []
    signals: list[str] = []
    count = 0
    for path in sorted(target.rglob("*")):
        if count >= limit:
            break
        rel = str(path.relative_to(target))
        signals.append(rel)
        if path.is_file() and path.suffix.lower() in {".md", ".json", ".yml", ".yaml", ".toml", ".py", ".ts", ".js", ".html"}:
            try:
                signals.append(path.read_text(encoding="utf-8", errors="ignore")[:4000])
            except OSError:
                pass
        count += 1
    return signals


def score_manifest(manifest: dict, query_tokens: set[str], full_text: str, target_blob: str) -> tuple[int, list[str]]:
    name = manifest.get("name", "")
    searchable = " ".join([
        name,
        manifest.get("title", ""),
        manifest.get("summary", ""),
        manifest.get("category", ""),
        " ".join(manifest.get("tags", [])),
        " ".join(manifest.get("recommended_trigger_phrases", [])),
        " ".join(manifest.get("expected_inputs", [])),
        " ".join(manifest.get("expected_outputs", [])),
    ])
    tokens = tokenize(searchable)
    overlap = sorted(query_tokens & tokens)
    score = len(overlap) * 3
    reasons: list[str] = []
    if overlap:
        reasons.append("matched terms: " + ", ".join(overlap[:8]))
    if name in full_text:
        score += 20
        reasons.append("explicit skill name mentioned")
    for phrase in manifest.get("recommended_trigger_phrases", []):
        phrase_l = phrase.lower()
        if phrase_l and phrase_l in full_text:
            score += 25
            reasons.append("matched recommended trigger phrase")
            break
    for signal in FILE_SIGNALS.get(name, []):
        if signal.lower() in target_blob.lower() or signal.lower() in full_text:
            score += 8
            reasons.append(f"project signal: {signal}")
    return score, reasons[:5]


def render_markdown(results: list[dict], query: str, target: str | None) -> str:
    lines = ["# Factor Skill Selection", ""]
    if query:
        lines.append(f"Query: `{query}`")
    if target:
        lines.append(f"Target: `{target}`")
    lines.append("")
    if not results:
        lines.append("No Skill candidates found.")
        return "\n".join(lines) + "\n"
    primary = results[0]
    lines.append(f"Primary Skill: `{primary['name']}`")
    lines.append(f"Path: `{primary['path']}`")
    lines.append(f"Score: `{primary['score']}`")
    lines.append("")
    lines.append("## Ranked candidates")
    lines.append("")
    lines.append("| Rank | Skill | Category | Score | Reasons |")
    lines.append("|---:|---|---|---:|---|")
    for i, item in enumerate(results, 1):
        reasons = "; ".join(item.get("reasons", [])) or "general match"
        lines.append(f"| {i} | `{item['name']}` | `{item.get('category','')}` | {item['score']} | {reasons} |")
    lines.append("")
    lines.append("## Suggested next step")
    lines.append("")
    lines.append(f"Read `{primary['path']}/skill.json`, then `{primary['path']}/SKILL.md`, then apply the checklist and scoring rubric.")
    if len(results) > 1:
        lines.append(f"Use `{results[1]['name']}` as a secondary Skill if the project spans multiple concerns.")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Recommend Factor Skills from a request and optional target path")
    parser.add_argument("query", nargs="?", default="", help="User request or project description")
    parser.add_argument("--root", default=".", help="Repository root")
    parser.add_argument("--target", default=None, help="Optional target project path to inspect lightly")
    parser.add_argument("--top", type=int, default=3, help="Number of candidates to return")
    parser.add_argument("--json", dest="json_out", default=None, help="Optional JSON output path")
    parser.add_argument("--markdown", default=None, help="Optional Markdown output path")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    manifests = collect_manifests(root)
    target_blob = ""
    if args.target:
        target_path = Path(args.target).resolve()
        target_blob = "\n".join(iter_project_signal_text(target_path))
    full_text = f"{args.query}\n{target_blob}".lower()
    query_tokens = tokenize(full_text)

    results = []
    for manifest in manifests:
        score, reasons = score_manifest(manifest, query_tokens, full_text, target_blob)
        if score > 0:
            results.append({
                "name": manifest.get("name"),
                "path": manifest.get("path"),
                "category": manifest.get("category"),
                "summary": manifest.get("summary"),
                "score": score,
                "reasons": reasons,
            })
    results.sort(key=lambda item: (-item["score"], item["name"]))
    results = results[: max(1, args.top)]

    payload = {
        "query": args.query,
        "target": args.target,
        "result_count": len(results),
        "primary_skill": results[0]["name"] if results else None,
        "candidates": results,
    }

    if args.json_out:
        out = Path(args.json_out).resolve()
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    markdown = render_markdown(results, args.query, args.target)
    if args.markdown:
        out = Path(args.markdown).resolve()
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(markdown, encoding="utf-8")
    else:
        print(markdown)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
