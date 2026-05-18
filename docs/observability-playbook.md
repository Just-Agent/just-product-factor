# Observability Playbook

Use `15-factor-observability` when a project technically works but is hard to debug, validate, or hand off to another Agent.

## Minimum viable observability

A small open-source product should usually have:

- clear install/build/run/test commands
- actionable errors for common failures
- one validation summary or smoke-test output
- predictable artifact paths
- issue template fields for environment, command, version, and error output
- release notes that say what was validated

## Agent-native observability

Agent-native products should additionally provide:

- run ids or task ids
- tool-call summaries
- RAG retrieval summaries when relevant
- MCP invocation summaries when relevant
- decision logs for non-obvious choices
- validation summaries that the next Agent can read

## Safe diagnostics

Do not log by default:

- API keys or tokens
- cookies or auth headers
- passwords or secrets
- unredacted user data
- full prompts that may contain private context
- raw documents with sensitive content

Prefer:

- hashes or ids
- summarized inputs
- field-level redaction
- opt-in verbose mode
- short diagnostic snippets

## Pairing guide

- Pair with `14-factor-security-privacy` when logs may contain secrets or user data.
- Pair with `5-factor-evals` when observability should feed regression checks.
- Pair with `8-factor-github-actions` when workflow summaries and release artifacts matter.
- Pair with `12-factor-agents` when Agent steps and tool calls need traceability.
