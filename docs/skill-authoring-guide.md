# Skill Authoring Guide

Use this guide to create a new `xx-factor-*` Skill.

## Naming

Use a clear domain name:

```text
<number>-factor-<domain>
xx-factor-<domain>
```

Examples:

- `6-factor-cli`
- `8-factor-github-actions`
- `9-factor-rag`
- `xx-factor-mobile-app`

## Required files

Each Skill must include:

- `SKILL.md`
- `checklist.md`
- `scoring-rubric.md`
- `audit-report-template.md`
- `refactor-plan-template.md`
- `usage-examples.md`
- `skill.json`

## Required design decisions

Every Skill should answer:

1. When should an Agent call this Skill?
2. What inputs should the Agent inspect?
3. What should the Agent output?
4. What dimensions should be scored?
5. What changes should be prioritized first?
6. How should validation be recorded?

## Quality bar

A good Factor Skill is not a blog post. It is a repeatable operating procedure for project audit and refactor.
