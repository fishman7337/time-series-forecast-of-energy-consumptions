"""Feature preparation helpers for time-series modelling."""

from __future__ import annotations

import numpy as np
import pandas as pd


def train_test_split_by_horizon(
    data: pd.DataFrame | pd.Series,
    horizon: int,
) -> tuple[pd.DataFrame | pd.Series, pd.DataFrame | pd.Series]:
    """Split a time series so the final ``horizon`` rows are reserved for testing."""
    if horizon <= 0:
        raise ValueError("horizon must be greater than zero")
    if len(data) <= horizon:
        raise ValueError("horizon must be smaller than the number of observations")

    return data.iloc[:-horizon].copy(), data.iloc[-horizon:].copy()


def log_transform(data: pd.DataFrame | pd.Series) -> pd.DataFrame | pd.Series:
    """Apply a natural log transform after checking values are strictly positive."""
    if np.asarray(data <= 0).any():
        raise ValueError("log transformation requires strictly positive values")
    return np.log(data)


def inverse_log_transform(data: pd.DataFrame | pd.Series) -> pd.DataFrame | pd.Series:
    """Reverse a natural log transformation."""
    return np.exp(data)


def future_period_index(
    observed_index: pd.DatetimeIndex,
    steps: int,
    *,
    fallback_frequency: str = "MS",
) -> pd.DatetimeIndex:
    """Create a future date index that continues the observed time-series frequency."""
    if steps <= 0:
        raise ValueError("steps must be greater than zero")
    if not isinstance(observed_index, pd.DatetimeIndex):
        raise TypeError("observed_index must be a pandas DatetimeIndex")
    if observed_index.empty:
        raise ValueError("observed_index must contain at least one timestamp")

    frequency = pd.infer_freq(observed_index) or fallback_frequency
    offset = pd.tseries.frequencies.to_offset(frequency)
    start = observed_index[-1] + offset
    return pd.date_range(start=start, periods=steps, freq=offset)
