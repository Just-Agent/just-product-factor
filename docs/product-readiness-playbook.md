# Product Readiness Playbook

Use this playbook when a repository already has useful code or standards, but needs to become a product-quality open-source project.

## Productization order

1. Make the promise clear.
2. Make the first run successful.
3. Make examples copyable.
4. Make validation repeatable.
5. Make release artifacts reproducible.
6. Make contribution and support paths visible.
7. Make the Agent-native workflow explicit.

## Recommended Skill pairing

| Situation | Primary Skill | Secondary Skills |
|---|---|---|
| Demo becoming product | `13-factor-product-readiness` | `12-factor-app`, `11-factor-cli` |
| Agent repo launch | `13-factor-product-readiness` | `12-factor-agents`, `8-factor-github-actions` |
| Static site or landing page | `13-factor-product-readiness` | `10-factor-html` |
| Automation project | `13-factor-product-readiness` | `8-factor-github-actions`, `11-factor-cli` |
| RAG product | `13-factor-product-readiness` | `9-factor-rag`, `12-factor-app` |
| MCP server | `13-factor-product-readiness` | `7-factor-mcp`, `11-factor-cli` |

## Output expectation

A product readiness audit should identify launch blockers first, then polish opportunities, then repeat-use improvements. Avoid spending effort on visual polish if the install path, quickstart, or validation path is broken.
