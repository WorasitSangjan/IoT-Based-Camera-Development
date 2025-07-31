# AGIcam Dashboard

> Web-based interface for monitoring AGIcam IoT camera sensors in agricultural field trials.

## Overview

The AGIcam Dashboard provides real-time monitoring and historical data access for 18 camera sensors deployed in wheat breeding trials. Built with HTML5 and Bootstrap 5, it offers:

- **Real-time NDVI monitoring** via embedded Grafana dashboards
- **Historical image galleries** from field-deployed cameras  
- **Responsive design** for desktop and mobile access

## Screenshots

### Homepage - Field Deployment View
![AGIcam Homepage](https://github.com/WorasitSangjan/IoT-based-Camera-Development/blob/main/3_AGIcam_Dashboard/images/homepage-screenshort.png)
*Real AGIcam sensors deployed across wheat breeding trials showing field layout and installation*

### Dashboard - Real-time NDVI Monitoring  
![AGIcam Dashboard](https://github.com/WorasitSangjan/IoT-based-Camera-Development/blob/main/3_AGIcam_Dashboard/images/dashboard-screenshort.png)
*Grid view of all 18 camera sensors with embedded Grafana dashboards for live NDVI monitoring*

### Plant Health - Historical Data Access
![Plant Health Page](https://github.com/WorasitSangjan/IoT-based-Camera-Development/blob/main/3_AGIcam_Dashboard/images/planthealth-screenshort.png)
*Table interface providing access to historical NDVI image galleries for each camera sensor*

## Pages

### 1. Homepage (`index.html`)
Main landing page with AGIcam system overview and navigation to field deployment information.

### 2. Dashboard (`dashboardlists.html`) 
Grid layout displaying all 18 cameras with:
- Real-time NDVI dashboard previews
- Direct links to Grafana dashboards
- Organized by crop type (6 Winter Wheat + 12 Spring Wheat)

### 3. Plant Health (`planthealth.html`)
Table format providing:
- Complete device inventory with IDs and locations
- Direct links to historical image galleries

## File Structure

```
4_AGIcam_Dashboard/
├── index.html              # Homepage
├── dashboardlists.html     # Main dashboard  
├── planthealth.html        # Image galleries
└── images/
    ├── agicam.jpg         # Hero image
    └── agicam8ndvi.png    # NDVI thumbnail
```

## Quick Start

1. **Clone repository**
   ```bash
   git clone https://github.com/WorasitSangjan/IoT-based-Camera-Development.git
   cd IoT-based-Camera-Development/4_AGIcam_Dashboard
   ```

2. **Serve files locally**
   ```bash
   python -m http.server 8000
   ```

3. **Open browser**
   ```
   http://localhost:8000
   ```

## External Services

- **Grafana Dashboards**: `Use the link to Grafana on the cloud` - Real-time NDVI data
- **Image Server**: `Use the link to image database on the cloud` - Historical photos
- **Bootstrap CDN**: UI framework and responsive components

## Camera Layout

**18 Total Sensors:**
- **Winter Wheat (6)**: AGIcam4, 7, 8, 9, 11, 12
- **Spring Wheat (12)**: AGIcam13-25 (excluding 20)

**Capture Schedule:** 3 times daily (10:30, 12:00, 13:30)

## Technology Stack

- **Frontend**: HTML5, Bootstrap 5.0.2, JavaScript
- **Visualization**: Embedded Grafana dashboards
- **Responsive**: Mobile-friendly design
- **External APIs**: Real-time data from field sensors

## Features

- **Responsive navigation** with Bootstrap collapse menu
- **Real-time dashboards** embedded via iframes
- **Direct image access** to historical galleries
- **Mobile optimized** for field use
- **External link handling** opens in new tabs

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/WorasitSangjan/IoT-based-Camera-Development/blob/main/LICENSE) file for details.

---
© 2022 AGIcam - Phenomics Lab|Washington State University
