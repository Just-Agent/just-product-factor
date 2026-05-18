# 15-factor-observability Refactor Plan

## Goal

Make the project easier to observe, debug, validate, and hand off to future Agent iterations without leaking sensitive information.

## Phase 1: Make failures visible

- [ ] Add clear errors for missing configuration, missing dependencies, invalid input, and permission failure.
- [ ] Add validation summary output for core commands or workflows.
- [ ] Document the minimal troubleshooting path in README or docs.

## Phase 2: Make runs traceable

- [ ] Add run id / request id / workflow id where appropriate.
- [ ] Correlate Agent steps, tool calls, RAG retrievals, MCP invocations, or CI jobs.
- [ ] Save audit-summary, validation-summary, and decision-log artifacts.

## Phase 3: Add useful metrics

- [ ] Count runs, failures, retries, and skipped checks.
- [ ] Record durations for build, test, retrieval, tool calls, and release steps.
- [ ] Define release confidence metrics or quality gates.

## Phase 4: Make observability safe

- [ ] Redact secrets and tokens.
- [ ] Avoid logging raw user data by default.
- [ ] Document debug mode and retention expectations.
- [ ] Pair with `14-factor-security-privacy` for sensitive systems.

## Phase 5: Improve user and Agent handoff

- [ ] Add issue template fields for diagnostic evidence.
- [ ] Add docs/troubleshooting.md or equivalent.
- [ ] Add stable output paths for audit artifacts.
- [ ] Add examples showing good failure reports.

## Validation plan

| Check | Command | Expected result |
|---|---|---|
| Structure |  |  |
| Smoke run |  |  |
| Failure mode |  |  |
| Redaction |  |  |
| Artifact output |  |  |
