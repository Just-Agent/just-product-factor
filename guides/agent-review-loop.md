# Agent Review Loop

Use this loop when repeatedly improving a project with Product Factor Skills.

## Loop

1. Pick the closest Skill.
2. Read the target repository.
3. Produce an evidence-based audit.
4. Select the highest-impact release blocker.
5. Modify real files.
6. Run validation if possible.
7. Update changelog and logs.
8. Package the next version.

## Good iteration behavior

- Prefer small shippable improvements over broad plans.
- Record what was actually changed.
- Keep version numbers consistent.
- Do not hide validation failures.
- Make the next prompt easier by updating logs.

## Bad iteration behavior

- Rebuilding the project from scratch when a previous version exists.
- Only writing plans without modifying files.
- Claiming tests passed without running them.
- Adding a Skill without required templates and examples.
