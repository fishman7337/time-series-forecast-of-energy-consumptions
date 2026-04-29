# Model Card

## Model Overview

The project compares ARIMA and SARIMAX models for monthly consumption
forecasting across three targets:

- Gas Consumption (tons)
- Electricity Consumption (MWh)
- Water Consumption (tons)

The notebook includes exploratory analysis, stationarity checks, baseline
modelling, tuned ARIMA models, SARIMAX models, residual analysis, and final
60-month forecasts.

## Current Final Configuration

| Target | Model | Order | Seasonal Order |
| --- | --- | --- | --- |
| Gas Consumption (tons) | ARIMA | `(18, 2, 9)` | N/A |
| Electricity Consumption (MWh) | SARIMAX | `(3, 1, 4)` | `(5, 1, 6, 12)` |
| Water Consumption (tons) | ARIMA | `(9, 2, 17)` | N/A |

## Intended Use

- Academic demonstration of time-series modelling.
- Reproducible forecasting experiments.
- Learning reference for converting notebooks into a tested ML codebase.

## Not Intended For

- Production grid planning.
- Financial, safety-critical, or public policy decisions without additional
  validation.
- Forecasting outside the statistical assumptions and historical scope of the
  dataset.

## Metrics

The reusable code reports:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R2 score
- Explained variance
- Mean Absolute Percentage Error (MAPE)

## Limitations

- Models are univariate by target; they do not currently include weather,
  pricing, population, industrial output, or policy variables.
- High ARIMA orders can overfit and may be slow to train.
- Log transformation requires strictly positive target values.
- Forecast intervals are not yet exported by the CLI.

## Responsible Use

Forecasts should be treated as decision support, not decision automation.
Review model outputs alongside residual diagnostics and domain context before
using them outside the coursework setting.
