# Security and Privacy Readiness Playbook

Use this playbook when a project is moving from prototype to public release, public demo, hosted deployment, or open-source distribution.

## Recommended routing

1. Use the domain Skill first when the technical surface is clear.
2. Use `14-factor-security-privacy` before release or deployment.
3. Pair with:
   - `12-factor-agents` for Agent tools and autonomous execution.
   - `7-factor-mcp` for MCP tool schemas and permissions.
   - `8-factor-github-actions` for workflow permissions and release safety.
   - `9-factor-rag` for private/public knowledge boundaries.
   - `12-factor-app` for service configuration and deployment.

## Minimum release safety pass

- Search for committed secrets and realistic credentials.
- Confirm `.env.example` exists and real `.env` files are ignored.
- Review workflow permissions.
- Review logs, examples, fixtures, and generated artifacts for sensitive data.
- Document data retention and cleanup behavior.
- Add vulnerability reporting guidance for public projects.
- Record validation limits in release notes.

## Agent-specific security questions

- What tools can the Agent call?
- Which tool calls can modify files, deploy code, send messages, or access external services?
- Which actions require human approval?
- How are tool arguments validated?
- Could retrieved text or user input cause prompt injection or tool escalation?
- Are outputs and logs redacted?

## Output expectations

A useful security/privacy review should produce:

- A trust boundary map.
- A critical blocker list.
- A 14-factor scorecard.
- A mitigation plan ordered by release risk.
- Validation results or explicit validation limits.
