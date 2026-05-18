# 14-factor-security-privacy Audit Report

## Project

- Name:
- Version or commit:
- Reviewer:
- Date:
- Paired Skills:

## Scope

Describe the product surface, data handled, integrations, tools, workflows, and release context reviewed.

## Trust boundary map

| Boundary | Assets involved | Risk | Current control | Gap |
|---|---|---|---|---|
| User input -> app/tool |  |  |  |  |
| Agent -> tool/runtime |  |  |  |  |
| CI/CD -> release artifact |  |  |  |  |
| Data source -> public output |  |  |  |  |

## Scorecard

| Factor | Score | Evidence | Gap | Priority |
|---|---:|---|---|---|
| Asset Inventory |  |  |  |  |
| Secret Hygiene |  |  |  |  |
| Configuration Safety |  |  |  |  |
| Permission Boundaries |  |  |  |  |
| Input Validation |  |  |  |  |
| Output and Log Safety |  |  |  |  |
| Data Handling |  |  |  |  |
| Dependency Hygiene |  |  |  |  |
| CI/CD Security |  |  |  |  |
| Agent and Tool Safety |  |  |  |  |
| MCP and Integration Safety |  |  |  |  |
| RAG and Knowledge Safety |  |  |  |  |
| Release and Disclosure Readiness |  |  |  |  |
| Validation Evidence |  |  |  |  |

Total score: `/70`

## Critical blockers

1.
2.
3.

## Secrets and sensitive-data review

- Search commands or manual checks performed:
- Findings:
- Redaction or rotation needed:

## CI/CD and dependency review

- Workflow permission issues:
- Dependency or lockfile issues:
- Release artifact issues:

## Agent/tool safety findings

- Tool permission concerns:
- Prompt/tool escalation risks:
- Human approval gaps:

## Validation results

List commands run and outcomes. If commands could not run, explain the exact limitation.

## Recommendation

Summarize whether the project is safe to publish, safe to demo only, or blocked pending mitigation.
