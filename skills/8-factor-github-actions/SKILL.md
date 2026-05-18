# 8-factor-github-actions Skill

## Name

8-factor-github-actions

## Purpose

Audit and improve GitHub Actions workflows for safe automation, clear triggers, least privilege, caching, reuse, and release readiness.

## When to use

- CI workflows
- Release workflows
- GitHub Pages deployment
- Scheduled automation
- Repository dispatch workflows

## When not to use

- Local scripts with no GitHub integration
- Non-GitHub CI systems unless adapting principles

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

- Trigger design
- Permissions
- Secrets handling
- Caching
- Build/test steps
- Artifacts
- Failure messages
- Reuse and maintainability

## Refactor priorities

1. Set least permissions
2. Make triggers explicit
3. Add validation jobs
4. Improve cache/artifacts
5. Document usage

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

