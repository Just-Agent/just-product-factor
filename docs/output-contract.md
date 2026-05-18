# Factor Skill Output Contract

Every Product Factor Skill should produce outputs that are useful to both humans and Agents.

## Required sections

1. Executive summary
2. Scope and assumptions
3. Evidence table
4. Score table
5. Release readiness decision
6. Prioritized refactor plan
7. Validation commands
8. Known limits
9. Next iteration suggestions

## Evidence rules

- Tie every major finding to a file, command, snippet, or observed behavior.
- Do not claim a command passed unless it was actually run.
- Separate static inspection from runtime validation.
- Mark assumptions clearly.

## Refactor rules

- Prefer changes that make the product installable, runnable, understandable, and safe.
- Rank work by user impact and release readiness.
- Include concrete file-level changes when possible.
- Keep non-essential ideas in a backlog section.

## Release readiness labels

- `ready`: can be used by target users with normal care.
- `ready-with-limits`: usable but has documented gaps.
- `not-ready`: install, run, safety, or correctness blockers remain.
