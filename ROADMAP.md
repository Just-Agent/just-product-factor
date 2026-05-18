# Roadmap

## v0.2.x

- Add real before/after audit examples for each Skill.
- Add a release packaging script.
- Add richer Skill Factory documentation.
- Add optional JSON schema validation if dependency policy allows.

## v0.3.x

- Add a lightweight CLI wrapper for selecting and applying Skills.
- Add domain-specific sample reports for Agent, App, HTML, GitHub Actions, RAG, and MCP projects.
- Add examples showing how to use multiple Skills on one project.

## v0.4.x

- Add score normalization across Skills.
- Add release-quality badges and generated manifest tables.
- Add a versioned Skill registry format.

## v1.0.0 criteria

- Stable Skill schema.
- Stable validation script.
- Complete examples for all included Skills.
- Clear contribution and release process.
- At least one real-world audit case per Skill.


## v0.5.0 candidate themes

- CLI Skill Pack polish with completed example reports.
- Formal test suite for `scan_factor_project.py` and `generate_factor_skill.py`.
- Optional package metadata for installable Skill distribution.
- Deeper schema checks for scoring rubrics and report templates.


## Suggested next milestones after v0.5.0

- Machine-readable score dashboard for all generated audits.
- Completed example reports for each bundled Skill.
- Optional `factor` CLI wrapper around `run_skill_audit.py`.
- Markdown linting and link validation for release workflows.


## After v0.5.0

- Add product readiness presets for OSS library, CLI tool, Agent project, static site, and RAG product.
- Add optional JSON output mode for `render_skill_prompt.py` and `run_skill_audit.py`.
- Add issue and PR templates for productized open-source workflow.


## v0.6.0 completed themes

- Added first-class documentation readiness review with `6-factor-docs`.
- Added catalog export tooling for manifest-driven discovery.
- Added GitHub issue and PR templates for open-source collaboration.

## v0.7.0 completed themes

- Added `5-factor-evals` as a first-class validation and release confidence Skill.
- Added a lightweight dependency-free Skill selector for ambiguous or multi-domain audits.
- Added selector documentation and examples for primary/secondary Skill routing.

## After v0.7.0

- Add completed example audit reports for `5-factor-evals`, `6-factor-docs`, and `13-factor-product-readiness`.
- Add optional markdown link/reference checking with standard-library fallbacks.
- Add a single wrapper command that selects a Skill and generates an audit workspace in one step.


## Added in v0.9.0

- `15-factor-observability` for runtime visibility, structured logs, metrics, traces, validation artifacts, failure diagnostics, and Agent handoff readiness.
- `scripts/compose_factor_review.py` for multi-Skill review planning.

## Future ideas

- Add completed sample audit reports for every bundled Skill.
- Add composition presets for common release workflows.
- Add optional markdown link/reference checking with standard-library fallbacks.
