import pytest

from energy_forecasting.models import ForecastModelSpec


def test_sarimax_spec_requires_seasonal_order() -> None:
    spec = ForecastModelSpec(family="sarimax", order=(1, 1, 1))

    with pytest.raises(ValueError, match="seasonal_order"):
        spec.validate()


def test_arima_spec_validates_without_seasonal_order() -> None:
    spec = ForecastModelSpec(family="arima", order=(1, 1, 1))

    spec.validate()
