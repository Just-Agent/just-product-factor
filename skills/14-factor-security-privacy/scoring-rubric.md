# 14-factor-security-privacy Scoring Rubric

Score each factor from 0 to 5.

| Score | Meaning |
|---:|---|
| 0 | Missing or unsafe; likely release blocker |
| 1 | Mentioned, but not actionable or not enforced |
| 2 | Basic awareness with important gaps |
| 3 | Usable baseline for low-risk projects |
| 4 | Strong practice with documented validation |
| 5 | Release-grade and continuously maintained |

## Factors

1. Asset Inventory
2. Secret Hygiene
3. Configuration Safety
4. Permission Boundaries
5. Input Validation
6. Output and Log Safety
7. Data Handling
8. Dependency Hygiene
9. CI/CD Security
10. Agent and Tool Safety
11. MCP and Integration Safety
12. RAG and Knowledge Safety
13. Release and Disclosure Readiness
14. Validation Evidence

## Rating bands

| Total | Rating | Interpretation |
|---:|---|---|
| 0-24 | Critical | Unsafe for public release without mitigation |
| 25-44 | Risky | Major gaps remain; treat as pre-release only |
| 45-57 | Baseline | Acceptable for low-risk demos with clear limits |
| 58-66 | Release-ready | Good product security posture for typical open-source use |
| 67-70 | Mature | Strong repeatable security/privacy practice |

## Priority rule

Any confirmed committed real secret, unsafe CI secret exposure, destructive unaudited tool action, or private-data leak should be treated as a critical blocker even if the total score appears acceptable.
