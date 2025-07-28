# 4_Data_Analysis

This folder contains the data analysis components for AGIcam's yield prediction pipeline, implementing both Random Forest and Long Short-Term Memory (LSTM) models for wheat yield prediction using time-series vegetation index data.

## Overview

The data analysis pipeline processes time-series vegetation index (VI) data collected by AGIcam sensors to predict grain yield in wheat breeding trials. Two machine learning approaches are implemented:

1. **Random Forest Regression**: Uses Area Under Curve (AUC) features from VI time series
2. **Long Short-Term Memory (LSTM)**: Processes sequential VI data to capture temporal dependencies

## Folder Structure

```
4_Data_Analysis/
├── LSTM_TimeSerie_YieldPrediction/     # LSTM model implementation
├── RandomForest_TimeSerie_Yield.../    # Random Forest model implementation
└── README.md                           # This file
```

## Data Requirements

### Input Data Format
- **Time-series VI data**: JSON format with timestamp metadata
- **Vegetation Indices**: Seven VIs computed from RGB/NoIR imagery
  - Chlorophyll Index Green (CIgreen)
  - Enhanced Vegetation Index 2 (EVI2)
  - Green Normalized Difference Vegetation Index (GNDVI)
  - Normalized Difference Vegetation Index (NDVI)
  - Renormalized Difference Vegetation Index (RDVI)
  - Soil Adjusted Vegetation Index (SAVI)
  - Simple Ratio (SR)
- **Ground truth yield data**: Plot-level grain yield measurements
- **Metadata**: Plot IDs, replicate information, phenological stages

### Data Collection Schedule
- **Frequency**: 3 times per day (10:30, 12:00, 13:30)
- **Images per session**: 5 synchronized RGB and NoIR images
- **Season duration**: ~2 months (spring wheat), ~3 months (winter wheat)

## Model Implementations

### Random Forest Regression

**Approach**: 
- Converts VI time series into Area Under Curve (AUC) features using trapezoidal rule
- Divides growing season into temporal windows:
  - Initial 7-day window for early-season variability
  - Non-overlapping 3-day intervals thereafter
  - Results in 19 intervals (spring wheat) and 25 intervals (winter wheat)

**Key Features**:
- Uses scikit-learn RandomForestRegressor
- Hyperparameter optimization via grid search with LOOCV
- Feature importance analysis to identify key VIs and time windows
- Performance metrics: RMSE and MAPE

**Expected Performance**:
- **Spring Wheat**: RMSE = 514.18 kg/ha, MAPE = 8.11% (optimal: 2 days before heading)
- **Winter Wheat**: RMSE = 983.84 kg/ha, MAPE = 9.31% (optimal: 9 days before heading)

### Long Short-Term Memory (LSTM)

**Approach**:
- Processes sequential VI data to capture temporal dependencies
- Two input configurations: univariate (NDVI only) and multivariate (all 7 VIs)
- Per-plot evaluation identifying optimal prediction day for each plot

**Architectures**:
1. **Vanilla LSTM**: Single layer, 100 units, batch normalization, dropout (0.2)
2. **Stacked LSTM**: Two layers, 50 units each, ReLU activation

**Implementation Details**:
- Framework: TensorFlow
- Optimizer: Adam (learning rate = 0.0005)
- Loss function: Mean Squared Error (MSE)
- Data split: 80% training, 20% testing
- Regularization: L2 regularization, dropout

**Expected Performance**:
- **Spring Wheat**: RMSE = 221.76 kg/ha, Error = 3.41% (optimal: ~1 week after heading)
- **Winter Wheat**: RMSE = 210.28 kg/ha, Error = 1.62% (optimal: ~1 week after heading)

## Dependencies

### Python Libraries
- **scikit-learn**: Random Forest implementation and evaluation metrics
- **TensorFlow**: LSTM model development and training
- **pandas**: Data manipulation and preprocessing
- **numpy**: Numerical computations
- **matplotlib/seaborn**: Data visualization
- **scipy**: Statistical functions (trapezoidal rule for AUC)

---
© 2022 AGIcam - Phenomics Lab|Washington State University
