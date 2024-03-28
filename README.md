# Cloud-Based IoT System with Virtual Sensors

## Introduction
This repository hosts code for a cloud-based Internet of Things (IoT) system tailored for collecting environmental data from virtual sensors. The system leverages MQTT protocol for communication and seamlessly integrates with the Thingspeak platform for data storage and visualization.

## Key Features
- Collects environmental data (temperature, humidity, CO2) from virtual sensors.
- Communicates with Thingspeak via MQTT for efficient data upload.
- Real-time monitoring and visualization of environmental data.
- Designed for deployment on MicroPython-enabled devices.

## Setup Instructions

### 1. Create Accounts:
   - Sign up for accounts on Wokwi and ThingSpeak platforms.

### 2. Configure ThingSpeak:
   - Upon logging into ThingSpeak, create a new channel with fields for temperature, humidity, and CO2 levels.
   - Add a new device on ThingSpeak and link it with the created channel.

## Getting Started

### 1. Clone the Repository:
   ```bash
   git clone https://github.com/Kenni001/IOT-Assigment.git
   cd IOT-Assigment
   ```

### 2. Configuration:
   - Customize MQTT broker details, ThingSpeak credentials, and Wi-Fi settings in the `main.py` file.
   - Ensure MicroPython environment is properly set up on your device.

### 3. Deploy the Code:
   - Upload the Python scripts (`main.py`) to your MicroPython-enabled device.

## Running the Code

### 1. Execution:
   - Run the `main.py` script on your MicroPython device to commence collecting and uploading sensor data.

## Dependencies

- MicroPython libraries
- `umqtt.simple` for MQTT communication
- `network` for Wi-Fi connectivity

## Usage

1. Ensure the MicroPython device is connected to the internet via Wi-Fi.
2. The device will continuously collect sensor data and upload it to ThingSpeak at regular intervals.
3. Access the ThingSpeak platform to visualize and analyze the collected data.
