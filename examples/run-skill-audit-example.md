# Run a Skill Audit Example

This example shows how to create a repeatable audit package before asking an Agent to review a project.

```bash
python scripts/run_skill_audit.py   --repo .   --target .   --skill 12-factor-app   --out ./tmp/self-audit
```

Then ask the Agent:

```text
Use the 12-factor-app skill to audit this project.
Start from tmp/self-audit/audit-brief.md.
Fill tmp/self-audit/audit-report.md and tmp/self-audit/refactor-plan.md.
Record validation results in tmp/self-audit/validation-summary.md.
```

For Agent projects, switch the Skill:

```bash
python scripts/run_skill_audit.py --repo . --target ./my-agent --skill 12-factor-agents --out ./tmp/agent-audit
```

For HTML pages:

```bash
python scripts/run_skill_audit.py --repo . --target ./site --skill 10-factor-html --out ./tmp/html-audit
```
