# 13-factor-product-readiness Skill

## Name

13-factor-product-readiness

## Purpose

Audit and refactor a repository so it feels like a shippable product rather than a prototype. This Skill focuses on positioning, onboarding, product surface, docs, examples, validation, release packaging, support loops, and user retention details.

## When to use

Use this Skill when:

- The user wants to make a project more publishable, usable, and memorable.
- A repository already runs, but its product story, onboarding, examples, or release quality are weak.
- The project spans multiple domains and needs a top-level product readiness pass.
- The user asks for "爆款开源产品", release readiness, launch readiness, or product polish.

## When not to use

Do not use this Skill as the only review for deeply technical subsystems. Pair it with a domain Skill such as `12-factor-agents`, `12-factor-app`, `10-factor-html`, `8-factor-github-actions`, `9-factor-rag`, `7-factor-mcp`, or `11-factor-cli` when implementation quality also needs detailed review.

## Inputs

Inspect README, product positioning, screenshots or demos, examples, quickstart, docs, CLI/API surface, configuration, tests, workflows, changelog, release notes, roadmap, issue templates, and any onboarding or support material.

## Workflow

1. Identify the target user, product promise, and primary use case.
2. Check whether a new user can understand value within 30 seconds.
3. Check whether a new user can run the project within 5 minutes.
4. Review examples, docs, validation commands, release files, and support loops.
5. Score with `scoring-rubric.md`.
6. Produce an audit report using `audit-report-template.md`.
7. Produce a prioritized launch-readiness refactor plan using `refactor-plan-template.md`.
8. Recommend a primary domain Skill for deeper technical follow-up if needed.

## Review dimensions

- Product promise and target user
- First-run onboarding and quickstart
- Demo, screenshots, examples, and recipes
- Installation, configuration, and validation path
- Error messages, logs, and failure recovery
- Documentation structure and API/CLI clarity
- Release packaging and version discipline
- GitHub repository polish and contribution loop
- Security, privacy, and operational disclaimers
- Roadmap, changelog, and support loop
- Differentiation and memorability
- Agent-native usage path
- Retention details that make users come back

## Scoring

Use `scoring-rubric.md`. Score each factor from 0 to 5, then convert to a 100-point score.

## Output format

Return:

1. Product readiness summary.
2. Target user and core promise diagnosis.
3. 13-factor scorecard.
4. Critical launch blockers.
5. High-leverage product polish changes.
6. Release-readiness refactor plan.
7. Suggested paired technical Skills.
8. Validation results or validation limits.
9. Next iteration recommendation.

## Example calls

See `usage-examples.md`.

## Version

v0.5.0
