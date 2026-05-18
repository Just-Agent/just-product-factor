# Skill Routing Guide

This guide helps an Agent choose the right Factor Skill before starting an audit.

## Routing table

| User asks about | Start with | Add-on Skills |
|---|---|---|
| Agent workflow, memory, tools, human approval | `12-factor-agents` | `11-factor-cli` if the Agent ships a CLI |
| SaaS, API, web app, deployability | `12-factor-app` | `8-factor-github-actions`, `11-factor-cli` |
| Static HTML, landing page, generated preview | `10-factor-html` | `12-factor-app` if deployability matters |
| CI/CD, GitHub Pages, scheduled automation | `8-factor-github-actions` | `12-factor-app` |
| RAG, retrieval, chunks, citations | `9-factor-rag` | `12-factor-agents` |
| MCP tools, server/client schema | `7-factor-mcp` | `12-factor-agents` |
| Command-line UX, packaging, help text | `11-factor-cli` | `12-factor-app`, `6-factor-docs` |
| README, docs, quickstart, examples, Agent handoff prompts | `6-factor-docs` | `13-factor-product-readiness`, domain-specific Skill |

## Selection protocol

1. Identify the primary user-facing surface.
2. Choose the most specific Skill for that surface.
3. Add secondary Skills only when they improve the review.
4. Read `skill.json` first, then `SKILL.md`.
5. Produce one combined audit report when multiple Skills are used.

## Avoid over-routing

Do not run every Skill on every project. A focused review is more useful than a generic checklist dump.


## Evaluation and regression routing

Use `5-factor-evals` as the primary Skill when the request is about golden cases, regression tests, benchmarks, validation harnesses, failure taxonomies, or release gates. Use it as a secondary Skill after `12-factor-agents`, `9-factor-rag`, `10-factor-html`, or `13-factor-product-readiness` when the main review needs measurable release confidence.
