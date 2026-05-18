# Documentation Readiness Playbook

Use this playbook with `6-factor-docs` when a repository is technically useful but hard for new users or Agents to understand.

## The documentation ladder

1. **Promise:** What is this project and who is it for?
2. **First action:** What should a new user do first?
3. **Expected output:** What should success look like?
4. **Next path:** Where should the user go after the quickstart?
5. **Reference:** Where are stable details kept?
6. **Maintenance:** How do docs stay correct across releases?

## First 30 seconds test

A new reader should be able to answer:

- What does this project do?
- Is it for me?
- What can I copy and run?
- What will I get if it works?

## Agent handoff test

An Agent should be able to answer:

- Which Skill or workflow should apply?
- Which files should be inspected?
- Which outputs are expected?
- Which validation commands should be attempted?
- Which assumptions must be recorded?

## Common fixes

- Move install and quickstart above long concept sections.
- Add expected output after every first-run command.
- Convert vague examples into recipes with inputs, commands, outputs, and validation.
- Keep changelog, release notes, and README version references aligned.
- Add prompts only when they include inputs, constraints, and output format.
