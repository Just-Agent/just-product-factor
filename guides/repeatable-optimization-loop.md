# Repeatable Optimization Loop

Use this loop when improving the same project across multiple versions.

## 1. Route

Choose the primary Skill using `docs/multi-skill-routing-matrix.md`.

## 2. Prepare

Run:

```bash
python scripts/run_skill_audit.py --repo . --target <project> --skill <skill> --out <audit-dir>
```

## 3. Audit

Fill the Skill audit report with evidence. Avoid vague comments such as "needs improvement" without file references or concrete next steps.

## 4. Refactor

Convert findings into a staged refactor plan:

- Release blockers
- Quick wins
- Product polish
- Architecture improvements
- Long-term roadmap

## 5. Validate

Run available commands. Record both successes and failures.

## 6. Log

Record the iteration in project logs so the next Agent can continue instead of restarting.

## 7. Repeat

Every iteration should make the project more installable, understandable, testable, deployable, maintainable, and useful.
