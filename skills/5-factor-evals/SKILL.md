# 5-factor-evals

Version: `v0.7.0`

## Skill name

5-factor-evals

## Purpose

Use `5-factor-evals` to audit and improve evaluation, regression testing, benchmark, and release confidence systems for Agent-native products. It turns vague quality claims into repeatable checks that can be run before and after refactors.

## When to use

Use this Skill when:

- A project uses LLMs, Agents, RAG, tools, prompts, generated UI, or automated workflows and needs measurable quality gates.
- A user asks whether changes made the product better or worse.
- A repository has examples, demos, or tests but no stable acceptance suite.
- Releases are risky because there is no baseline, no golden cases, no regression log, or no failure taxonomy.
- Multiple Factor Skills produce recommendations and the team needs a shared validation layer.

## When not to use

Do not use this Skill as a replacement for domain review. Pair it with the relevant primary Skill such as `12-factor-agents`, `9-factor-rag`, `10-factor-html`, `11-factor-cli`, or `13-factor-product-readiness`.

## Expected inputs

- Target project files, README, examples, tests, scripts, and CI configuration.
- Existing benchmark cases, prompt examples, screenshots, logs, or evaluation notes.
- Product goals, user journeys, acceptance criteria, and known failure cases.
- Previous audit reports or refactor plans if available.

## Workflow

1. Identify the product behavior that must stay reliable.
2. Extract or propose representative golden cases.
3. Define pass/fail criteria before changing code or prompts.
4. Review existing tests, smoke checks, fixtures, examples, CI gates, and logs.
5. Score the project with `scoring-rubric.md`.
6. Produce an audit report using `audit-report-template.md`.
7. Produce a refactor plan using `refactor-plan-template.md`.
8. Recommend the smallest useful evaluation harness that can run repeatedly.
9. Record validation results and validation limits honestly.

## Five factors

1. **Quality Contract** — The project defines what good output means in user-facing terms.
2. **Golden Cases** — The project keeps representative examples, fixtures, and expected outcomes.
3. **Regression Loop** — The project can detect whether a change breaks important behavior.
4. **Failure Taxonomy** — The project names common failure modes and maps them to fixes.
5. **Release Gates** — The project connects evaluations to CI, release notes, and go/no-go decisions.

## Output format

Return:

1. Selected evaluation scope and why.
2. Current eval maturity scorecard.
3. Missing golden cases and critical validation gaps.
4. Proposed minimum evaluation harness.
5. Regression and failure taxonomy plan.
6. Release gate recommendations.
7. Validation results or validation limits.

## Example calls

```text
Use the 5-factor-evals skill to audit this Agent project for golden cases, regression tests, failure taxonomy, and release gates.

Use the 5-factor-evals skill to add a repeatable evaluation plan before we refactor this RAG pipeline.

Use the 5-factor-evals skill as a secondary review after 12-factor-agents and 9-factor-rag.
```

## Version record

- `v0.7.0`: Added as a first-class evaluation and regression confidence Skill.
