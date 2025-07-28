# Data Analysis

This folder contains the data analysis components for AGIcam's yield prediction pipeline, implementing both Random Forest and Long Short-Term Memory (LSTM) models for wheat yield prediction using time-series vegetation index data.

## Overview

The data analysis pipeline processes time-series vegetation index (VI) data collected by AGIcam sensors to predict grain yield in wheat breeding trials. Two machine learning approaches are implemented:

1. **Random Forest Regression**: Uses Area Under Curve (AUC) features from the VI time series
2. **Long Short-Term Memory (LSTM)**: Processes sequential VI data to capture temporal dependencies

## Folder Structure

```
4_Data_Analysis/
├── LSTM_TimeSerie_YieldPrediction/     # LSTM model implementation
├── RandomForest_TimeSerie_Yield.../    # Random Forest model implementation
└── README.md                           # This file
```

## Data Requirements

### Dataset Availability
**Dataset will be published on Zenodo** - Link will be shared soon

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

<img src="https://raw.githubusercontent.com/WorasitSangjan/IoT-based-Camera-Development/main/4_Data_Analysis/images/flow.png" alt="Machine Learning and Deep Learning Workflow" width="750">

*Figure: Machine learning and deep learning frameworks for yield prediction using time-series vegetation index (VI) data*

### Random Forest Regression

**Approach**: 
- Converts VI time series into Area Under Curve (AUC) features using the trapezoidal rule
- Divides the growing season into temporal windows:
  - Initial 7-day window for early-season variability
  - Non-overlapping 3-day intervals thereafter
  - Results in 19 intervals (spring wheat) and 25 intervals (winter wheat)

**Workflow**:
1. **VI Time Series + Yield Data** → Combined input datasets
2. **AUC Computation** → Trapezoidal integration across 3-day intervals
3. **Feature Matrix** → Structured input for model training
4. **Model Training** → Random Forest with Grid Search + LOOCV optimization
5. **Evaluation** → RMSE and MAPE performance metrics

**Key Features**:
- Uses scikit-learn RandomForestRegressor
- Hyperparameter optimization via grid search with LOOCV
- Feature importance analysis to identify key VIs and time windows
- Performance metrics: RMSE and MAPE

### Long Short-Term Memory (LSTM)

**Approach**:
- Processes sequential VI data to capture temporal dependencies
- Two input configurations: 
  - **Univariate**: NDVI only
  - **Multivariate**: All 7 VIs
- Per-plot evaluation identifying optimal prediction day for each plot

**Workflow**:
1. **Data Preprocessing** → Interpolation and normalization
2. **Model Training** → LSTM architectures with temporal sequence processing
3. **Evaluation** → RMSE, Percent Error, and Optimal Prediction Day identification

**Architectures**:
- **Vanilla LSTM**: 1 Layer, 100 cells/layer
- **Stacked LSTM**: 2 Layers, 50 cells/layer

**Implementation Details**:
- Framework: TensorFlow
- 80/20 Train-Test Split
- Optimizer: Adam (learning rate = 0.0005)
- Loss function: Mean Squared Error (MSE)
- Regularization: L2 regularization, dropout (0.2)

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
