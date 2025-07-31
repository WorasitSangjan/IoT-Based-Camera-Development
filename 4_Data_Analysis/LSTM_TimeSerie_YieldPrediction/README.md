# LSTM Time Series Yield Prediction

A deep learning system for predicting crop yields using LSTM neural networks with time series data from AGIcam.

This project implements Long Short-Term Memory (LSTM) neural networks to predict wheat crop yields based on:
- **Vegetation Indices**: NDVI, EVI2, SAVI, GNDVI, etc.
- **Time Series Data**: Daily measurements throughout growing season

## Project Structure

```
LSTM_TimeSerie_YieldPrediction/
├── DataStructures/           # Core data models
│   ├── conditions_state.py   # Weather/environmental data
│   ├── data_point.py         # Daily measurement point
│   ├── plot.py               # Agricultural plot data
│   └── vi_state.py           # Vegetation indices
├── Helpers/                  # Utility functions
│   ├── interpolator.py       # Missing data interpolation
│   ├── parser.py             # CSV data parsing
│   ├── utility.py            # General utilities
│   └── visualizer.py         # Data visualization
├── data_handler.py           # Main data processing & management
├── lstm_model.py             # LSTM model implementations
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## Quick Start

### Prerequisites
```bash
pip install -r requirements.txt
```

## Features

### Data Processing
- **Automatic data interpolation** for missing values
- **Sequence preparation** for LSTM input formatting
- **Train/test splitting** with variety balancing
- **Data normalization** and preprocessing

### LSTM Models
- **VanillaLSTM**: Single-layer LSTM (100 units)
- **StackedLSTM**: Multi-layer LSTM (50+50 units)
- **Customizable architectures** with regularization
- **Early stopping** and model checkpointing

### Analysis Tools
- **Yield prediction** with accuracy metrics
- **Time series visualization** 
- **Correlation analysis** between variables and yield
- **Model performance evaluation**

## 🔧 Model Architecture

### VanillaLSTM
```
Input → Masking → LSTM(100) → BatchNorm → Dropout → Dense(1)
```

### StackedLSTM
```
Input → Masking → LSTM(50) → Dropout → BatchNorm → 
LSTM(50) → Dropout → BatchNorm → Dense(1)
```

## Data Format

The system expects agricultural plot data with:
- **Plot metadata**: variety, location, yield, etc.
- **Time series data**: Daily measurements of:
  - Vegetation indices (NDVI, EVI2, SAVI, etc.)

## Use Cases

- **Precision Agriculture**: Optimize farming decisions
- **Yield Forecasting**: Predict harvest outcomes
- **Research**: Study crop-environment relationships

## Requirements

- Python 3.7+
- TensorFlow 2.x
- NumPy
- Pandas
- Matplotlib
- Scipy
- Colorama

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/WorasitSangjan/IoT-based-Camera-Development/blob/main/LICENSE) file for details.

---
© 2022 AGIcam - Phenomics Lab|Washington State University
