# Reproducibility

## Environment

Use Python 3.10 or newer. CI currently uses Python 3.12.

```powershell
python -m pip install -r requirements-dev.txt
```

## Dataset Placement

Store the raw CSV at:

```text
data/raw/CA2-Energy-Consumption-Data.csv
```

The source code can also accept a custom path through `--data`.

## Repeatable Workflow

```powershell
python -m energy_forecasting.cli validate --data data/raw/CA2-Energy-Consumption-Data.csv
python -m energy_forecasting.cli evaluate --data data/raw/CA2-Energy-Consumption-Data.csv
python -m energy_forecasting.cli train --data data/raw/CA2-Energy-Consumption-Data.csv
```

## Notebook Workflow

The original notebook is preserved under `notebooks/`. If running it from that
folder, the expected dataset path is:

```text
../data/raw/CA2-Energy-Consumption-Data.csv
```

## Determinism

Statsmodels ARIMA/SARIMAX fitting is deterministic for the same data,
dependency versions, and optimizer settings. Metrics may still vary across
library versions, so record dependency changes when comparing submissions.
