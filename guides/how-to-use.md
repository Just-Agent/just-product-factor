# How to Use product-factor-skills

`product-factor-skills` turns engineering standards into Agent-callable Skill packs.

## Quick start

1. Choose a Skill from `skills/`.
2. Read `skill.json` for trigger phrases and inputs.
3. Read `SKILL.md` for scope and workflow.
4. Apply `checklist.md` and `scoring-rubric.md`.
5. Output an audit report and refactor plan.

## Common commands for Agents

```text
Use the 12-factor-agents skill to review this agent project.
Use the 12-factor-app skill to audit this app for release readiness.
Use the 10-factor-html skill to polish this HTML page.
Use the 8-factor-github-actions skill to review this workflow.
Use the 9-factor-rag skill to audit this RAG system.
Use the 7-factor-mcp skill to review this MCP server.
```

## For maintainers

Run validation:

```bash
python scripts/scan_factor_project.py .
```

Create a new Skill skeleton:

```bash
python scripts/generate_factor_skill.py xx-factor-cli --title "xx-factor-cli" --category cli
```
