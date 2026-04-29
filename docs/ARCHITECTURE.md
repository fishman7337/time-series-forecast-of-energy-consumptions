# Architecture

## Design

The repository is split into narrative artifacts and reusable automation:

- `notebooks/` contains the original coursework story and visual analysis.
- `src/energy_forecasting/` contains reusable data, feature, metric, model, and
  pipeline helpers.
- `tests/` verifies reusable code without requiring the private raw dataset.
- `docs/` records project context, assumptions, and operational guidance.

## Package Modules

| Module | Responsibility |
| --- | --- |
| `config.py` | Paths, target column names, and model configuration. |
| `data.py` | CSV loading, schema validation, date parsing, and outlier helpers. |
| `features.py` | Time-based splitting, log transforms, and future date indexes. |
| `metrics.py` | Regression metric calculation. |
| `models.py` | ARIMA/SARIMAX model specifications and persistence. |
| `pipeline.py` | Evaluation, training, and JSON report writing. |
| `cli.py` | Command-line interface for validation, evaluation, and training. |

## Data Flow

```text
data/raw CSV
    -> load_energy_data
    -> prepare_energy_dataframe
    -> evaluate_model or train_and_save_default_models
    -> models/ and reports/
```

## Extension Points

- Add exogenous variables by extending the data contract and SARIMAX pipeline.
- Add forecast intervals to the CLI output.
- Add model registry integration if artifacts are promoted beyond coursework.
- Add drift monitoring once actual post-forecast values are available.
