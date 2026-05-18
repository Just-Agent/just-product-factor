# Skill Prompt Renderer

`render_skill_prompt.py` turns a Factor Skill folder into a single copyable prompt pack. Use it when an Agent, a coding assistant, or a CI task needs the full review instructions without manually opening every Skill file.

## Usage

```bash
python scripts/render_skill_prompt.py 12-factor-agents --target ./my-agent --out ./tmp/12-factor-agents-prompt.md
```

Print to stdout:

```bash
python scripts/render_skill_prompt.py 13-factor-product-readiness --target ./my-repo
```

## Why it exists

A Factor Skill is intentionally split into focused files:

- `SKILL.md`
- `checklist.md`
- `scoring-rubric.md`
- `audit-report-template.md`
- `refactor-plan-template.md`
- `usage-examples.md`
- `skill.json`

The renderer keeps that maintainable source structure while producing a one-shot prompt for repeated audits.

## Recommended loop

1. Pick the closest Skill.
2. Render the prompt pack.
3. Ask the Agent to inspect the target project.
4. Produce an audit report and refactor plan.
5. Apply the changes.
6. Run validation.
7. Repeat in the next version.
