# Iteration Log

## v0.9.0 - 2026-05-18

### Previous version

v0.8.0

### Current version

v0.9.0

### Added

- Added `skills/15-factor-observability/` with `SKILL.md`, checklist, scoring rubric, audit report template, refactor plan template, usage examples, and manifest.
- Added `scripts/compose_factor_review.py` for dependency-free multi-Skill review planning.
- Added `docs/observability-playbook.md` and `docs/multi-skill-composition-guide.md`.
- Added `templates/multi-skill-review-plan-template.md`.
- Added `examples/observability-audit-prompt.md` and `examples/composed-review-prompt.md`.

### Modified files

- `README.md`
- `SKILL.md`
- `VERSION`
- `CHANGELOG.md`
- `RELEASE_NOTES.md`
- `ROADMAP.md`
- `product-factor-skills.json`
- `skills.json`
- `scripts/scan_factor_project.py`
- `scripts/select_factor_skill.py`
- `.github/workflows/validate.yml`
- all existing `skills/*/skill.json`
- `docs/generated-skill-catalog.md`
- `docs/generated-skill-catalog.json`
- `logs/file-manifest.md`
- `logs/version-history.md`

### Fixed problems

- Observability is now a first-class review path instead of being scattered across app, Agent, CI/CD, and security reviews.
- Multi-Skill reviews now have a repeatable plan generator instead of relying on manual prompt stitching.
- Corrected older release status and version-history inconsistencies while updating the repository to `v0.9.0`.

### Skill experience improvements

- Agents can now route debugging, logging, traceability, release evidence, and validation artifact requests to `15-factor-observability`.
- Agents can generate a composed review package for complex product releases using `scripts/compose_factor_review.py`.
- README now documents the new observability path and multi-Skill composition workflow.

### Validation results

- `python scripts/scan_factor_project.py .` passed.
- `python -m py_compile scripts/*.py` passed.
- `python scripts/select_factor_skill.py "improve logs traces validation artifacts and debugging handoff" --root . --top 5 --json ./tmp/observability-selection.json --markdown ./tmp/observability-selection.md` passed.
- `python scripts/compose_factor_review.py "prepare this Agent product for release with observability and security" --root . --target ./examples/sample-agent-project --max-skills 4 --out ./tmp/composed-review` passed.
- `python scripts/render_skill_prompt.py 15-factor-observability --target ./examples/sample-agent-project --out ./tmp/observability-prompt.md` passed.
- `python scripts/export_skill_catalog.py . --markdown docs/generated-skill-catalog.md --json docs/generated-skill-catalog.json` passed.
- `python scripts/run_skill_audit.py --repo . --target ./examples/sample-agent-project --skill 12-factor-agents --out ./tmp/agent-audit` passed.
- `python scripts/build_release_zip.py . --out /tmp/product-factor-skills-smoke.zip` passed.

### Not completed

- No completed real-world observability audit report yet.
- Composer remains dependency-free and heuristic; it does not deeply understand source code.
- No dashboard, telemetry backend, or external observability integration is included.

### Next iteration direction

- Add completed sample audit reports for observability, security/privacy, docs, and product readiness.
- Add optional markdown link/reference checking with standard-library fallbacks.
- Add richer composition presets such as `agent-release`, `rag-release`, `mcp-release`, and `app-release`.


## v0.8.0 iteration

- Previous version: `v0.7.0`
- Current version: `v0.8.0`

### Added

- `skills/14-factor-security-privacy/` with complete Skill pack:
  - `SKILL.md`
  - `checklist.md`
  - `scoring-rubric.md`
  - `audit-report-template.md`
  - `refactor-plan-template.md`
  - `usage-examples.md`
  - `skill.json`
- `SECURITY.md`
- `docs/security-privacy-playbook.md`
- `templates/security-review-template.md`
- `examples/security-privacy-audit-prompt.md`

### Changed files

- `README.md`
- `SKILL.md`
- `VERSION`
- `CHANGELOG.md`
- `RELEASE_NOTES.md`
- `product-factor-skills.json`
- `skills.json`
- `scripts/scan_factor_project.py`
- `scripts/select_factor_skill.py`
- `.github/workflows/validate.yml`
- all existing `skills/*/skill.json` files for version alignment

### Fixed or improved

- Added a missing release-safety layer for secrets, privacy, permissions, and supply-chain risk.
- Improved Skill routing for projects that are technically ready but unsafe to publish.
- Strengthened CI validation around security/privacy docs and prompt rendering.

### Validation

- `python scripts/scan_factor_project.py .` passed.
- `python -m py_compile scripts/*.py` passed.
- `python scripts/select_factor_skill.py "check secrets workflow permissions data retention and deployment safety" --root . --top 5` passed.
- `python scripts/render_skill_prompt.py 14-factor-security-privacy --target ./examples/sample-agent-project --out ./tmp/security-privacy-prompt.md` passed.
- `python scripts/export_skill_catalog.py . --markdown ./tmp/generated-skill-catalog.md --json ./tmp/generated-skill-catalog.json` passed.
- `python scripts/run_skill_audit.py --repo . --target ./examples/sample-agent-project --skill 14-factor-security-privacy --out ./tmp/security-audit` passed.
- `python scripts/build_release_zip.py . --out /tmp/product-factor-skills-smoke.zip` passed.

### Not completed

- No formal secret scanning dependency was added; the project remains standard-library-first.
- No formal legal/compliance framework mapping was added.

### Next iteration suggestions

- Add a `policy-as-checklist` export mode for compliance-like internal reviews.
- Add cross-Skill bundled audit plans for common scenarios such as Agent + RAG + Security.
- Add richer generated catalog artifacts for publication.



## v0.7.0 - 2026-05-18

### Previous version

v0.6.0

### Current version

v0.7.0

### Added

- Added `skills/5-factor-evals/` with `SKILL.md`, checklist, scoring rubric, audit report template, refactor plan template, usage examples, and manifest.
- Added `scripts/select_factor_skill.py` for lightweight primary/secondary Skill recommendation.
- Added `docs/skill-selection-engine.md` and `examples/skill-selection-prompt.md`.

### Modified files

- `README.md`
- `SKILL.md`
- `VERSION`
- `CHANGELOG.md`
- `RELEASE_NOTES.md`
- `ROADMAP.md`
- `product-factor-skills.json`
- `skills.json`
- `docs/skill-routing-guide.md`
- `docs/multi-skill-routing-matrix.md`
- `scripts/scan_factor_project.py`
- `.github/workflows/validate.yml`
- all existing `skills/*/skill.json`

### Fixed problems

- Broad or ambiguous audit requests now have a standard selection path.
- Evaluation maturity is now a first-class review dimension instead of being split across Agent, RAG, docs, and product readiness Skills.

### Skill experience improvements

- Agents can recommend a primary Skill and secondary Skills before starting the audit.
- Teams can pair `5-factor-evals` with any domain Skill to define golden cases, regression loops, and release gates.
- CI now smoke-tests the selector and the new evaluation prompt rendering path.

### Validation results

- `python scripts/scan_factor_project.py .` passed.
- `python scripts/select_factor_skill.py "audit this RAG app for retrieval quality and regression tests" --root . --top 5 --json ./tmp/skill-selection.json --markdown ./tmp/skill-selection.md` passed.
- `python scripts/render_skill_prompt.py 5-factor-evals --target ./examples/sample-agent-project --out ./tmp/evals-prompt.md` passed.
- `python scripts/export_skill_catalog.py . --markdown ./tmp/generated-skill-catalog.md --json ./tmp/generated-skill-catalog.json` passed.
- `python scripts/build_release_zip.py . --out /tmp/product-factor-skills-smoke.zip` passed.
- `python -m py_compile scripts/*.py` passed.

### Not completed

- No completed real-world evaluation audit report yet.
- Selector remains heuristic and dependency-free; it does not deeply parse code or call external services.
- No combined command yet that selects a Skill and immediately generates an audit workspace.

### Next iteration direction

- Add completed sample reports for `5-factor-evals`, `6-factor-docs`, and `13-factor-product-readiness`.
- Add a wrapper command that selects a Skill and creates the audit workspace in one run.
- Add optional markdown link/reference checking with standard-library fallbacks.

## v0.6.0 - 2026-05-18

### Previous version

v0.5.0

### Current version

v0.6.0

### Added

- Added `skills/6-factor-docs/` with `SKILL.md`, checklist, scoring rubric, audit report template, refactor plan template, usage examples, and manifest.
- Added `scripts/export_skill_catalog.py` to generate markdown and JSON catalogs from Skill manifests.
- Added `docs/documentation-readiness-playbook.md`, `docs/skill-catalog-exporter.md`, and `examples/docs-audit-prompt.md`.
- Added `.github/ISSUE_TEMPLATE/bug_report.md`, `.github/ISSUE_TEMPLATE/skill_request.md`, `.github/ISSUE_TEMPLATE/docs_improvement.md`, and `.github/pull_request_template.md`.

### Modified files

- `README.md`
- `SKILL.md`
- `VERSION`
- `CHANGELOG.md`
- `RELEASE_NOTES.md`
- `ROADMAP.md`
- `product-factor-skills.json`
- `skills.json`
- `docs/skill-routing-guide.md`
- `docs/multi-skill-routing-matrix.md`
- `scripts/scan_factor_project.py`
- `.github/workflows/validate.yml`
- all existing `skills/*/skill.json`

### Fixed problems

- Documentation quality is now a first-class review dimension instead of being mixed into product readiness or app review.
- Repository collaboration flow now has dedicated templates for bugs, docs improvements, Skill requests, and pull requests.

### Skill experience improvements

- Agents can now route documentation-heavy requests to `6-factor-docs`.
- Maintainers can export a manifest-driven Skill catalog for human and machine discovery.
- Release validation now checks for nine bundled Skills and smoke-tests the catalog exporter.

### Validation results

- `python scripts/scan_factor_project.py .` passed.
- `python scripts/export_skill_catalog.py . --markdown ./tmp/generated-skill-catalog.md --json ./tmp/generated-skill-catalog.json` passed.
- `python scripts/render_skill_prompt.py 6-factor-docs --target ./examples/sample-agent-project --out ./tmp/docs-prompt.md` passed.
- `python scripts/build_release_zip.py . --out /tmp/product-factor-skills-smoke.zip` passed.
- `python -m py_compile scripts/*.py` passed.

### Not completed

- No completed real-world documentation audit example yet.
- Link checking remains documented as a future enhancement, not implemented as a dependency-free checker.
- No single wrapper command for automatic Skill selection yet.

### Next iteration direction

- Add completed sample reports for `6-factor-docs` and `13-factor-product-readiness`.
- Add optional link/reference checking with standard-library fallbacks.
- Add a lightweight Skill selector that recommends primary and secondary Skills from project signals.

## v0.5.0 - 2026-05-18

### Previous version

v0.4.0

### Current version

v0.5.0

### Added

- Added `skills/13-factor-product-readiness/` with `SKILL.md`, checklist, scoring rubric, audit report template, refactor plan template, usage examples, and manifest.
- Added `scripts/render_skill_prompt.py` for rendering a one-shot Agent prompt from a Skill folder.
- Added `docs/skill-prompt-renderer.md` and `docs/product-readiness-playbook.md`.
- Added `examples/product-readiness-audit-prompt.md`.

### Modified files

- `README.md`
- `SKILL.md`
- `VERSION`
- `CHANGELOG.md`
- `RELEASE_NOTES.md`
- `ROADMAP.md`
- `product-factor-skills.json`
- `skills.json`
- `scripts/scan_factor_project.py`
- `.github/workflows/validate.yml`
- all existing `skills/*/skill.json`

### Fixed problems

- Fixed the GitHub Actions validation workflow syntax by converting the multi-command validation step to `run: |`.
- Increased scanner coverage for the new prompt renderer and product readiness docs.

### Skill experience improvements

- Product-level launch readiness is now a first-class Skill instead of being hidden inside app or CLI review.
- A complete Skill can now be rendered as a single handoff prompt for repeated audits in other Agent sessions.

### Validation results

- `python scripts/scan_factor_project.py .` passed.
- `python scripts/render_skill_prompt.py 13-factor-product-readiness --target ./examples/sample-agent-project --out ./tmp/product-readiness-prompt.md` passed.
- `python scripts/build_release_zip.py . --out /tmp/product-factor-skills-smoke.zip` passed.
- `python -m py_compile scripts/*.py` passed.

### Not completed

- No dedicated issue template or PR template yet.
- No JSON schema validation dependency is used; validation remains standard-library only.
- No web documentation site yet.

### Next iteration direction

- Add `.github/ISSUE_TEMPLATE/` and `.github/pull_request_template.md`.
- Add product readiness presets for different project types.
- Add JSON output support to the prompt renderer.
