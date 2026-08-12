import pandas as pd
import pytest

from energy_forecasting.config import TARGET_COLUMNS
from energy_forecasting.data import prepare_energy_dataframe, remove_iqr_outliers


def _raw_frame() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "DATE": ["01/03/2020", "01/01/2020", "01/02/2020"],
            "Gas Consumption (tons)": [30.0, 10.0, 20.0],
            "Electricity Consumption (MWh)": [300.0, 100.0, 200.0],
            "Water Consumption (tons)": [3.0, 1.0, 2.0],
        }
    )


def test_prepare_energy_dataframe_parses_sorts_and_indexes_dates() -> None:
    prepared = prepare_energy_dataframe(_raw_frame())

    assert list(prepared.columns) == list(TARGET_COLUMNS)
    assert prepared.index.name == "DATE"
    assert prepared.index.is_monotonic_increasing
    assert prepared.iloc[0]["Gas Consumption (tons)"] == 10.0


def test_prepare_energy_dataframe_rejects_missing_columns() -> None:
    with pytest.raises(ValueError, match="missing required column"):
        prepare_energy_dataframe(_raw_frame().drop(columns=["Water Consumption (tons)"]))


def test_prepare_energy_dataframe_rejects_non_positive_targets() -> None:
    raw = _raw_frame()
    raw.loc[0, "Gas Consumption (tons)"] = 0

    with pytest.raises(ValueError, match="strictly positive"):
        prepare_energy_dataframe(raw)


def test_prepare_energy_dataframe_rejects_missing_months() -> None:
    raw = _raw_frame().drop(index=2)

    with pytest.raises(ValueError, match="every consecutive month"):
        prepare_energy_dataframe(raw)


def test_prepare_energy_dataframe_rejects_multiple_rows_in_one_month() -> None:
    raw = _raw_frame()
    raw.loc[0, "DATE"] = "15/02/2020"

    with pytest.raises(ValueError, match="every consecutive month"):
        prepare_energy_dataframe(raw)


def test_remove_iqr_outliers_returns_bounds() -> None:
    data = pd.DataFrame({"value": [10, 11, 12, 13, 1000]})

    cleaned, bounds = remove_iqr_outliers(data, ["value"])

    assert len(cleaned) == 4
    assert "value" in bounds
