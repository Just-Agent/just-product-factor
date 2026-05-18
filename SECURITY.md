# Security Policy

`product-factor-skills` is a standards and template repository. It does not process user data by default, but the included Skills may be used to audit projects that handle sensitive data, secrets, credentials, workflows, or Agent tool calls.

## Reporting a vulnerability

If you find a security issue in this repository's scripts, templates, workflows, or generated release artifacts, please open a private report through the hosting platform's security reporting feature when available, or contact the maintainers through the repository issue process with sensitive details removed.

## Scope

In scope:

- Repository scripts that could mishandle files or generated artifacts.
- GitHub Actions workflow risks.
- Templates that encourage unsafe defaults.
- Example content that accidentally includes realistic secrets.

Out of scope:

- Formal compliance certification.
- Security review of downstream projects unless maintainers explicitly request it.
- Third-party repositories referenced for attribution.

## Maintainer checklist

Before each release:

- Run `python scripts/scan_factor_project.py .`.
- Check for realistic secrets in examples and logs.
- Confirm workflow permissions are minimal.
- Confirm release notes include validation limits.
