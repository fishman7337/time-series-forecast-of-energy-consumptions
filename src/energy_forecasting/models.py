"""Forecast model specifications and training helpers."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Literal

import joblib
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX

from energy_forecasting.config import MODEL_DIR

ModelFamily = Literal["arima", "sarimax"]


@dataclass(frozen=True)
class ForecastModelSpec:
    """Serializable model configuration for one target series."""

    family: ModelFamily
    order: tuple[int, int, int]
    seasonal_order: tuple[int, int, int, int] | None = None

    def validate(self) -> None:
        """Validate the model family and required seasonal configuration."""

        if self.family not in {"arima", "sarimax"}:
            raise ValueError(f"Unsupported model family: {self.family}")
        if self.family == "sarimax" and self.seasonal_order is None:
            raise ValueError("SARIMAX models require a seasonal_order")


def fit_univariate_model(series: pd.Series, spec: ForecastModelSpec):
    """Fit an ARIMA or SARIMAX model to a single log-transformed target series."""

    spec.validate()
    if series.empty:
        raise ValueError("series must contain at least one observation")

    if spec.family == "arima":
        return ARIMA(series, order=spec.order).fit()

    return SARIMAX(series, order=spec.order, seasonal_order=spec.seasonal_order).fit()


def save_model(model, target_name: str, model_dir: str | Path = MODEL_DIR) -> Path:
    """Persist a fitted statsmodels result object with a filesystem-safe name."""

    output_dir = Path(model_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    safe_target = _safe_name(target_name)
    model_path = output_dir / f"{safe_target}_model.joblib"
    joblib.dump(model, model_path)
    return model_path


def _safe_name(value: str) -> str:
    return "_".join("".join(char.lower() if char.isalnum() else " " for char in value).split())
