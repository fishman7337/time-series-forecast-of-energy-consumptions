# energy_forecasting Package

This package contains reusable utilities for the energy consumption forecasting
workflow.

## Modules

- `config.py`: Shared paths, target columns, and model configuration.
- `data.py`: CSV loading, validation, date parsing, and outlier helpers.
- `features.py`: Train-test splitting, log transforms, and future date indexes.
- `metrics.py`: Regression metrics used for model comparison.
- `models.py`: ARIMA/SARIMAX model specifications and persistence.
- `pipeline.py`: Evaluation, final training, and report writing helpers.
- `cli.py`: Command-line interface for validation, evaluation, and training.
