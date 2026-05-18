# 14-factor-security-privacy Skill

Version: `v0.8.0`

## Skill name

14-factor-security-privacy

## Purpose

Use `14-factor-security-privacy` to audit and improve security, privacy, secrets, permission boundaries, dependency hygiene, data handling, and release safety for product engineering repositories. It is designed as a practical product-readiness layer, not a heavy compliance program.

## When to use

Use this Skill when:

- A project handles user data, API keys, credentials, uploaded files, tokens, logs, model outputs, or third-party integrations.
- A repository is moving from demo to public release and needs a security/privacy pass.
- A product includes Agent tools, MCP tools, RAG pipelines, CI/CD workflows, web apps, CLIs, or hosted services.
- A user asks whether the project is safe to publish, deploy, share, or open source.
- Another Factor Skill finds issues around permissions, logs, supply chain, secrets, or data retention.

## When not to use

Do not use this Skill as legal advice, formal compliance certification, penetration testing, or a replacement for organization-specific security review. For regulated domains, use it as a preparation checklist before specialist review.

## Inputs

Inspect README, configuration files, environment variable docs, `.gitignore`, examples, logs, workflows, package manifests, lockfiles, Docker files, deployment docs, API/tool schemas, auth code, storage paths, data examples, and release notes.

## Workflow

1. Identify what data, credentials, files, tokens, and permissions the project touches.
2. Map trust boundaries across users, Agent, tools, workflows, storage, network calls, and third-party services.
3. Check repository hygiene: secrets, fixtures, generated artifacts, logs, ignored files, and sample configs.
4. Review dependency, workflow, and release risks.
5. Score with `scoring-rubric.md`.
6. Produce an audit report using `audit-report-template.md`.
7. Produce a prioritized mitigation plan using `refactor-plan-template.md`.
8. Pair with a domain Skill such as `12-factor-agents`, `12-factor-app`, `7-factor-mcp`, `8-factor-github-actions`, or `9-factor-rag` when technical depth is required.

## Fourteen factors

1. **Asset Inventory** — Data, credentials, files, and privileged operations are identified.
2. **Secret Hygiene** — Real secrets are not committed, logged, or embedded in examples.
3. **Configuration Safety** — `.env.example`, defaults, and docs avoid unsafe production settings.
4. **Permission Boundaries** — Tools, tokens, workflows, and APIs use least privilege.
5. **Input Validation** — User, model, file, URL, and tool inputs are validated before use.
6. **Output and Log Safety** — Logs, reports, traces, and examples avoid sensitive leakage.
7. **Data Handling** — Retention, deletion, anonymization, and storage expectations are documented.
8. **Dependency Hygiene** — Dependencies, lockfiles, and supply-chain risks are visible and updatable.
9. **CI/CD Security** — Workflows avoid overbroad tokens, unsafe pull request execution, and secret exposure.
10. **Agent and Tool Safety** — Agent tool calls have clear contracts, guardrails, and failure handling.
11. **MCP and Integration Safety** — External tools and MCP servers document schemas, permissions, and trust limits.
12. **RAG and Knowledge Safety** — Retrieval pipelines avoid leaking private data and track source boundaries.
13. **Release and Disclosure Readiness** — Security notes, support contact, and vulnerability reporting are present.
14. **Validation Evidence** — The project includes lightweight checks or manual evidence for high-risk areas.

## Scoring

Use `scoring-rubric.md`. Score each factor from 0 to 5, then convert to a 100-point readiness score.

## Output format

Return:

1. Security/privacy scope summary.
2. Trust boundary map.
3. 14-factor scorecard.
4. Critical release blockers.
5. Secrets and data-handling findings.
6. CI/CD, dependency, and tool-permission findings.
7. Prioritized mitigation plan.
8. Validation results or validation limits.
9. Recommended paired Skills.

## Example calls

See `usage-examples.md`.

## Version record

- `v0.8.0`: Added as a first-class security/privacy readiness Skill.
