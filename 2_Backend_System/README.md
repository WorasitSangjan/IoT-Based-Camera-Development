# AGIcam Backend Data Pipeline

**Node-RED data pipeline for transferring IoT sensor data from JSON files to InfluxDB time-series database.**

This repository shares the backend code we developed for our AGIcam project - an automated agricultural monitoring system using IoT cameras and vegetation index analysis.

## 📁 Repository Contents

| File | Description | Authors |
|------|-------------|---------|
| **`flows.json`** | Complete Node-RED flow for data transfer pipeline | Nisit Pukrongta and Worasit Sangjan |
| **`data-transform.js`** | JavaScript transformation function example | Nisit Pukrongta and Worasit Sangjan |

## What This Code Does

Our system reads vegetation index data from JSON files and transfers it to InfluxDB for analysis and visualization:

![AGIcam Data Pipeline](path/to/your/diagram.png)

The pipeline automatically processes data at scheduled intervals, transforming nested JSON structures into time-series database format suitable for analysis and dashboard visualization.

### The Pipeline Flow
1. **Trigger Scheduled Data Flow** - Initiates processing at defined time intervals
2. **Read JSON File** - Loads vegetation index data from Raspberry Pi's SD storage
3. **Parse JSON to Object** - Converts JSON file into JavaScript object (msg.payload)
4. **Function Node** - Transforms data structure and adds metadata + routing
5. **Database Node** - Writes VI data and metadata to InfluxDB time-series database

## What You Can Adapt for Your Project

### For IoT Data Transfer Projects
- **Node-RED flow structure** - Basic pipeline pattern for file → database transfer
- **JSON to InfluxDB transformation** - Converting nested data to time-series format
- **Multi-sensor data handling** - Processing data from multiple IoT devices
- **Automated scheduling** - Triggered data processing workflow

### Customizable Components
- **Input source**: Change from JSON files to MQTT, HTTP, or other data sources
- **Data transformation**: Modify the JavaScript function for your data structure
- **Output database**: Replace InfluxDB with PostgreSQL, MongoDB, etc.
- **Number of sensors**: Scale up/down for your sensor network

## Quick Setup

1. **Import the flow**: Copy `flows.json` content into Node-RED
2. **Modify data paths**: Update file paths and database connections for your setup
3. **Customize transformation**: Edit the function node using `data-transform.js` as reference
4. **Deploy and test**: Run the pipeline with your data

## Our Data Structure Example

**Input (JSON file)**:
```json
{
  "rep1": {
    "vr1_1": {
      "timestamp": "2022-05-15T12:00:00Z",
      "mean": 0.85,
      "median": 0.84,
      "std": 0.12,
      "max": 0.95
    }
  }
}
```

**Output (InfluxDB)**:
```javascript
{
  measurement: "vr1_1",
  fields: { mean: 0.85, median: 0.84, std: 0.12, max: 0.95 },
  tags: { plot: "rep1" },
  timestamp: new Date()
}
```

## Technology Stack

- **Node-RED**: Visual programming for IoT data flows
- **InfluxDB 1.x**: Time-series database for sensor data
- **JavaScript**: Data transformation logic

---
© 2022 AGIcam - Phenomics Lab|Washington State University