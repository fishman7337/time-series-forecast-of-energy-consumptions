# Energy Consumption Forecasting

Energy Consumption Forecasting is a reproducible time-series project for
forecasting monthly gas, electricity, and water consumption using ARIMA and
SARIMAX models.

This project was completed at Singapore Polytechnic, School of Computing, under
the Diploma in Applied AI & Analytics. It was submitted for the AI & Machine
Learning module (ST1511), CA2 Part A, by Goh Kun Ming, DAAA student, in AY24/25
Year 1 Semester 2. The lecturer was Adjunct Lecturer Tai Hock Lin (Andy).

## Project Goals

- Clean and validate monthly energy consumption data.
- Explore trend, seasonality, stationarity, and autocorrelation.
- Train baseline ARIMA, tuned ARIMA, and SARIMAX forecasting models.
- Forecast gas, electricity, and water consumption for the next 60 months.
- Keep the original coursework notebook while adding reusable code, tests, CI,
  documentation, and MLOps scaffolding.

## Repository Structure

```text
.
+-- .github/                 # CI, security scans, issue and PR templates
+-- data/                    # Dataset contract and local data placeholders
|   +-- raw/                 # Place CA2-Energy-Consumption-Data.csv here
|   +-- processed/           # Generated clean datasets, not committed
+-- docs/                    # Data card, model card, MLOps, architecture notes
+-- models/                  # Generated model artifacts, not committed
+-- notebooks/               # Original narrative notebook
+-- reports/                 # Presentation and generated reports
+-- src/energy_forecasting/  # Reusable Python package
+-- tests/                   # Pytest suite
```

## Quick Start

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

Place the raw CA2 dataset at:

```text
data/raw/CA2-Energy-Consumption-Data.csv
```

Optional local configuration can be copied from `.env.example` if you prefer to
keep path and forecast settings in environment variables.

Validate the dataset:

```powershell
python -m energy_forecasting.cli validate --data data/raw/CA2-Energy-Consumption-Data.csv
```

Run tests and quality checks:

```powershell
python -m pytest
python -m ruff check .
python -m bandit -c pyproject.toml -r src
```

Train the configured final models:

```powershell
python -m energy_forecasting.cli train --data data/raw/CA2-Energy-Consumption-Data.csv
```

## Data Contract

The raw dataset is expected to contain:

| Column | Type | Notes |
| --- | --- | --- |
| `DATE` | date | Parsed as day-first dates, for example `01/01/2020`. |
| `Gas Consumption (tons)` | numeric | Must be strictly positive. |
| `Electricity Consumption (MWh)` | numeric | Must be strictly positive. |
| `Water Consumption (tons)` | numeric | Must be strictly positive. |

The raw dataset is not committed. See [docs/DATA_CARD.md](docs/DATA_CARD.md)
for the full data contract and handling notes.

## Main Artifacts

- Notebook: [notebooks/A-Time-Series.ipynb](notebooks/A-Time-Series.ipynb)
- Split notebooks: [notebooks/sections](notebooks/sections)
- Presentation: [reports/presentation/AIML-Part-A-Presentation-GohKunMing.pptx](reports/presentation/AIML-Part-A-Presentation-GohKunMing.pptx)
- Source package: [src/energy_forecasting](src/energy_forecasting)
- MLOps guide: [docs/MLOPS.md](docs/MLOPS.md)
- Model card: [docs/MODEL_CARD.md](docs/MODEL_CARD.md)

## Quality Gates

Every push should pass:

- `ruff` for linting and import order.
- `pytest` with coverage for reusable code.
- `bandit` for Python security checks.
- `pip-audit` for dependency vulnerability scanning.
- GitHub CodeQL analysis for static security review.

## Limitations

This is an academic forecasting project, not a production utility planning
system. Forecasts depend on the supplied historical dataset and should be
reviewed with domain knowledge before any operational use.
