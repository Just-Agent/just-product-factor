# Skill Audit Runner

`run_skill_audit.py` is a small standard-library utility that prepares a repeatable audit workspace for any target project.

It does **not** replace an Agent review. It creates the structure an Agent should fill in so reviews are consistent across projects and Factor Skills.

## Usage

```bash
python scripts/run_skill_audit.py   --repo .   --target ./examples/sample-agent-project   --skill 12-factor-agents   --out ./tmp/agent-audit
```

## Outputs

The runner creates:

```text
audit-brief.md
  Selected Skill, project signals, top files, and recommended Agent workflow.

audit-report.md
  A copy of the selected Skill audit report template.

refactor-plan.md
  A copy of the selected Skill refactor plan template.

validation-summary.md
  Shared validation template.

decision-log.md
  Shared decision log template.

audit-summary.json
  Machine-readable summary for later automation.
```

## Recommended Agent loop

1. Generate the audit package.
2. Ask the Agent to read `audit-brief.md` first.
3. Ask the Agent to inspect the target project.
4. Ask the Agent to fill `audit-report.md` and `refactor-plan.md`.
5. Run project validation commands where possible.
6. Record validation results in `validation-summary.md`.
7. Record assumptions and tradeoffs in `decision-log.md`.

## Why this matters

A reusable Skill is useful only when its output is repeatable. The audit runner turns Skill packs into a practical workflow that can be used across Agent projects, apps, HTML pages, GitHub Actions workflows, RAG systems, MCP servers, and CLI tools.
