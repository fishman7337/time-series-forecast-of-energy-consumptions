import numpy as np
import pandas as pd
import pytest

from energy_forecasting.features import (
    future_period_index,
    inverse_log_transform,
    log_transform,
    train_test_split_by_horizon,
)


def test_train_test_split_by_horizon_keeps_final_rows_for_test() -> None:
    series = pd.Series(range(6))

    train, test = train_test_split_by_horizon(series, horizon=2)

    assert train.tolist() == [0, 1, 2, 3]
    assert test.tolist() == [4, 5]


def test_train_test_split_by_horizon_rejects_invalid_horizon() -> None:
    with pytest.raises(ValueError, match="horizon"):
        train_test_split_by_horizon(pd.Series([1, 2]), horizon=2)


def test_log_transform_round_trip() -> None:
    values = pd.Series([1.0, np.e, np.e**2])

    transformed = log_transform(values)

    assert inverse_log_transform(transformed).round(8).equals(values.round(8))


def test_log_transform_rejects_zero_or_negative_values() -> None:
    with pytest.raises(ValueError, match="strictly positive"):
        log_transform(pd.Series([1.0, 0.0, -1.0]))


def test_future_period_index_continues_monthly_frequency() -> None:
    observed = pd.date_range("2020-01-01", periods=3, freq="MS")

    future = future_period_index(observed, 2)

    assert future.tolist() == [
        pd.Timestamp("2020-04-01"),
        pd.Timestamp("2020-05-01"),
    ]
