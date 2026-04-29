from energy_forecasting.models import save_model


def test_save_model_uses_filesystem_safe_target_name(tmp_path) -> None:
    model_path = save_model({"model": "placeholder"}, "Gas Consumption (tons)", tmp_path)

    assert model_path.name == "gas_consumption_tons_model.joblib"
    assert model_path.exists()
