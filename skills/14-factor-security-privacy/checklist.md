# 14-factor-security-privacy Checklist

## 1. Asset Inventory

- [ ] The project identifies user data, credentials, tokens, files, generated outputs, and privileged actions.
- [ ] External services and third-party APIs are listed.
- [ ] Trust boundaries between user, Agent, server, tools, storage, and CI/CD are clear.

## 2. Secret Hygiene

- [ ] No real API keys, tokens, passwords, cookies, private URLs, or signing secrets are committed.
- [ ] `.env.example` uses placeholders only.
- [ ] Logs, fixtures, screenshots, and examples do not expose secrets.
- [ ] Secret rotation guidance exists if accidental exposure happens.

## 3. Configuration Safety

- [ ] Defaults are safe for local development.
- [ ] Production settings are documented separately.
- [ ] Dangerous flags are clearly labeled.
- [ ] Required environment variables are listed.

## 4. Permission Boundaries

- [ ] API tokens and workflow permissions follow least privilege.
- [ ] Agent tools describe what they can and cannot do.
- [ ] File-system, network, shell, and deployment operations are constrained.
- [ ] Human approval is required for destructive or high-risk actions.

## 5. Input Validation

- [ ] User input, uploaded files, URLs, paths, prompts, and tool arguments are validated.
- [ ] Path traversal, shell injection, SSRF, unsafe redirects, and unsafe deserialization risks are considered.
- [ ] Error messages do not reveal sensitive internals.

## 6. Output and Log Safety

- [ ] Logs and traces redact tokens and user-sensitive data.
- [ ] Audit reports do not include raw private data unless explicitly necessary.
- [ ] Generated examples avoid realistic secrets and PII.

## 7. Data Handling

- [ ] Retention expectations are documented.
- [ ] Deletion and cleanup paths exist for temporary files and generated artifacts.
- [ ] Public/private data boundaries are explicit.
- [ ] Telemetry, analytics, or model logging is disclosed when present.

## 8. Dependency Hygiene

- [ ] Dependency manifests and lockfiles are present where appropriate.
- [ ] Known high-risk dependencies are reviewed.
- [ ] Update and vulnerability-check paths are documented.
- [ ] Generated vendored files are clearly separated from source.

## 9. CI/CD Security

- [ ] Workflow permissions are minimal.
- [ ] Secrets are not exposed to untrusted pull requests.
- [ ] Release automation includes version and artifact checks.
- [ ] Deployment workflows include explicit environments or approvals when needed.

## 10. Agent and Tool Safety

- [ ] Tool schemas are clear and narrow.
- [ ] Tool outputs are validated before feeding into later actions.
- [ ] Prompt injection and tool-call escalation risks are documented.
- [ ] Unsafe autonomous loops require guardrails or budget limits.

## 11. MCP and Integration Safety

- [ ] MCP tools document permissions, side effects, and data access.
- [ ] Integrations define trust assumptions.
- [ ] Failures and partial results are handled safely.

## 12. RAG and Knowledge Safety

- [ ] Retrieval sources are labeled as public, private, or mixed.
- [ ] Citation and source boundaries are preserved.
- [ ] Private knowledge is not accidentally exposed in public outputs.

## 13. Release and Disclosure Readiness

- [ ] SECURITY.md or vulnerability reporting guidance exists for public repositories.
- [ ] Release notes mention security-relevant changes and validation limits.
- [ ] License, attribution, and third-party content boundaries are clear.

## 14. Validation Evidence

- [ ] Basic secret scan or manual search has been run.
- [ ] CI workflow security posture has been reviewed.
- [ ] High-risk tool permissions have been tested.
- [ ] Remaining risks are documented honestly.
