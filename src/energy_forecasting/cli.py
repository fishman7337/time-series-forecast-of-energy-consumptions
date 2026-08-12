"""Command-line entry points for validation, evaluation, and training."""

from __future__ import annotations

import argparse
from pathlib import Path

from energy_forecasting.config import (
    DEFAULT_DATA_PATH,
    DEFAULT_TEST_HORIZON,
    MODEL_DIR,
    REPORTS_DIR,
    TARGET_COLUMNS,
)
from energy_forecasting.data import load_energy_data
from energy_forecasting.pipeline import (
    default_model_specs,
    evaluate_model,
    train_and_save_default_models,
    write_json_report,
)


def build_parser() -> argparse.ArgumentParser:
    """Build the energy-forecasting workflow argument parser.

    Returns:
        Parser with validation, evaluation, and training subcommands.
    """
    parser = argparse.ArgumentParser(description="Energy consumption forecasting workflow")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate = subparsers.add_parser("validate", help="Validate the raw CSV schema")
    validate.add_argument("--data", type=Path, default=DEFAULT_DATA_PATH)

    evaluate = subparsers.add_parser("evaluate", help="Evaluate configured models")
    evaluate.add_argument("--data", type=Path, default=DEFAULT_DATA_PATH)
    evaluate.add_argument("--horizon", type=int, default=DEFAULT_TEST_HORIZON)
    evaluate.add_argument("--metrics-file", type=Path, default=REPORTS_DIR / "metrics.json")

    train = subparsers.add_parser("train", help="Train and persist final models")
    train.add_argument("--data", type=Path, default=DEFAULT_DATA_PATH)
    train.add_argument("--models-dir", type=Path, default=MODEL_DIR)
    train.add_argument("--forecast-file", type=Path, default=REPORTS_DIR / "forecasts.json")
    train.add_argument("--forecast-steps", type=int, default=60)

    return parser


def main(argv: list[str] | None = None) -> int:
    """Run validation, evaluation, or model training.

    Args:
        argv: Optional argument list. Uses process arguments when omitted.

    Returns:
        Process exit code for the selected workflow.
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    data = load_energy_data(args.data)

    if args.command == "validate":
        print(f"Validated {len(data)} monthly observations across {len(TARGET_COLUMNS)} targets.")
        return 0

    if args.command == "evaluate":
        specs = default_model_specs()
        metrics = {
            target: evaluate_model(data, target, specs[target], horizon=args.horizon)
            for target in TARGET_COLUMNS
        }
        output_path = write_json_report(metrics, args.metrics_file)
        print(f"Metrics written to {output_path}")
        return 0

    if args.command == "train":
        forecasts = train_and_save_default_models(
            data,
            model_dir=args.models_dir,
            forecast_steps=args.forecast_steps,
        )
        output_path = write_json_report(forecasts, args.forecast_file)
        print(f"Forecasts written to {output_path}")
        return 0

    parser.error(f"Unsupported command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
