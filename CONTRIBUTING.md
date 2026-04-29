# Contributing

Thank you for improving this project. The repository contains both an academic
submission and production-style scaffolding, so changes should preserve the
coursework context while making the code easier to reproduce.

## Development Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

## Before Opening a Pull Request

Run:

```powershell
python -m ruff check .
python -m pytest --cov=energy_forecasting --cov-report=term-missing
python -m bandit -c pyproject.toml -r src
```

## Contribution Guidelines

- Keep raw data, generated models, and generated reports out of Git.
- Add tests for reusable code under `src/energy_forecasting`.
- Keep the notebook as the narrative analysis artifact.
- Prefer small, reviewable commits with clear messages.
- Update documentation when behaviour, paths, or workflows change.

## Branch Naming

Use short branch names such as:

```text
feature/model-evaluation
docs/mlops-update
fix/data-validation
```
