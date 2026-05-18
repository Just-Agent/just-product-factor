# 5-factor-evals Scoring Rubric

Score each factor from 0 to 5.

| Score | Meaning |
|---:|---|
| 0 | Missing or actively misleading |
| 1 | Mentioned, but not actionable |
| 2 | Some examples or notes exist, but no repeatable loop |
| 3 | Usable lightweight evaluation exists |
| 4 | Evaluation is repeatable, documented, and connected to releases |
| 5 | Evaluation is mature, automated where useful, and continuously improved |

## Factors

1. Quality Contract
2. Golden Cases
3. Regression Loop
4. Failure Taxonomy
5. Release Gates

## Rating bands

| Total | Rating | Interpretation |
|---:|---|---|
| 0-7 | Fragile | Changes are mostly trust-based and hard to verify |
| 8-14 | Basic | Some quality signals exist, but regressions are likely |
| 15-20 | Repeatable | Useful checks exist and can guide refactors |
| 21-25 | Release-grade | Quality gates support confident product iteration |
