# 10-factor-html Skill

## Name

10-factor-html

## Purpose

Audit and improve HTML pages for semantic quality, responsiveness, accessibility, SEO, performance, visual polish, and deployability.

## When to use

- Landing pages
- Static HTML pages
- README preview pages
- Generated Agent UI
- Documentation pages

## When not to use

- Backend-only services
- Unrendered design specs
- Native mobile UI

## Inputs

Ask for or inspect:

- README and docs
- source files
- examples and recipes
- configuration files
- tests and validation scripts
- CI/CD workflow files
- logs, changelog, release notes, or version history

## Workflow

1. Identify the project goal and user-facing promise.
2. Inspect available files.
3. Apply `checklist.md`.
4. Score with `scoring-rubric.md`.
5. Produce an audit report using `audit-report-template.md`.
6. Produce a refactor plan using `refactor-plan-template.md`.
7. Prioritize changes by product value and release readiness.
8. Validate changes if the environment allows.

## Review dimensions

- Semantic structure
- Responsive layout
- Accessibility
- SEO metadata
- Performance
- Content clarity
- Visual hierarchy
- Asset handling
- Deployability
- Maintainability

## Refactor priorities

1. Fix semantic HTML
2. Make it responsive
3. Improve accessibility
4. Add SEO metadata
5. Polish visuals and performance

## Output format

Return:

1. Summary
2. Scorecard
3. Critical findings
4. Recommended changes
5. Refactor plan
6. Validation plan
7. Next iteration suggestions

## Example calls

See `usage-examples.md`.

## Version

v0.5.0

## Agent manifest

This Skill includes a machine-readable `skill.json` manifest so an Agent can quickly identify triggers, expected inputs, expected outputs, required files, and the review protocol before reading the full markdown pack.

