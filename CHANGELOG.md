# Changelog

## v0.9.0 - 2026-05-18

### Added

- Added `15-factor-observability` as a first-class Factor Skill for logs, metrics, traces, validation artifacts, failure diagnostics, privacy-safe debugging, release evidence, and Agent handoff readiness.
- Added `scripts/compose_factor_review.py` to generate a composed multi-Skill review workspace with `review-plan.md`, `review-plan.json`, and `handoff-prompt.md`.
- Added `docs/observability-playbook.md` and `docs/multi-skill-composition-guide.md`.
- Added `templates/multi-skill-review-plan-template.md`.
- Added `examples/observability-audit-prompt.md` and `examples/composed-review-prompt.md`.

### Changed

- Updated README, root `SKILL.md`, registries, Skill manifests, validation script, selector, and GitHub Actions workflow for `v0.9.0`.
- Updated `product-factor-skills.json` and `skills.json` to include twelve bundled Skills.
- Updated validation to require `15-factor-observability`, the multi-Skill composer, and observability support files.

### Fixed

- Fixed the malformed v0.8.0 date entry in `logs/version-history.md` while adding v0.9.0.
- Corrected README status so it reflects the current release instead of an older v0.5.0 note.

### Validation

- Ran `python scripts/scan_factor_project.py .`.
- Ran `python -m py_compile scripts/*.py`.
- Ran Skill selector, multi-Skill composer, prompt renderer, catalog exporter, audit runner, and release zip smoke tests locally.

## v0.8.0 - Security and privacy readiness Skill

### Added

- Added `14-factor-security-privacy` as a first-class Factor Skill for secrets hygiene, permission boundaries, input/output safety, data handling, dependency hygiene, CI/CD security, Agent/tool safety, MCP/RAG integration risk, disclosure readiness, and validation evidence.
- Added `SECURITY.md` for vulnerability reporting guidance and maintainer release safety checks.
- Added `docs/security-privacy-playbook.md`, `templates/security-review-template.md`, and `examples/security-privacy-audit-prompt.md`.

### Changed

- Updated root README and root `SKILL.md` routing to include the new security/privacy review path.
- Updated `product-factor-skills.json`, `skills.json`, and all Skill manifests to version `v0.8.0`.
- Updated validation to require eleven bundled Skills and security/privacy support files.
- Updated GitHub Actions smoke tests to render and select the new security/privacy Skill.

### Validation

- Ran `python scripts/scan_factor_project.py .`.
- Ran `python -m py_compile scripts/*.py`.
- Ran Skill selector, prompt renderer, catalog exporter, audit runner, and release zip smoke tests locally.



## v0.7.0 - 2026-05-18

### Added
- Added `5-factor-evals` for evaluation quality contracts, golden cases, regression loops, failure taxonomies, and release gates.
- Added `scripts/select_factor_skill.py` to recommend primary and secondary Skills from a user request and optional target project signals.
- Added `docs/skill-selection-engine.md` and `examples/skill-selection-prompt.md`.

### Changed
- Updated README, root `SKILL.md`, routing docs, registries, scanner, workflow, and all Skill manifests to `v0.7.0`.
- Expanded validation coverage to require at least ten bundled Skills and smoke-test Skill selection.

### Fixed
- Closed the previous gap where broad requests required manual routing before an Agent could choose a Skill.
- Made evaluation and release confidence a first-class reusable standard instead of scattering it across Agent, RAG, and product-readiness reviews.

### Validation
- Ran `python scripts/scan_factor_project.py .` successfully.
- Ran `python scripts/select_factor_skill.py "audit this RAG app for retrieval quality and regression tests" --root . --top 5 --json ./tmp/skill-selection.json --markdown ./tmp/skill-selection.md` successfully.
- Ran `python scripts/render_skill_prompt.py 5-factor-evals --target ./examples/sample-agent-project --out ./tmp/evals-prompt.md` successfully.
- Ran `python scripts/export_skill_catalog.py . --markdown ./tmp/generated-skill-catalog.md --json ./tmp/generated-skill-catalog.json` successfully.
- Ran `python scripts/build_release_zip.py . --out /tmp/product-factor-skills-smoke.zip` successfully.
- Ran `python -m py_compile scripts/*.py` successfully.

## v0.6.0 - 2026-05-18

### Added
- Added `6-factor-docs` for documentation positioning, first-run onboarding, information architecture, examples, accuracy, maintenance, and Agent handoff readiness.
- Added `scripts/export_skill_catalog.py` for generating markdown and JSON catalogs from Skill manifests.
- Added `docs/documentation-readiness-playbook.md`, `docs/skill-catalog-exporter.md`, and `examples/docs-audit-prompt.md`.
- Added GitHub issue templates and a pull request template.

### Changed
- Updated README, root `SKILL.md`, routing docs, registries, scanner, workflow, and all Skill manifests to `v0.6.0`.
- Expanded validation coverage to require at least nine bundled Skills and smoke-test catalog export.

### Fixed
- Reduced ambiguity around when to use product readiness versus documentation readiness.
- Strengthened collaboration workflow for new Skill requests, bugs, and documentation improvements.

### Validation
- Ran `python scripts/scan_factor_project.py .` successfully.
- Ran `python scripts/export_skill_catalog.py . --markdown ./tmp/generated-skill-catalog.md --json ./tmp/generated-skill-catalog.json` successfully.
- Ran `python scripts/render_skill_prompt.py 6-factor-docs --target ./examples/sample-agent-project --out ./tmp/docs-prompt.md` successfully.
- Ran `python scripts/build_release_zip.py . --out /tmp/product-factor-skills-smoke.zip` successfully.
- Ran `python -m py_compile scripts/*.py` successfully.

## v0.5.0 - 2026-05-18

### Added
- Added `13-factor-product-readiness` for launch readiness, onboarding, product polish, release discipline, open-source credibility, and repeat-use value.
- Added `scripts/render_skill_prompt.py` to render a complete one-shot Agent prompt from any Factor Skill.
- Added `docs/skill-prompt-renderer.md`, `docs/product-readiness-playbook.md`, and `examples/product-readiness-audit-prompt.md`.

### Changed
- Updated README, root `SKILL.md`, registries, scanner, and validation workflow for the new product readiness workflow.
- Updated all Skill manifests and versions to `v0.5.0`.
- Fixed the GitHub Actions validation step to use a valid multi-line `run: |` block.
- Updated release zip builder to exclude temporary audit output directories.

### Fixed
- Corrected validation workflow syntax so repository scanning, audit runner smoke test, prompt renderer smoke test, and release zip smoke test can run in CI.

### Validation
- Ran `python scripts/scan_factor_project.py .` successfully.
- Ran `python scripts/render_skill_prompt.py 13-factor-product-readiness --target ./examples/sample-agent-project --out ./tmp/product-readiness-prompt.md` successfully.
- Ran `python scripts/build_release_zip.py . --out /tmp/product-factor-skills-smoke.zip` successfully.
- Ran `python -m py_compile scripts/*.py` successfully.

## v0.4.0 - 2026-05-18

### Added
- Added `scripts/run_skill_audit.py` to generate repeatable audit workspaces for target projects.
- Added `docs/skill-audit-runner.md` with runner usage and output conventions.
- Added `docs/multi-skill-routing-matrix.md` for choosing primary and secondary Factor Skills.
- Added `guides/repeatable-optimization-loop.md` for multi-version project improvement.
- Added `examples/run-skill-audit-example.md` and a tiny `examples/sample-agent-project/` smoke-test fixture.

### Changed
- Updated README and root `SKILL.md` to explain the audit runner workflow.
- Updated validation workflow to smoke-test audit package generation.
- Updated all manifests and Skill versions to `v0.4.0`.

### Fixed
- Strengthened validation coverage for new support docs and runner scripts.

## v0.4.0 - 2026-05-18

### Added

- Added machine-readable `skill.json` manifests for every Factor Skill.
- Added root `product-factor-skills.json` registry and synchronized `skills.json`.
- Added `schemas/skill-manifest.schema.json` for future manifest validation.
- Added `scripts/generate_factor_skill.py` to create new `xx-factor-*` Skill skeletons.
- Added `docs/agent-invocation-protocol.md`, `docs/skill-authoring-guide.md`, and `docs/release-checklist.md`.
- Added more copyable examples for complete product audit, GitHub Actions audit, RAG audit, and new Skill generation.

### Changed

- Upgraded version from `v0.1.0` to `v0.4.0`.
- Expanded README with the manifest-first Agent invocation protocol.
- Strengthened the root `SKILL.md` with routing rules and output format.
- Strengthened `scripts/scan_factor_project.py` to validate manifests, registry membership, version consistency, README keywords, logs, and workflow presence.
- Updated GitHub Actions validation workflow to run the stronger scanner and test the Skill generator dry run.
- Updated each Skill to reference its new `skill.json` manifest.

### Fixed

- Reduced ambiguity around how an Agent should select and invoke a Skill.
- Made version consistency checkable across root files, registry, and Skill manifests.

### Validation

- Ran `python scripts/scan_factor_project.py .` successfully.
- Ran `python scripts/generate_factor_skill.py xx-factor-cli --title "xx-factor-cli" --category cli --dry-run` successfully.

## v0.1.0 - 2026-05-18

### Added

- Initial `product-factor-skills` repository.
- Added base Skills: `12-factor-agents`, `12-factor-app`, `10-factor-html`, `8-factor-github-actions`, `9-factor-rag`, and `7-factor-mcp`.
- Added checklists, scoring rubrics, audit templates, refactor plan templates, usage examples, validation script, logs, and GitHub Actions workflow.
