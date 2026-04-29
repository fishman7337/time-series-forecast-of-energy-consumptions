"""Data loading, schema validation, and cleaning helpers."""

from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path

import pandas as pd

from energy_forecasting.config import DATE_COLUMN, DEFAULT_DATA_PATH, TARGET_COLUMNS


def load_energy_data(path: str | Path = DEFAULT_DATA_PATH) -> pd.DataFrame:
    """Load the raw coursework CSV and return a validated time-indexed frame."""

    csv_path = Path(path)
    if not csv_path.exists():
        raise FileNotFoundError(
            f"Dataset not found at {csv_path}. Place the CA2 CSV under data/raw/ "
            "or pass --data with the dataset path."
        )

    raw = pd.read_csv(csv_path)
    return prepare_energy_dataframe(raw)


def prepare_energy_dataframe(
    df: pd.DataFrame,
    *,
    date_column: str = DATE_COLUMN,
    target_columns: Iterable[str] = TARGET_COLUMNS,
    drop_duplicate_dates: bool = True,
) -> pd.DataFrame:
    """Validate, type-cast, sort, and index the energy consumption dataframe."""

    target_columns = tuple(target_columns)
    required_columns = (date_column, *target_columns)
    validate_schema(df, required_columns)

    prepared = df.loc[:, required_columns].copy()
    prepared[date_column] = pd.to_datetime(prepared[date_column], dayfirst=True, errors="raise")

    for column in target_columns:
        prepared[column] = pd.to_numeric(prepared[column], errors="raise")

    prepared = prepared.dropna(subset=required_columns)
    if drop_duplicate_dates:
        prepared = prepared.sort_values(date_column).drop_duplicates(
            subset=date_column,
            keep="last",
        )

    prepared = prepared.sort_values(date_column).set_index(date_column)
    prepared.index.name = date_column
    validate_positive_targets(prepared, target_columns)
    return prepared


def validate_schema(df: pd.DataFrame, required_columns: Iterable[str]) -> None:
    """Raise a readable error if expected columns are missing."""

    missing = [column for column in required_columns if column not in df.columns]
    if missing:
        missing_text = ", ".join(missing)
        raise ValueError(f"Dataset is missing required column(s): {missing_text}")


def validate_positive_targets(
    df: pd.DataFrame,
    target_columns: Iterable[str] = TARGET_COLUMNS,
) -> None:
    """Ensure target values are strictly positive before log transformation."""

    invalid_counts = {
        column: int((df[column] <= 0).sum())
        for column in target_columns
        if column in df.columns and int((df[column] <= 0).sum()) > 0
    }
    if invalid_counts:
        details = ", ".join(f"{column}: {count}" for column, count in invalid_counts.items())
        raise ValueError(
            "Consumption values must be strictly positive for log-transformed "
            f"time-series models. Invalid counts: {details}"
        )


def remove_iqr_outliers(
    df: pd.DataFrame,
    columns: Iterable[str],
    *,
    whisker_width: float = 1.5,
) -> tuple[pd.DataFrame, dict[str, tuple[float, float]]]:
    """Remove IQR outliers from selected columns and return the cleaned data plus bounds."""

    cleaned = df.copy()
    bounds: dict[str, tuple[float, float]] = {}

    for column in columns:
        if column not in cleaned.columns:
            raise ValueError(f"Cannot calculate outliers for missing column: {column}")

        first_quartile = cleaned[column].quantile(0.25)
        third_quartile = cleaned[column].quantile(0.75)
        iqr = third_quartile - first_quartile
        lower_bound = float(first_quartile - whisker_width * iqr)
        upper_bound = float(third_quartile + whisker_width * iqr)
        bounds[column] = (lower_bound, upper_bound)

        mask = cleaned[column].between(lower_bound, upper_bound) | cleaned[column].isna()
        cleaned = cleaned.loc[mask]

    return cleaned, bounds
