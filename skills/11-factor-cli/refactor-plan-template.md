# 11-factor-cli Refactor Plan

## Goal

Make the CLI installable, understandable, scriptable, observable, testable, and release-ready.

## Phase 1: Make it runnable

- [ ] Confirm package metadata and executable entrypoint.
- [ ] Add or fix install instructions.
- [ ] Add root `--help` and version output.
- [ ] Add one happy path example.

## Phase 2: Make it usable

- [ ] Improve command names and flag names.
- [ ] Add actionable error messages.
- [ ] Add input validation before side effects.
- [ ] Add examples to README and help text.

## Phase 3: Make it scriptable

- [ ] Add stable exit codes.
- [ ] Add non-interactive mode for CI.
- [ ] Add optional JSON output where useful.
- [ ] Separate progress logs from machine-readable output.

## Phase 4: Make it releasable

- [ ] Add smoke tests.
- [ ] Add CI validation.
- [ ] Update changelog and release notes.
- [ ] Document publishing steps.

## Validation commands

```bash
<install command>
<cli> --help
<cli> --version
<cli> <happy-path-command>
<test command>
```

## Next iteration

-
