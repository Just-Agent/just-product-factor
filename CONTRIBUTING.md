# Contributing

Thanks for improving `product-factor-skills`.

## Contribution types

You can contribute:

- New Factor Skills.
- Better checklists.
- Better scoring rubrics.
- Better audit or refactor templates.
- Real before/after examples.
- Validation scripts.
- Documentation improvements.

## New Skill requirements

Every new Skill must include:

- `SKILL.md`
- `checklist.md`
- `scoring-rubric.md`
- `audit-report-template.md`
- `refactor-plan-template.md`
- `usage-examples.md`
- `skill.json`

Use:

```bash
python scripts/generate_factor_skill.py xx-factor-example --title "xx-factor-example" --category example
```

Then update:

- `product-factor-skills.json`
- `skills.json`
- `README.md`
- `CHANGELOG.md`
- `logs/file-manifest.md`

## Validation

Run:

```bash
python scripts/scan_factor_project.py .
```

The scanner should pass before release.
