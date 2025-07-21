# AGIcam Repository Structure

This repository contains the hardware and codes of AGIcam IoT-based camera system for automated field phenotyping.

## Branch Contents

### 1. **1_Camera_Development**
Hardware design components for the physical camera system:

## Hardware Components

![AGIcam Hardware Assembly](hardware_assembly.png)

The 3D printed enclosure system houses the following components:
- Raspberry Pi Compute Module 3+ Lite (main processing unit)
- Dual Raspberry Pi Camera V2 modules (RGB and NoIR)
- Witty Pi 3 power management board
- Voltaic battery system
- StereoPi board for dual camera control

**1_Enclosure_3DModel/** - 3D printable enclosure files:
- `CameraCOVER.stl` - STL file for camera protective cover
- `HousingCOVER.stl` - STL file for main enclosure lid  
- `InstallFLANGE.stl` - STL file for mounting flange
- `Sensor_housing.stl` - STL file for primary electronics housing

### 2. **2_Program_on_RasPi**
Software components that run on Raspberry Pi to automatically capture images and extract the plant traits:

**Documentation Files:**
- `0_crontab_docs.md` - Markdown file with scheduled task setup instructions
- `0_rustdesk_docs.md` - Markdown file with remote desktop access guide

**Python Scripts:**
- `1_capture_dual_img.py` - Python script for synchronized RGB/NoIR image capture
- `1_capture_dual_img_original.py` - Python script for synchronized RGB/NoIR image capture (original version)
- `2_extract_ndvi.py` - Python script for vegetation index calculation

## Python Requirements

**Recommended Python Version:** 3.7+

**Required Libraries:**
```bash
# For image capture scripts
pip3 install picamera2

# For NDVI processing
pip3 install opencv-python numpy
```

**Library Details:**
- `picamera2` - Raspberry Pi camera interface
- `opencv-python` (cv2) - Image processing
- `numpy` - Numerical operations
- Built-in libraries: `os`, `time`, `datetime`, `json`, `statistics`

---
© 2022 AGIcam - Phenomics Lab|Washington State University