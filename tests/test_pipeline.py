import json

from energy_forecasting.config import TARGET_COLUMNS
from energy_forecasting.pipeline import default_model_specs, write_json_report


def test_default_model_specs_cover_all_targets() -> None:
    specs = default_model_specs()

    assert set(specs) == set(TARGET_COLUMNS)
    assert specs["Electricity Consumption (MWh)"].family == "sarimax"


def test_write_json_report_creates_parent_directory(tmp_path) -> None:
    output_path = tmp_path / "nested" / "metrics.json"

    written = write_json_report({"mae": 1.23}, output_path)

    assert written == output_path
    assert json.loads(output_path.read_text(encoding="utf-8")) == {"mae": 1.23}
