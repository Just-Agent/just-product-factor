# 11-factor-cli Checklist

Score each item as `pass`, `partial`, `fail`, or `not applicable`. Add evidence for every important claim.

## 1. Installability

- The README explains installation for a clean machine.
- The package metadata exposes a clear executable entrypoint.
- Local development install is documented.
- Runtime requirements and supported versions are explicit.

## 2. Command surface

- Commands are named consistently.
- Subcommands match user mental models.
- Destructive commands require confirmation or a clear force flag.
- Flags have sensible defaults.

## 3. Help and examples

- `--help` works at root and subcommand level.
- Help text includes examples, defaults, and required arguments.
- README examples match the actual command names.
- Common recipes are copy-pasteable.

## 4. Input validation

- Missing arguments produce actionable messages.
- Invalid files, paths, URLs, and enum values are handled clearly.
- The CLI validates configuration before doing expensive or destructive work.

## 5. Error handling

- Errors explain what failed, why it likely failed, and what to try next.
- Stack traces are hidden by default but available in debug mode.
- Exit codes distinguish success, user error, environment error, and internal error.

## 6. Configuration and environment

- Environment variables are documented.
- Config files are optional or discoverable.
- Precedence among flags, env vars, and config files is clear.
- Secrets are never printed.

## 7. Output contract

- Human-readable output is clean.
- Machine-readable output is available when useful, such as `--json`.
- Output paths and generated filenames are predictable.
- Progress output does not corrupt JSON or pipeable output.

## 8. Logging and verbosity

- `--verbose` or `--debug` reveals diagnostic details.
- Quiet mode exists for scripts when needed.
- Logs are useful without being noisy.

## 9. Automation friendliness

- Commands work in CI without prompts.
- Exit codes are reliable.
- Inputs and outputs can be scripted.
- The CLI can run non-interactively.

## 10. Testing and smoke checks

- Help output has smoke tests.
- At least one happy path command has a test.
- Error paths are tested.
- CI runs tests or smoke checks.

## 11. Packaging and release readiness

- Version command exists or version is visible.
- Changelog and release notes exist.
- Package publishing steps are documented.
- The CLI has a minimal release checklist.
