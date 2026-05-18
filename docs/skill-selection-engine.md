# Skill Selection Engine

`product-factor-skills` now includes a lightweight selector for choosing the best primary and secondary Factor Skills before an audit begins.

The selector is dependency-free and uses:

- `skills/*/skill.json` manifests
- trigger phrases
- tags, categories, summaries, and expected outputs
- optional project file-name and text signals

## Usage

```bash
python scripts/select_factor_skill.py "audit this RAG app for retrieval quality and regression tests" --root .
```

With a target project path:

```bash
python scripts/select_factor_skill.py "prepare this repo for release" --root . --target ./examples/sample-agent-project --top 5
```

Write machine-readable and markdown results:

```bash
python scripts/select_factor_skill.py   "review this MCP server and add release confidence"   --root .   --target ./my-project   --json ./tmp/skill-selection.json   --markdown ./tmp/skill-selection.md
```

## How Agents should use it

1. Run the selector when the user request is broad or ambiguous.
2. Use the top result as the primary Skill.
3. Use the second or third result as secondary Skills when the target spans multiple domains.
4. Read the selected `skill.json` first, then `SKILL.md`, checklist, scoring rubric, and templates.
5. Record selection evidence in the audit report.

## Limits

The selector is a heuristic helper, not a replacement for judgment. It does not call external services, parse every language deeply, or infer business context that is not present in the query or files.
