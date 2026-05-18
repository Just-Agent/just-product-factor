# 14-factor-security-privacy Refactor Plan

## Goal

Reduce security, privacy, and release risks with the smallest set of high-leverage changes.

## Phase 1 — Release blockers

- [ ] Remove or rotate exposed secrets.
- [ ] Add `.env.example` and ensure real `.env` files are ignored.
- [ ] Reduce workflow token permissions.
- [ ] Add or update `SECURITY.md` for public vulnerability reporting.
- [ ] Document high-risk tool side effects and approval requirements.

## Phase 2 — Safe defaults and data boundaries

- [ ] Replace unsafe defaults with local-safe defaults.
- [ ] Document data retention and cleanup behavior.
- [ ] Redact sensitive logs and reports.
- [ ] Add input validation for file paths, URLs, shell commands, and tool arguments.
- [ ] Label public/private data sources.

## Phase 3 — Repeatable validation

- [ ] Add a lightweight secret-scan command or documented manual check.
- [ ] Add CI checks for workflow permissions and required files.
- [ ] Add dependency update/vulnerability-review guidance.
- [ ] Record security/privacy validation status in release notes.

## Risks

- Treating this checklist as legal compliance.
- Hiding validation limits.
- Adding broad automation permissions for convenience.
- Letting Agent tools perform destructive actions without approval.

## Done definition

A maintainer can explain what data is touched, where secrets live, which tools can act, what risks remain, and what validation was performed before release.
