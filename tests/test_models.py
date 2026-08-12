import numpy as np
import pandas as pd
import pytest

from energy_forecasting.models import ForecastModelSpec, fit_univariate_model


def test_sarimax_spec_requires_seasonal_order() -> None:
    spec = ForecastModelSpec(family="sarimax", order=(1, 1, 1))

    with pytest.raises(ValueError, match="seasonal_order"):
        spec.validate()


def test_arima_spec_validates_without_seasonal_order() -> None:
    spec = ForecastModelSpec(family="arima", order=(1, 1, 1))

    spec.validate()


@pytest.mark.parametrize(
    "order",
    [(-1, 1, 1), (1, 1), (1, 1, 1.5)],
)
def test_model_spec_rejects_invalid_orders(order) -> None:
    spec = ForecastModelSpec(family="arima", order=order)

    with pytest.raises(ValueError, match="three non-negative integers"):
        spec.validate()


@pytest.mark.parametrize("period", [0, -1, 1.0, True, np.int64(12)])
def test_sarimax_spec_rejects_invalid_seasonal_period(period) -> None:
    spec = ForecastModelSpec(
        family="sarimax",
        order=(1, 1, 1),
        seasonal_order=(1, 0, 1, period),
    )

    with pytest.raises(ValueError, match="plain positive integer period"):
        spec.validate()


def test_fit_model_rejects_non_finite_series() -> None:
    spec = ForecastModelSpec(family="arima", order=(1, 0, 0))

    with pytest.raises(ValueError, match="finite observations"):
        fit_univariate_model(pd.Series([1.0, float("inf"), 2.0]), spec)
