"""Project configuration and shared constants."""

from __future__ import annotations

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
MODEL_DIR = PROJECT_ROOT / "models"
REPORTS_DIR = PROJECT_ROOT / "reports"

DATE_COLUMN = "DATE"
TARGET_COLUMNS = (
    "Gas Consumption (tons)",
    "Electricity Consumption (MWh)",
    "Water Consumption (tons)",
)

DEFAULT_DATA_PATH = RAW_DATA_DIR / "CA2-Energy-Consumption-Data.csv"
DEFAULT_FORECAST_STEPS = 60
DEFAULT_TEST_HORIZON = 60

DEFAULT_MODEL_CONFIG = {
    "Gas Consumption (tons)": {
        "family": "arima",
        "order": (18, 2, 9),
    },
    "Electricity Consumption (MWh)": {
        "family": "sarimax",
        "order": (3, 1, 4),
        "seasonal_order": (5, 1, 6, 12),
    },
    "Water Consumption (tons)": {
        "family": "arima",
        "order": (9, 2, 17),
    },
}
