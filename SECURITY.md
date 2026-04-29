# Security Policy

## Supported Scope

Security review covers the maintained Python package, GitHub Actions workflows,
dependency definitions, documentation, and project configuration in this
repository.

## Reporting a Vulnerability

Do not open a public issue for sensitive vulnerabilities. Contact the repository
maintainer privately with:

- Affected file, dependency, or workflow.
- Steps to reproduce.
- Expected impact.
- Suggested fix, if known.

## Data Handling

- Do not commit private, licensed, or sensitive datasets.
- Store raw data locally under `data/raw/`.
- Store generated model artifacts locally under `models/`.
- Review notebooks before committing to ensure outputs do not expose sensitive
  paths, credentials, or private data.

## Automated Security Checks

The CI workflow includes:

- Bandit for Python security linting.
- pip-audit for project dependency vulnerability scanning through
  `requirements-audit.txt`.
- CodeQL for static analysis.
- Dependabot for dependency and GitHub Actions update proposals.
