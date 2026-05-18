# 11-factor-cli Skill

Version: `v0.7.0`

## Purpose

Use this Skill to audit and refactor command-line products so they are installable, understandable, scriptable, observable, testable, and release-ready.

## When to use

Use this Skill when a project contains a CLI entrypoint, developer tool, automation wrapper, scaffold generator, local command runner, or product-facing command interface.

Typical targets:

- Node.js CLIs using `bin`, `commander`, `yargs`, `oclif`, or custom scripts
- Python CLIs using `argparse`, `click`, `typer`, or console scripts
- Go, Rust, or shell-based CLIs
- GitHub Actions helper commands
- Agent-generated CLI tools that need product polish

## When not to use

Do not use this Skill for pure web UI review, RAG quality review, MCP schema review, or Agent architecture review unless the CLI is the main product interface. Use a more specific Factor Skill first, then combine this Skill for the command layer.

## Inputs

- Repository tree or source archive
- README and command docs
- CLI entrypoint files
- Package metadata and install instructions
- Examples, tests, workflows, and release scripts if present
- Error logs or user complaints if available

## Workflow

1. Identify the CLI runtime, install path, and command surface.
2. Check whether a new user can install, run help, execute the happy path, and recover from errors.
3. Apply `checklist.md` and collect evidence.
4. Score the project with `scoring-rubric.md`.
5. Produce `audit-report-template.md` output.
6. Produce `refactor-plan-template.md` output.
7. Recommend validation commands and record anything that could not be executed.

## Review dimensions

1. Installability
2. Command surface
3. Help and examples
4. Input validation
5. Error handling
6. Configuration and environment
7. Output contract
8. Logging and verbosity
9. Automation friendliness
10. Testing and smoke checks
11. Packaging and release readiness

## Scoring

Use a 100-point score. Treat installability, command UX, error handling, and validation as blocking quality gates. A CLI with a beautiful README but no runnable entrypoint should not pass release readiness.

## Refactor priority

1. Make it installable.
2. Make `--help` useful.
3. Make the happy path work.
4. Make failure modes understandable.
5. Make outputs stable for scripts and Agents.
6. Add smoke tests and release packaging.

## Output format

Return:

- Executive summary
- Score table
- Evidence-based findings
- Command UX review
- Installation and packaging review
- Refactor plan
- Validation commands
- Assumptions and unknowns

## Example call

```text
Use the 11-factor-cli skill to audit this CLI for installability, command UX, configuration, error handling, logging, testing, packaging, and release readiness.
```

## Version history

- `v0.5.0`: Added as a first-class Factor Skill for command-line products.
