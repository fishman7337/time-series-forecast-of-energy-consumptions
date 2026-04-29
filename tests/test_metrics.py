import numpy as np
import pytest

from energy_forecasting.metrics import regression_metrics


def test_regression_metrics_returns_expected_keys() -> None:
    metrics = regression_metrics(np.array([1.0, 2.0, 3.0]), np.array([1.1, 1.9, 3.2]))

    assert set(metrics) == {"mae", "rmse", "r2", "explained_variance", "mape"}
    assert metrics["mae"] > 0


def test_regression_metrics_rejects_shape_mismatch() -> None:
    with pytest.raises(ValueError, match="same shape"):
        regression_metrics(np.array([1.0, 2.0]), np.array([1.0]))
