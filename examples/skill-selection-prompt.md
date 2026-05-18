# Skill Selection Prompt Example

Use this when you are not sure which Factor Skill should be primary.

```text
Use product-factor-skills to select the best primary and secondary Skills for this repository.

Project summary:
- It is a RAG product with an Agent workflow and GitHub Actions deployment.
- Users complain about inconsistent citations and regressions after prompt changes.
- The README is usable but the release validation story is weak.

Please run or simulate the Skill selection workflow, explain the selected primary Skill, identify useful secondary Skills, and then continue with the selected audit workflow.
```

Likely routing:

- Primary: `9-factor-rag`
- Secondary: `5-factor-evals`
- Optional: `12-factor-agents`, `8-factor-github-actions`, `6-factor-docs`
