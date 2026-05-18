# 7-factor-mcp Skill

## Name

7-factor-mcp

## Purpose

Audit and improve MCP tools and servers for tool schema clarity, permission boundaries, runtime safety, observability, and user ergonomics.

## When to use

- MCP servers
- MCP clients
- Tool integrations
- Agent tool layers
- Local/remote tool bridges

## When not to use

- General APIs with no Agent/tool schema layer
- Static docs only

## Inputs

Ask for or inspect:

- README and docs
- source files
- examples and recipes
- configuration files
- tests and validation scripts
- CI/CD workflow files
- logs, changelog, release notes, or version history

## Workflow

1. Identify the project goal and user-facing promise.
2. Inspect available files.
3. Apply `checklist.md`.
4. Score with `scoring-rubric.md`.
5. Produce an audit report using `audit-report-template.md`.
6. Produce a refactor plan using `refactor-plan-template.md`.
7. Prioritize changes by product value and release readiness.
8. Validate changes if the environment allows.

## Review dimensions

- Tool boundaries
- Schema clarity
- Permission model
- Runtime safety
- Error handling
- Observability
- Developer ergonomics

## Refactor priorities

1. Clarify tool contracts
2. Reduce unsafe permissions
3. Improve errors
4. Add examples
5. Add validation and logs

## Output format

Return:

1. Summary
2. Scorecard
3. Critical findings
4. Recommended changes
5. Refactor plan
6. Validation plan
7. Next iteration suggestions

## Example calls

See `usage-examples.md`.

## Version

v0.5.0

## Agent manifest

This Skill includes a machine-readable `skill.json` manifest so an Agent can quickly identify triggers, expected inputs, expected outputs, required files, and the review protocol before reading the full markdown pack.

