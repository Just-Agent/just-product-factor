# Agent Invocation Protocol

This document defines how an Agent should call and apply `product-factor-skills`.

## 1. Select the closest Skill

Use the project type and user request to choose one Skill:

| Project need | Recommended Skill |
|---|---|
| Agent runtime, tools, memory, evals | `12-factor-agents` |
| App, SaaS, API, CLI, deployability | `12-factor-app` |
| HTML page, landing page, docs page | `10-factor-html` |
| GitHub Actions, CI/CD, releases | `8-factor-github-actions` |
| RAG, retrieval, citations, evals | `9-factor-rag` |
| MCP server/client/tool schema | `7-factor-mcp` |

## 2. Read machine-readable metadata first

Read `skills/<skill>/skill.json` before the markdown files. It tells the Agent:

- trigger phrases
- expected inputs
- expected outputs
- required files
- review protocol
- tags and category

## 3. Apply the full Skill pack

Then read:

1. `SKILL.md`
2. `checklist.md`
3. `scoring-rubric.md`
4. `audit-report-template.md`
5. `refactor-plan-template.md`
6. `usage-examples.md`

## 4. Produce two outputs

Every review should produce:

1. An evidence-based audit report.
2. A prioritized refactor plan.

For repo iteration tasks, also update changelog, release notes, version history, and file manifest.

## 5. Be honest about validation

If install, build, lint, test, or smoke tests cannot run, record the limitation. Do not claim success without evidence.
