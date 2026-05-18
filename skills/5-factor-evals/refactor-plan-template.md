# 5-factor-evals Refactor Plan

## Goal

Create a repeatable evaluation loop that improves release confidence without adding unnecessary process.

## Phase 1 — Minimum useful eval harness

- [ ] Define product-level quality contract.
- [ ] Add 5-10 golden cases.
- [ ] Add a simple smoke/eval command.
- [ ] Store results in a stable file format.

## Phase 2 — Regression confidence

- [ ] Add baseline comparison.
- [ ] Add failure taxonomy labels.
- [ ] Add CI smoke check for high-value cases.
- [ ] Record validation status in release notes.

## Phase 3 — Release-grade validation

- [ ] Add tiered checks for docs, code, prompts, data, and tool changes.
- [ ] Add regression dashboard or summary artifact.
- [ ] Add go/no-go thresholds.
- [ ] Schedule periodic review of stale cases.

## Risks

- Overfitting to narrow golden cases.
- Treating subjective quality as a single number.
- Adding expensive evals before a lightweight loop exists.
- Hiding validation limits instead of documenting them.

## Done definition

A maintainer or Agent can run one command, see what changed, understand failures, and decide whether a release is safe.
