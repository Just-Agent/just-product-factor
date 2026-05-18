# 12-factor-app Skill

## Name

12-factor-app

## Purpose

Audit and refactor apps for deployability, configuration, dependency hygiene, observability, release readiness, and user onboarding.

## When to use

- SaaS apps
- API services
- Full-stack apps
- CLI apps
- Deployable open-source products

## When not to use

- Single prompt templates
- Pure model evaluation with no app surface
- Documents with no runtime

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

- Installability
- Configuration
- Dependencies
- Build and runtime scripts
- Logging
- Error handling
- Documentation
- Examples
- CI/CD
- Release process

## Refactor priorities

1. Make it install and run
2. Make configuration clear
3. Add smoke tests
4. Improve docs/examples
5. Add release workflow

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

