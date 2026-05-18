# 15-factor-observability Scoring Rubric

Score each dimension from 0 to 5.

| Dimension | 0 | 3 | 5 |
|---|---|---|---|
| Runtime map | No known run path | Main paths documented | Critical paths, dependencies, inputs, and failure points are clear |
| Structured logging | Print-only or none | Basic leveled logs | Structured, searchable, correlated, privacy-safe logs |
| Error diagnostics | Generic failure | Common failures actionable | Failures include cause, context, next action, and recovery path |
| Metrics | None | Basic success/failure/duration | Product, runtime, quality, and release metrics are defined |
| Tracing | No correlation | Basic run id or workflow run | End-to-end request/run/tool/job correlation |
| Artifacts | None | Validation summary exists | Audit report, refactor plan, decision log, failures, and summaries are durable |
| Privacy safety | Secrets may leak | Some redaction | Defaults are safe, debug mode is explicit, sensitive data is controlled |
| Debug UX | Users cannot report useful bugs | Basic issue template | Troubleshooting, issue templates, examples, and diagnostics are strong |
| Release visibility | Releases have no validation evidence | Basic changelog | Release notes, CI artifacts, and validation gates are clear |
| Agent handoff | Agent must rediscover context | Some summaries exist | Agent can continue from stable logs, summaries, and plans |

## Score interpretation

| Total | Meaning |
|---:|---|
| 0-15 | Blind runtime. Failures are hard to reproduce. |
| 16-30 | Basic visibility, but not enough for reliable maintenance. |
| 31-40 | Usable observability for early product iteration. |
| 41-47 | Release-ready observability for most open-source projects. |
| 48-50 | Excellent observability and Agent handoff readiness. |

## Release gate guidance

- Public release should normally reach at least 35/50.
- Hosted production should normally reach at least 40/50.
- Agentic systems with tool calls, user data, or external integrations should pair this score with `14-factor-security-privacy`.
