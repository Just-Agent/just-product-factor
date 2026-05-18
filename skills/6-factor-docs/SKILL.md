# 6-factor-docs Skill

Version: `v0.7.0`

## Purpose

Use this Skill to audit and refactor documentation systems so a new user, contributor, or Agent can understand the product promise, complete the first useful action, locate deeper references, and keep documentation trustworthy over time.

## When to use

Use this Skill when a project depends on README quality, docs pages, guides, API references, examples, onboarding flows, changelog discipline, or Agent handoff prompts.

Typical targets:

- Open-source repositories with weak README or docs
- Developer tools that need copy-paste onboarding
- Agent-native projects that need repeatable usage prompts
- SDKs, CLIs, APIs, SaaS products, RAG projects, MCP servers, and HTML templates
- Documentation sites or docs folders that need structure and maintenance rules

## When not to use

Do not use this Skill as a substitute for product implementation review, security review, or UI review. Pair it with `13-factor-product-readiness` when the product promise is unclear, with `11-factor-cli` when commands are the core interface, and with `10-factor-html` when the docs page itself needs HTML quality review.

## Inputs

- README and docs tree
- Examples, recipes, tutorials, API references, and screenshots if present
- CLI help, package metadata, workflow files, and release notes if documentation references them
- Known user questions, bug reports, or onboarding friction if available
- Target audience and desired first successful action if known

## Workflow

1. Identify the target reader and the first successful action.
2. Review README, docs navigation, examples, and references for consistency.
3. Apply `checklist.md` and gather evidence.
4. Score with `scoring-rubric.md`.
5. Produce `audit-report-template.md` output.
6. Produce `refactor-plan-template.md` output.
7. Recommend validation steps, such as copy-paste command checks and link checks.

## Review dimensions

1. Positioning and promise
2. First-run onboarding
3. Information architecture
4. Examples and recipes
5. Accuracy and maintenance
6. Agent handoff readiness

## Scoring

Use a 100-point score. Treat first-run onboarding, command accuracy, and stale documentation as blocking quality gates. A beautiful documentation site should not pass if a clean user cannot understand what to do next.

## Refactor priority

1. Make the product promise obvious.
2. Make the first useful action copy-pasteable.
3. Align README, docs, examples, and release notes.
4. Separate quickstart, concepts, reference, and recipes.
5. Add maintenance rules and validation checks.
6. Add Agent-ready usage prompts and output expectations.

## Output format

Return:

- Executive summary
- Documentation scorecard
- Reader journey diagnosis
- Missing or stale docs findings
- Example and quickstart review
- Agent handoff review
- Prioritized documentation refactor plan
- Validation commands and limits

## Example call

```text
Use the 6-factor-docs skill to audit this repository documentation for positioning, onboarding, information architecture, examples, accuracy, maintenance, and Agent handoff readiness.
```

## Version history

- `v0.6.0`: Added as a first-class Factor Skill for documentation systems and Agent handoff readiness.
