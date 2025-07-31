# LSTM Time Series Yield Prediction

A deep learning system for predicting crop yields using LSTM neural networks with time series data from agricultural plots. The system processes vegetation indices and weather conditions to forecast final crop yield.

## 🌾 Overview

This project implements Long Short-Term Memory (LSTM) neural networks to predict wheat crop yields based on:
- **Vegetation Indices**: NDVI, EVI2, SAVI, GNDVI, etc.
- **Weather Conditions**: Temperature, humidity, precipitation, solar radiation
- **Time Series Data**: Daily measurements throughout growing season

## 🏗️ Project Structure

```
LSTM_TimeSerie_YieldPrediction/
├── DataStructures/           # Core data models
│   ├── conditions_state.py  # Weather/environmental data
│   ├── data_point.py        # Daily measurement point
│   ├── plot.py              # Agricultural plot data
│   └── vi_state.py          # Vegetation indices
├── Helpers/                  # Utility functions
│   ├── interpolator.py      # Missing data interpolation
│   ├── parser.py            # CSV data parsing
│   ├── utility.py           # General utilities
│   └── visualizer.py        # Data visualization
├── data_handler.py          # Main data processing & management
├── LSTM_model.py            # LSTM model implementations
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🚀 Quick Start

### Prerequisites
```bash
pip install -r requirements.txt
```

### Basic Usage

```python
from data_handler import DataHandler
from LSTM_model import VanillaLSTM, StackedLSTM

# 1. Initialize data handler with your plots data
data_handler = DataHandler(plots)

# 2. Create training/testing splits
data_handler.make_sets(
    target_variates=['ndvi', 'air_temp', 'relative_humidity'], 
    training_percentage_amt=80
)

# 3. Choose LSTM architecture
model = VanillaLSTM(num_epochs=300, verbose=1)
# OR for more complex model:
model = StackedLSTM(num_epochs=300, verbose=1)

# 4. Train the model
data_handler.train_on_training_sets(model)

# 5. Make predictions
data_handler.make_predictions_and_accuracies_for_test_sets(model)

# 6. Save trained model
model.save_trained_model(model_num=1)
```

## 📊 Features

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

## 📈 Data Format

The system expects agricultural plot data with:
- **Plot metadata**: variety, location, yield, etc.
- **Time series data**: Daily measurements of:
  - Vegetation indices (NDVI, EVI2, SAVI, etc.)
  - Weather conditions (temperature, humidity, etc.)

## 🎯 Use Cases

- **Precision Agriculture**: Optimize farming decisions
- **Yield Forecasting**: Predict harvest outcomes
- **Research**: Study crop-environment relationships
- **Risk Management**: Assess weather impact on yields

## 📋 Requirements

- Python 3.7+
- TensorFlow 2.x
- NumPy
- Pandas
- Matplotlib
- Scipy
- Colorama

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Agricultural research data providers
- TensorFlow and Keras development teams
- Open source community contributors

## 📞 Contact

For questions or collaboration opportunities, please open an issue or contact the repository maintainers.

---

**Made with ❤️ for sustainable agriculture and AI research**