"""End-to-end evaluation and training workflow helpers."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from energy_forecasting.config import (
    DEFAULT_FORECAST_STEPS,
    DEFAULT_MODEL_CONFIG,
    DEFAULT_TEST_HORIZON,
    MODEL_DIR,
    TARGET_COLUMNS,
)
from energy_forecasting.features import (
    inverse_log_transform,
    log_transform,
    train_test_split_by_horizon,
)
from energy_forecasting.metrics import regression_metrics
from energy_forecasting.models import ForecastModelSpec, fit_univariate_model, save_model


def default_model_specs() -> dict[str, ForecastModelSpec]:
    """Build typed model specifications from the project config."""
    specs: dict[str, ForecastModelSpec] = {}
    for target, config in DEFAULT_MODEL_CONFIG.items():
        specs[target] = ForecastModelSpec(
            family=config["family"],
            order=config["order"],
            seasonal_order=config.get("seasonal_order"),
        )
    return specs


def evaluate_model(
    data: pd.DataFrame,
    target: str,
    spec: ForecastModelSpec,
    *,
    horizon: int = DEFAULT_TEST_HORIZON,
) -> dict[str, float]:
    """Evaluate one configured model against a chronological holdout window."""
    train, test = train_test_split_by_horizon(data[target], horizon)
    train_log = log_transform(train)
    fitted_model = fit_univariate_model(train_log, spec)
    forecast_log = fitted_model.forecast(steps=len(test))
    forecast = inverse_log_transform(forecast_log)
    return regression_metrics(test.to_numpy(), forecast.to_numpy())


def train_and_save_default_models(
    data: pd.DataFrame,
    *,
    model_dir: str | Path = MODEL_DIR,
    forecast_steps: int = DEFAULT_FORECAST_STEPS,
) -> dict[str, dict[str, str | list[float]]]:
    """Train final models on all available data, save them, and return forecast metadata."""
    specs = default_model_specs()
    results: dict[str, dict[str, str | list[float]]] = {}

    for target in TARGET_COLUMNS:
        full_series_log = log_transform(data[target])
        fitted_model = fit_univariate_model(full_series_log, specs[target])
        model_path = save_model(fitted_model, target, model_dir)
        forecast = inverse_log_transform(fitted_model.forecast(steps=forecast_steps))

        results[target] = {
            "model_path": str(model_path),
            "forecast": [float(value) for value in forecast],
        }

    return results


def write_json_report(payload: dict, output_path: str | Path) -> Path:
    """Write a JSON metrics or forecast report."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return path
