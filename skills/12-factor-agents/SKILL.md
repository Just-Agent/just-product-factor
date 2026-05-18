# 12-factor-agents Skill

## Name

12-factor-agents

## Purpose

Audit and refactor LLM Agent systems for reliability, control, context discipline, tool safety, human-in-the-loop behavior, and production readiness.

## When to use

- Agent runtime design
- Tool calling workflows
- Memory and state handling
- Human approval loops
- Long-running task control
- Agent productization

## When not to use

- Static HTML polish only
- Pure CI configuration with no Agent logic
- General app deployment where no Agent exists

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

- Prompt and instruction boundaries
- Context engineering
- Tool contracts
- Control flow
- State and memory
- Human-in-the-loop
- Observability
- Error recovery
- Evaluation
- Release readiness

## Refactor priorities

1. Make the Agent behavior explicit
2. Make tools safe and typed
3. Make state inspectable
4. Add evaluation and traces
5. Improve docs and examples

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

