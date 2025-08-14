# Energy Consumption Forecasting – Time Series Analysis

## Project Overview
This project focuses on forecasting **energy consumption trends** using **time series analysis** techniques.  
It leverages ARIMA and SARIMAX models to generate accurate predictions, with deployments for **gas**, **energy**, and **water** consumption.

---

## Features
- **Data Cleaning & Preprocessing**
  - Missing data detection and handling
  - Removal of duplicate entries
  - Correcting data types and setting proper time index
  - Outlier detection and treatment

- **Exploratory Data Analysis**
  - Univariate statistical analysis
  - Seasonal decomposition
  - ACF/PACF plots for autocorrelation insights
  - Augmented Dickey-Fuller (ADF) Test for stationarity
  - Ljung-Box Test for randomness

- **Model Development**
  - **Baseline:** ARIMA
  - **Optimised ARIMA:** Grid Search for best parameters
  - **Advanced Model:** SARIMAX for seasonality and exogenous variables

- **Model Evaluation & Selection**
  - Performance metrics for comparison
  - Best model selection based on accuracy and residual diagnostics

- **Deployment**
  - Forecasting models deployed for:
    - Gas consumption
    - Energy consumption
    - Water consumption

---

## Technologies Used
- **Python**  
- **Pandas**, **NumPy** – Data processing  
- **Matplotlib**, **Seaborn** – Data visualisation  
- **statsmodels** – Time series modelling  
- **ARIMA**, **SARIMAX**  

---

## Results
- Accurate forecasts for short-term energy usage
- Robust handling of seasonality and trends
- Deployable model pipelines for multiple consumption types
