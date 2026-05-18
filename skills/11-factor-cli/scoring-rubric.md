# 11-factor-cli Scoring Rubric

Total: 100 points.

| Dimension | Points | What good looks like |
|---|---:|---|
| Installability | 12 | A clean user can install and run the CLI from documented steps. |
| Command surface | 10 | Commands are predictable, consistent, and hard to misuse. |
| Help and examples | 10 | `--help` and README examples are clear and aligned. |
| Input validation | 8 | Invalid input fails early with actionable messages. |
| Error handling | 10 | Errors include cause, next step, and stable exit behavior. |
| Configuration and environment | 8 | Flags, env vars, config files, and secrets are handled safely. |
| Output contract | 10 | Output is clean for humans and stable for scripts/Agents. |
| Logging and verbosity | 6 | Debug, verbose, and quiet modes are useful. |
| Automation friendliness | 8 | CI and non-interactive use are supported. |
| Testing and smoke checks | 10 | Help, happy path, and error paths are validated. |
| Packaging and release readiness | 8 | Versioning, changelog, and publishing flow are ready. |

## Release bands

- 90-100: Release-ready CLI.
- 75-89: Usable beta; fix remaining rough edges.
- 60-74: Prototype-quality; needs product hardening.
- Below 60: Not ready for users; fix install, help, and happy path first.

## Blocking failures

Do not mark the CLI release-ready if any of these fail:

- No documented install path.
- No working help command.
- No reliable happy path.
- Destructive command can run accidentally.
- Secrets may be printed in normal output.
