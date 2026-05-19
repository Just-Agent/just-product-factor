---
name: just-product-factor
description: Route product, UI, frontend, app, Agent, RAG, MCP, CLI, GitHub Actions, docs, security, observability, and release-readiness tasks to the right Factor Skill. Use when auditing, refactoring, packaging, or improving a project and the best review lens is not yet obvious.
---

# product-factor-skills Root Skill

## Name

product-factor-skills

## Purpose

Coordinate a collection of reusable Factor Skills for Agent-native product optimization. Use this root Skill when the user wants to audit, score, refactor, document, release, or continuously improve a project but has not selected a specific Factor Skill.

## When to use

Use this root Skill when:

- The user asks to optimize a project or repository.
- The user provides a zip and asks for the next version.
- The user asks which Factor Skill should apply.
- The project spans multiple domains such as Agent, App, HTML, GitHub Actions, RAG, MCP, CLI, docs, product readiness, security/privacy, and observability.
- The project involves UI, frontend, React/Next/Vite, dashboards, landing pages, mobile app screens, or HTML previews and needs a product-quality review route.
- The user wants to create a new `xx-factor-*` Skill.

## When not to use

Do not use this root Skill when the user already selected a specific Skill and the project scope is narrow. In that case, use the specific Skill folder directly.

## Workflow

1. Read `product-factor-skills.json` or `skills.json` to understand the registry.
2. If routing is unclear, run or simulate `python scripts/select_factor_skill.py "<request>" --root . --top 5`.
3. If the project needs multiple review lenses, run or simulate `python scripts/compose_factor_review.py "<request>" --root . --max-skills 4`.
4. Select the closest Skill based on project type and user intent.
5. Read the selected Skill's `skill.json` manifest.
6. Read the selected Skill's `SKILL.md`, checklist, scoring rubric, and templates.
7. Inspect project files.
8. Produce an audit report and refactor plan.
9. If modifying this repository, update version, changelog, release notes, logs, and file manifest.
10. Run `python scripts/scan_factor_project.py .` if possible.
11. Run `python scripts/export_skill_catalog.py . --markdown docs/generated-skill-catalog.md --json docs/generated-skill-catalog.json` when Skill manifests change.

## Skill routing

| User intent | Route to |
|---|---|
| Agent project, tools, memory, evals | `skills/12-factor-agents/` |
| App, API, SaaS, deployability | `skills/12-factor-app/` |
| UI, frontend, React/Next/Vite, dashboard, landing page, generated preview, HTML | `skills/10-factor-html/`, optionally paired with `skills/12-factor-app/` |
| GitHub Actions, CI/CD, release workflow | `skills/8-factor-github-actions/` |
| RAG, retrieval, citations | `skills/9-factor-rag/` |
| Evals, golden cases, regression tests, release gates | `skills/5-factor-evals/` |
| MCP server/client/tool schema | `skills/7-factor-mcp/` |
| CLI, commands, help text, packaging | `skills/11-factor-cli/` |
| Product launch readiness, onboarding, open-source polish | `skills/13-factor-product-readiness/` |
| README, docs, examples, quickstart, Agent handoff prompts | `skills/6-factor-docs/` |
| Security, privacy, secrets, permissions, data handling | `skills/14-factor-security-privacy/` |
| Observability, logs, traces, metrics, debugging, artifacts | `skills/15-factor-observability/` |
| Multi-Skill release or full product review | `scripts/compose_factor_review.py` plus selected Skill folders |
| New standard creation | `skill-factory/` and `scripts/generate_factor_skill.py` |

## Output format

When auditing a project, return:

1. Selected Skill and why.
2. Project diagnosis.
3. Factor scorecard.
4. Critical findings.
5. Prioritized refactor plan.
6. Validation results or validation limits.
7. Next iteration roadmap.

When iterating this repository, return the packaged zip link requested by the user.

## Version

v0.9.0

## New in v0.9.0

- Added `15-factor-observability` for runtime visibility, structured logs, metrics, traces, validation artifacts, failure diagnostics, privacy-safe debugging, and Agent handoff readiness.
- Added `scripts/compose_factor_review.py` to create a repeatable multi-Skill review plan with `review-plan.md`, `review-plan.json`, and `handoff-prompt.md`.
- Added `docs/observability-playbook.md`, `docs/multi-skill-composition-guide.md`, `templates/multi-skill-review-plan-template.md`, `examples/observability-audit-prompt.md`, and `examples/composed-review-prompt.md`.
- Updated routing, registry manifests, validation, and CI for twelve bundled Skills.

## New in v0.8.0

- Added `14-factor-security-privacy` for secrets hygiene, permission boundaries, data handling, CI/CD security, dependency hygiene, Agent/tool safety, and release blockers.
- Added `SECURITY.md`, `docs/security-privacy-playbook.md`, `templates/security-review-template.md`, and `examples/security-privacy-audit-prompt.md`.
- Updated routing, registry manifests, validation, and release logs for eleven bundled Skills.

## New in v0.7.0

- Added `5-factor-evals` for golden cases, regression checks, failure taxonomy, and release gates.
- Added `scripts/select_factor_skill.py` for dependency-free Skill selection from user requests and project signals.
- Added `docs/skill-selection-engine.md` and `examples/skill-selection-prompt.md` for routing broad or ambiguous audits.
- Updated validation to require ten bundled Skills and smoke-test the selector.

## Documentation routing

Use `6-factor-docs` when a project is technically useful but users or Agents cannot quickly understand what it does, how to start, where examples live, or how to validate success.

## Evaluation routing

Use `5-factor-evals` when a project needs repeatable confidence: golden cases, regression checks, benchmark notes, failure taxonomy, validation summaries, or release gates.

## Security/privacy routing

Use `14-factor-security-privacy` when a project touches secrets, credentials, user data, workflows, CI/CD, deployments, Agent tools, MCP integrations, RAG sources, or public release risk. Pair it with the relevant domain Skill when mitigation requires code, workflow, or product changes.

## Observability routing

Use `15-factor-observability` when a product is useful but hard to debug, when failures are not actionable, when CI or release validation lacks artifacts, or when future Agent iterations need stable logs and summaries to continue work.
