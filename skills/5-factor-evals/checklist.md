# 5-factor-evals Checklist

## 1. Quality Contract

- [ ] The project states what successful output means for users.
- [ ] Quality criteria are specific enough to judge examples.
- [ ] Evaluation goals are connected to product promises, not only technical metrics.
- [ ] Known non-goals and acceptable limitations are documented.

## 2. Golden Cases

- [ ] The project includes representative happy-path cases.
- [ ] The project includes edge cases, ambiguous inputs, and known failure examples.
- [ ] Expected outputs or acceptance notes are stored near fixtures.
- [ ] Cases are easy for an Agent or developer to run repeatedly.

## 3. Regression Loop

- [ ] There is a smoke test or evaluation command.
- [ ] The project can compare current behavior against a baseline.
- [ ] CI or release workflow runs at least the lightweight checks.
- [ ] Evaluation results are recorded in a stable format.

## 4. Failure Taxonomy

- [ ] Common failure modes are named and grouped.
- [ ] Each failure mode has an owner or recommended fix path.
- [ ] Failures distinguish data, prompt, tool, retrieval, UX, and infrastructure causes.
- [ ] Regression reports include examples, severity, and reproduction notes.

## 5. Release Gates

- [ ] Release notes mention validation status.
- [ ] High-risk changes require stronger checks than low-risk docs changes.
- [ ] The project records validation limits honestly.
- [ ] There is a go/no-go threshold for publishable releases.
