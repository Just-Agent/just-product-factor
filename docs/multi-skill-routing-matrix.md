# Multi-Skill Routing Matrix

Use this matrix when a project touches more than one domain.

| Project signal | Primary Skill | Secondary Skill |
|---|---|---|
| LLM tool calls, memory, planner, human approval | `12-factor-agents` | `12-factor-app` |
| SaaS app, API, service, deployment | `12-factor-app` | `8-factor-github-actions` |
| Static page, landing page, docs page, generated HTML | `10-factor-html` | `12-factor-app` |
| CI/CD YAML, release workflow, Pages deployment | `8-factor-github-actions` | `12-factor-app` |
| Retrieval, chunking, embeddings, citations, evaluation | `9-factor-rag` | `12-factor-agents` |
| MCP server/client, tool schema, permissions | `7-factor-mcp` | `12-factor-agents` |
| CLI commands, help text, errors, installability | `11-factor-cli` | `12-factor-app`, `6-factor-docs` |
| README, docs tree, quickstart, examples, handoff prompts | `6-factor-docs` | `13-factor-product-readiness`, domain-specific Skill |

## Routing rule

Pick one primary Skill to avoid scattered reviews. Add at most two secondary Skills when the target project clearly spans multiple domains.

## Output rule

The final report should include:

- Primary Skill score
- Secondary Skill notes
- Top five release blockers
- Top five product polish improvements
- Validation commands executed
- Assumptions and unknowns


## Product readiness overlay

| Project condition | Primary Skill | Secondary Skills |
|---|---|---|
| Useful demo that needs to become a product | `13-factor-product-readiness` | `12-factor-app`, `11-factor-cli`, `8-factor-github-actions` |
| Open-source launch preparation | `13-factor-product-readiness` | domain-specific Skill based on implementation |
| Agent-native project needing better adoption | `13-factor-product-readiness` | `12-factor-agents`, `10-factor-html`, `8-factor-github-actions`, `6-factor-docs` |


## Evaluation and regression routing

Use `5-factor-evals` as the primary Skill when the request is about golden cases, regression tests, benchmarks, validation harnesses, failure taxonomies, or release gates. Use it as a secondary Skill after `12-factor-agents`, `9-factor-rag`, `10-factor-html`, or `13-factor-product-readiness` when the main review needs measurable release confidence.
