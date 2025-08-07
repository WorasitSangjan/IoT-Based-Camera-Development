# AGIcam: An Open-Source IoT-Based Camera System for Automated In-Field Phenotyping and Yield Prediction

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Open Source](https://img.shields.io/badge/Open%20Source-Yes-brightgreen.svg)
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Raspberry%20Pi-red.svg)](https://raspberrypi.org)
![Agriculture](https://img.shields.io/badge/Agriculture-Precision%20Agriculture-green.svg)
![Research](https://img.shields.io/badge/Research-WSU--Phenomics-navy.svg)



> **A low-cost, solar-powered IoT platform for high-frequency crop monitoring and yield prediction in wheat breeding trials**

## Overview

AGIcam is an open-source Internet of Things (IoT) camera system designed for automated in-field phenotyping and yield prediction. Developed at Washington State University's Phenomics Lab, this platform enables continuous, high-frequency monitoring essential for capturing rapid phenological transitions and dynamic crop responses in breeding programs.

![AGIcam Field Deployment](https://github.com/WorasitSangjan/IoT-based-Camera-Development/blob/main/images/figure1.png)

*Figure 1: AGIcam sensor system deployed in a winter wheat breeding trial during the 2022 growing season*

### Key Features

- **Solar-Powered Autonomy**: 6W solar panel with 6,400 mAh battery for season-long operation
- **Wireless Connectivity**: 4G LTE and Wi-Fi for real-time data transmission
- **Dual Camera System**: Synchronized RGB and NoIR imaging (3x daily capture-Adjustable depend on User's requirement)
- **Edge Computing**: On-device vegetation index calculation for 7 VIs
- **Cloud Integration**: Automated data transfer to InfluxDB with Grafana visualization
- **Low Cost**: $150-200 per sensor unit

## System Architecture

![AGIcam System Architecture](https://github.com/WorasitSangjan/IoT-based-Camera-Development/blob/main/images/figure2.png)

*Figure 2: System architecture of the AGIcam platform, illustrating its core components*

The AGIcam platform consists of four main components:

1. **[Hardware Development](1_Camera_Development/)** - Physical sensor design and 3D enclosures
2. **[Backend System](2_Backend_System/)** - Node-RED data pipeline and cloud integration  
3. **[Web Dashboard](3_AGIcam_Dashboard/)** - Real-time monitoring interface
4. **[Data Analysis](4_Data_Analysis/)** - Machine learning models for yield prediction

## Performance Highlights

### Field Deployment Results (2022 Season)
- **18 sensors** deployed across spring and winter wheat trials
- **85%+ uptime** maintained throughout the growing season
- **Sub-daily monitoring** with 3 imaging sessions per day
- **7 vegetation indices** computed in real-time

### Yield Prediction Accuracy
| Crop Type | Model | RMSE (kg/ha) | Error Rate |
|-----------|-------|--------------|------------|
| Spring Wheat | LSTM | 221.76 | 3.41% |
| Winter Wheat | LSTM | 210.28 | 1.62% |
| Spring Wheat | Random Forest | 544.79 | 8.60% |
| Winter Wheat | Random Forest | 1059.82 | 10.41% |

## Quick Start

### Hardware Requirements
- Raspberry Pi Compute Module 3+ Lite
- Dual Raspberry Pi Camera V2 (RGB + NoIR)
- 6W Solar Panel + 6,400 mAh Battery
- Witty Pi 3 power management
- Custom 3D-printed enclosure

### Software Stack
- **OS**: Raspbian Buster
- **Backend**: Node-RED, Python 3.7+
- **Database**: InfluxDB (time-series)
- **Visualization**: Grafana
- **Cloud**: Microsoft Azure


## Research Applications

### Published Results
Our research demonstrates AGIcam's effectiveness for:
- **Yield prediction** with LSTM achieving 1.62% error
- **Phenological monitoring** during critical growth stages
- **High-throughput phenotyping** in breeding programs
- **Real-time decision support** for crop management

### Citation
If you use AGIcam in your research, please cite:
```
Will be updated soon!
```

## Repository Structure

```
IoT-based-Camera-Development/
├── 1_Camera_Development/           # Hardware design & 3D models
│   ├── 1_Enclosure_3DModel/        # STL files for 3D printing
│   └── 2_Program_on_RasPi/         # Raspberry Pi software
├── 2_Backend_System/               # Node-RED data pipeline
│   ├── flows.json                  # Complete data flow
│   └── data_transform.js           # Data transformation
├── 3_AGIcam_Dashboard/             # Web interface
│   ├── index.html                  # Homepage
│   ├── dashboardlists.html         # Sensor dashboards
│   └── planthealth.html            # Image galleries
├── 4_Data_Analysis/                # ML models
│   ├── LSTM_TimeSerie_Yield.../    # LSTM implementation
│   └── RandomForest_TimeSerie_.../ # Random Forest models
└── requirements.txt                # Python dependencies
```

## License

This project is open source under the [MIT License](LICENSE). See the LICENSE file for details.

## Acknowledgments

This research was funded by:
- USDA-NIFA Competitive Project (Accession #1028108)
- Washington State University Hatch Project (Accession #1014919)
- WSU College of AHNRS Emerging Research Issues Grant (ERI-20-04)

## Contact

- **Lead Researcher**: Worasit Sangjan - [worasit.sangjan@wsu.edu](mailto:worasit.sangjan@wsu.edu)
- **Principal Investigator**: Dr. Sindhuja Sankaran - [s.sankaran@wsu.edu](mailto:s.sankaran@wsu.edu)
- **Institution**: Washington State University, Phenomics Lab

---
© 2022 AGIcam - Phenomics Lab|Washington State University
