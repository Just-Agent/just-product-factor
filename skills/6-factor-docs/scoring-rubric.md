# 6-factor-docs Scoring Rubric

Total: 100 points.

| Dimension | Points | What good looks like |
|---|---:|---|
| Positioning and promise | 18 | The reader immediately understands what the project does, who it is for, and why it matters. |
| First-run onboarding | 22 | A clean user can complete the first useful action from copy-pasteable steps. |
| Information architecture | 16 | README, guides, references, recipes, and logs have clear roles and navigation. |
| Examples and recipes | 16 | Examples are realistic, complete, and aligned with actual commands/files. |
| Accuracy and maintenance | 16 | Docs match current behavior, versioning, changelog, and validation reality. |
| Agent handoff readiness | 12 | An Agent can use the docs as a repeatable instruction source with clear inputs and outputs. |

## Release bands

- 90-100: Documentation is release-ready and strongly supports adoption.
- 75-89: Good documentation; fix remaining onboarding and maintenance gaps.
- 60-74: Usable but prototype-like; improve quickstart, structure, and examples.
- Below 60: Documentation blocks adoption; fix promise, first-run path, and accuracy first.

## Blocking failures

Do not mark docs release-ready if any of these fail:

- The project purpose is unclear in the README.
- There is no copy-pasteable first useful action.
- Commands in the docs do not match the repository.
- Examples are incomplete or misleading.
- Version and release notes contradict current behavior.
