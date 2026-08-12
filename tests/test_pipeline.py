import json

import numpy as np
import pandas as pd
import pytest

from energy_forecasting.config import TARGET_COLUMNS
from energy_forecasting.pipeline import (
    default_model_specs,
    train_and_save_default_models,
    write_json_report,
)


def test_default_model_specs_cover_all_targets() -> None:
    specs = default_model_specs()

    assert set(specs) == set(TARGET_COLUMNS)
    assert specs["Electricity Consumption (MWh)"].family == "sarimax"


def test_write_json_report_creates_parent_directory(tmp_path) -> None:
    output_path = tmp_path / "nested" / "metrics.json"

    written = write_json_report({"mae": 1.23}, output_path)

    assert written == output_path
    assert json.loads(output_path.read_text(encoding="utf-8")) == {"mae": 1.23}


@pytest.mark.parametrize("forecast_steps", [0, -1, 1.0, True, np.int64(1)])
def test_training_rejects_invalid_forecast_steps_before_writing_models(
    tmp_path,
    forecast_steps,
) -> None:
    with pytest.raises(ValueError, match="forecast_steps"):
        train_and_save_default_models(
            pd.DataFrame(),
            model_dir=tmp_path,
            forecast_steps=forecast_steps,
        )

    assert not any(tmp_path.iterdir())
