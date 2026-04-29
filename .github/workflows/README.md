# GitHub Actions Workflows

This folder defines the automated checks for the repository.

## Workflows

- `ci.yml`: Runs Ruff, pytest with coverage, Bandit, and pip-audit.
- `codeql.yml`: Runs CodeQL static analysis for Python.

Both workflows run on pushes and pull requests. CodeQL also runs on a weekly
schedule.
