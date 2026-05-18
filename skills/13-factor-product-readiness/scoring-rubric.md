# 13-factor-product-readiness Scoring Rubric

Score each factor from 0 to 5.

| Factor | 0 | 3 | 5 |
|---|---|---|---|
| Product promise | Unclear | Understandable but generic | Clear, memorable, and specific |
| First 30 seconds | Visitor is confused | Value is visible after scanning | Value is obvious immediately |
| First 5 minutes | Cannot run | Runs with friction | Copyable path works cleanly |
| Examples and recipes | Missing | Some examples | Real workflows with expected outputs |
| Product surface | Inconsistent | Mostly usable | Predictable and polished |
| Failure recovery | Silent or cryptic | Some guidance | Actionable errors and troubleshooting |
| Documentation structure | Scattered | Basic docs | Clear README, guides, reference, examples |
| Validation path | Missing | Manual checks | CI and local validation are clear |
| Release readiness | No release discipline | Partial release files | Versioned, packaged, and reproducible |
| GitHub polish | Empty shell | Basic repo hygiene | Contributor-friendly and credible |
| Trust and safety | Not addressed | Partial notes | Clear assumptions and safe defaults |
| Agent-native path | Not supported | Some prompts | Manifests, templates, and repeatable loops |
| Retention and differentiation | Generic | Some differentiation | Strong identity and repeat-use value |

Overall score = average score / 5 * 100.

Recommended bands:

- 90-100: launch-ready.
- 75-89: strong beta; fix polish and validation gaps.
- 60-74: useful but needs productization.
- 40-59: prototype; major onboarding and release gaps.
- 0-39: unclear product; rebuild positioning and usage path first.
