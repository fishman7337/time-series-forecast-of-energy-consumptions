"""Model evaluation metrics."""

from __future__ import annotations

import numpy as np
from sklearn.metrics import (
    explained_variance_score,
    mean_absolute_error,
    mean_absolute_percentage_error,
    mean_squared_error,
    r2_score,
)


def regression_metrics(y_true: np.ndarray, y_pred: np.ndarray) -> dict[str, float]:
    """Return the regression metrics used in the notebook and reports."""
    actual = np.asarray(y_true, dtype=float)
    predicted = np.asarray(y_pred, dtype=float)

    if actual.shape != predicted.shape:
        raise ValueError("y_true and y_pred must have the same shape")
    if actual.size == 0:
        raise ValueError("metrics require at least one observation")

    return {
        "mae": float(mean_absolute_error(actual, predicted)),
        "rmse": float(np.sqrt(mean_squared_error(actual, predicted))),
        "r2": float(r2_score(actual, predicted)),
        "explained_variance": float(explained_variance_score(actual, predicted)),
        "mape": float(mean_absolute_percentage_error(actual, predicted)),
    }
