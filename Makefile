.PHONY: install lint test security audit quality validate evaluate train

install:
	python -m pip install --upgrade pip
	python -m pip install -r requirements-dev.txt

lint:
	python -m ruff check .

test:
	python -m pytest --cov=energy_forecasting --cov-report=term-missing

security:
	python -m bandit -c pyproject.toml -r src

audit:
	python -m pip_audit -r requirements-audit.txt

quality: lint test security audit

validate:
	python -m energy_forecasting.cli validate --data data/raw/CA2-Energy-Consumption-Data.csv

evaluate:
	python -m energy_forecasting.cli evaluate --data data/raw/CA2-Energy-Consumption-Data.csv

train:
	python -m energy_forecasting.cli train --data data/raw/CA2-Energy-Consumption-Data.csv
