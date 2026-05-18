# Multi-Skill Composition Guide

Some repositories are not cleanly covered by one Factor Skill. A release-ready Agent-native product may need product readiness, Agent architecture, security, observability, docs, evals, and workflow checks together.

Use multi-Skill composition when the user asks for one of these outcomes:

- “turn this repo into a publishable product”
- “prepare this Agent app for release”
- “audit this RAG system end to end”
- “make this project debuggable and safe before deployment”
- “choose the right Factor Skills and create a review plan”

## Recommended composition patterns

| Project type | Primary Skill | Secondary Skills |
|---|---|---|
| Agent product | `12-factor-agents` | `5-factor-evals`, `14-factor-security-privacy`, `15-factor-observability`, `6-factor-docs` |
| App / SaaS | `12-factor-app` | `13-factor-product-readiness`, `14-factor-security-privacy`, `15-factor-observability`, `8-factor-github-actions` |
| RAG product | `9-factor-rag` | `5-factor-evals`, `14-factor-security-privacy`, `15-factor-observability`, `6-factor-docs` |
| MCP server | `7-factor-mcp` | `14-factor-security-privacy`, `15-factor-observability`, `11-factor-cli`, `6-factor-docs` |
| HTML / landing page | `10-factor-html` | `13-factor-product-readiness`, `6-factor-docs`, `15-factor-observability` |
| CI/CD release pipeline | `8-factor-github-actions` | `14-factor-security-privacy`, `15-factor-observability`, `13-factor-product-readiness` |

## Dependency-free composer

Generate a composed review workspace:

```bash
python scripts/compose_factor_review.py \
  "prepare this Agent RAG product for public release" \
  --root . \
  --target ./examples/sample-agent-project \
  --max-skills 4 \
  --out ./tmp/composed-review
```

Force a specific Skill set:

```bash
python scripts/compose_factor_review.py \
  "make this deployment safer and easier to debug" \
  --root . \
  --skills 12-factor-app,14-factor-security-privacy,15-factor-observability,8-factor-github-actions \
  --out ./tmp/app-release-review
```

The composer creates:

- `review-plan.md`
- `review-plan.json`
- `handoff-prompt.md`

## Agent protocol

1. Use the first selected Skill as the primary lens.
2. Use secondary Skills only for their relevant dimensions.
3. Avoid duplicate findings by merging similar issues.
4. Resolve conflicts by prioritizing safety, correctness, deployability, and user experience.
5. Return one combined audit report and one prioritized refactor plan.
6. Record validation evidence and limits honestly.

## Conflict resolution

| Conflict | Resolution |
|---|---|
| Product polish vs security | Security wins before public release. |
| Observability vs privacy | Keep useful diagnostics, but redact or summarize sensitive data. |
| Fast release vs eval confidence | Add minimum smoke/golden checks before release. |
| CLI simplicity vs debug detail | Keep default output simple; expose verbose/debug mode. |
| Agent autonomy vs human approval | Human approval wins for destructive or high-risk operations. |
