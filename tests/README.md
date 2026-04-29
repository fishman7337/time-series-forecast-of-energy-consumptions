# Tests

This folder contains the pytest suite for reusable code under
`src/energy_forecasting`.

The tests intentionally use small synthetic data so CI can run without access to
the private coursework CSV.

## Run

```powershell
python -m pytest --cov=energy_forecasting --cov-report=term-missing
```
