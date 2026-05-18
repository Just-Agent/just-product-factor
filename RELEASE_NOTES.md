# Release Notes

## v0.9.0 - 2026-05-18

`v0.9.0` makes product-factor-skills more useful for real release work by adding observability as a first-class review standard and by adding a dependency-free multi-Skill composer.

### Highlights

- New `15-factor-observability` Skill for runtime visibility, debugging, release evidence, validation artifacts, logs, metrics, traces, and Agent handoff readiness.
- New `scripts/compose_factor_review.py` for producing a repeatable multi-Skill review plan instead of manually stitching several Skills together.
- New observability playbook and multi-Skill composition guide.
- New composed review template and examples.
- Expanded CI smoke tests and local validation coverage.

### Upgrade notes

- Repository version is now `v0.9.0`.
- All bundled `skills/*/skill.json` manifests now use `v0.9.0`.
- `scripts/scan_factor_project.py` now expects twelve bundled Skills.

### Validation summary

Validated with the repository scanner, Python compilation, Skill selector, multi-Skill composer, prompt renderer, catalog exporter, audit runner, and release zip builder.

## Summary

`v0.8.0` adds security and privacy readiness as a first-class Factor Skill. The repository can now guide Agents through release blockers around secrets, credentials, permissions, data handling, dependency hygiene, CI/CD safety, Agent tool risk, MCP/RAG integration boundaries, and validation evidence.

## Highlights

- New Skill: `14-factor-security-privacy`.
- New support docs: `docs/security-privacy-playbook.md`.
- New template: `templates/security-review-template.md`.
- New example prompt: `examples/security-privacy-audit-prompt.md`.
- New repository security policy: `SECURITY.md`.
- Validation now expects eleven bundled Skills.

## Upgrade notes

Use `14-factor-security-privacy` before public release, hosted deployment, open-source distribution, or any refactor that touches tools, workflows, credentials, storage, logs, or private/public data boundaries.

## Validation

Local validation commands were executed and recorded in `logs/iteration-log.md`.

# Release Notes - v0.7.0

v0.7.0 adds a first-class evaluation and release-confidence layer to `product-factor-skills`.

The main additions are:

- `5-factor-evals` for quality contracts, golden cases, regression loops, failure taxonomy, and release gates.
- `scripts/select_factor_skill.py` for dependency-free routing from broad user requests or target project signals.
- `docs/skill-selection-engine.md` and `examples/skill-selection-prompt.md` to help Agents pick primary and secondary Skills before an audit.

This release makes the repository more Agent-callable because broad requests can now start with a repeatable selection step instead of relying only on manual judgment.

## Validation

- `python scripts/scan_factor_project.py .` passed.
- `python scripts/select_factor_skill.py "audit this RAG app for retrieval quality and regression tests" --root . --top 5 --json ./tmp/skill-selection.json --markdown ./tmp/skill-selection.md` passed.
- `python scripts/render_skill_prompt.py 5-factor-evals --target ./examples/sample-agent-project --out ./tmp/evals-prompt.md` passed.
- `python scripts/export_skill_catalog.py . --markdown ./tmp/generated-skill-catalog.md --json ./tmp/generated-skill-catalog.json` passed.
- `python scripts/build_release_zip.py . --out /tmp/product-factor-skills-smoke.zip` passed.
- `python -m py_compile scripts/*.py` passed.
