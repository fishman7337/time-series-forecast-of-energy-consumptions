# MLOps Guide

## Lifecycle

1. Place raw data in `data/raw/`.
2. Validate schema and positivity constraints.
3. Run notebook exploration when analysis changes are needed.
4. Run reusable CLI evaluation for repeatable metrics.
5. Train final models and write artifacts to `models/`.
6. Store generated metrics and forecasts under `reports/`.
7. Run CI quality and security gates before merging or publishing.

## Local Commands

```powershell
python -m energy_forecasting.cli validate --data data/raw/CA2-Energy-Consumption-Data.csv
python -m energy_forecasting.cli evaluate --data data/raw/CA2-Energy-Consumption-Data.csv
python -m energy_forecasting.cli train --data data/raw/CA2-Energy-Consumption-Data.csv
```

## CI Gates

The GitHub workflow runs:

- Ruff linting.
- Pytest with coverage.
- Bandit security checks.
- pip-audit dependency vulnerability checks.
- CodeQL static analysis.

## Artifact Policy

Committed:

- Source code.
- Tests.
- Documentation.
- Original notebook and presentation.
- Placeholder files and data contracts.

Not committed:

- Raw datasets.
- Processed datasets.
- Trained model artifacts.
- Local virtual environments.
- Generated reports unless deliberately approved.

## Reproducibility

The reusable workflow is configuration-driven through:

- `pyproject.toml`
- `params.yaml`
- `dvc.yaml`
- `src/energy_forecasting/config.py`

Use the same Python version and dependency set when comparing metrics across
runs.

## Monitoring Considerations

If this project is extended into a deployed service, monitor:

- Data freshness.
- Missing or duplicated months.
- Distribution drift in each target.
- Forecast error once actual values arrive.
- Training failures and dependency vulnerabilities.
