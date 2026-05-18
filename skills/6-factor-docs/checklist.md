# 6-factor-docs Checklist

Score each item as `pass`, `partial`, `fail`, or `not applicable`. Add evidence for every important claim.

## 1. Positioning and promise

- The README explains what the project is in the first screen.
- The target user and core use case are clear.
- The slogan or one-line description matches the actual repository.
- The docs explain when to use and when not to use the project.

## 2. First-run onboarding

- A new user can identify the first useful action within 30 seconds.
- Installation or setup steps are explicit and ordered.
- The quickstart is copy-pasteable.
- Expected output is shown after the first command or action.
- Common setup failures have recovery guidance.

## 3. Information architecture

- README, guides, references, examples, and release notes have clear responsibilities.
- Navigation paths are obvious for beginner, contributor, and maintainer use cases.
- Concepts are separated from command references and recipes.
- Deep details do not bury the quickstart.

## 4. Examples and recipes

- Examples map to realistic user tasks.
- Recipes include inputs, commands, outputs, and success criteria.
- Example names match actual files and commands.
- At least one complete end-to-end workflow exists.

## 5. Accuracy and maintenance

- README commands match package metadata, scripts, and CLI help.
- Version references are current.
- Changelog and release notes reflect the current behavior.
- Docs identify validation commands or review cadence.
- Stale TODOs, broken links, and outdated screenshots are visible as debt.

## 6. Agent handoff readiness

- The docs include copyable prompts or task instructions when Agent use is expected.
- Inputs, outputs, constraints, and validation expectations are explicit.
- The project can be reviewed by an Agent without hidden assumptions.
- Audit/refactor outputs are templated or contract-driven where useful.
