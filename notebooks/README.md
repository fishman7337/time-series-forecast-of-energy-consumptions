# Notebooks

This folder contains the original coursework notebook:

```text
A-Time-Series.ipynb
```

The notebook preserves the narrative analysis and visual explanation. Reusable
code for CI and testing lives under `src/energy_forecasting`.

## Split Notebooks

The original full notebook is retained unchanged as the canonical artifact.
Smaller section notebooks are generated under `notebooks/sections/` for easier
review and navigation:

| File | Content |
| --- | --- |
| `00_project_context.ipynb` | Title, academic context, objective, and background. |
| `01_importing_modules.ipynb` | Imports and setup cells. |
| `02_data_analysis.ipynb` | CSV loading and initial data analysis. |
| `03_data_cleaning.ipynb` | Missing values, duplicates, and date conversion. |
| `04_feature_engineering.ipynb` | Outlier identification and treatment. |
| `05_data_visualisation.ipynb` | Univariate, stationarity, and autocorrelation analysis. |
| `06_model_training.ipynb` | Preprocessing, baseline ARIMA, ARIMA, and SARIMAX training. |
| `07_model_evaluation_and_deployment.ipynb` | Model comparison, selection, final forecasting, and implications. |

Use `sections/manifest.json` to trace each split notebook back to its original
cell range in `A-Time-Series.ipynb`.
