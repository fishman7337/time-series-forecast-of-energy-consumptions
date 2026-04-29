from pathlib import Path

from energy_forecasting.cli import main


def test_cli_validate_loads_dataset(tmp_path, capsys) -> None:
    csv_path = _write_sample_csv(tmp_path / "sample.csv")

    exit_code = main(["validate", "--data", str(csv_path)])

    assert exit_code == 0
    assert "Validated 2 monthly observations" in capsys.readouterr().out


def _write_sample_csv(path: Path) -> Path:
    header = ",".join(
        [
            "DATE",
            "Gas Consumption (tons)",
            "Electricity Consumption (MWh)",
            "Water Consumption (tons)",
        ]
    )
    path.write_text(
        "\n".join(
            [
                header,
                "01/01/2020,10,100,1",
                "01/02/2020,20,200,2",
            ]
        ),
        encoding="utf-8",
    )
    return path
