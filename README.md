# Home Assistant MQTT Assignment

## Student Details
- Name: Eniyavan M
- Register Number: 42110332

## Project Overview
This project demonstrates Python to MQTT to Home Assistant integration.
Sensor values are published using a Python script to a unique MQTT topic
and displayed live in the Home Assistant dashboard.

## MQTT Details
- Broker: Mosquitto (Windows)
- Topic: home/eniyavan-2025/sensor

## Sensors Implemented
1. Temperature (25°C)
2. Humidity (60%)
3. Light Intensity (300 lux)

## Files in This Repository
- sensor_publish.py : Python script to publish sensor data
- screenshots/ : Contains Home Assistant and MQTT output screenshots
- summary.pdf : One-page assignment summary
- README.md : Project documentation

## Steps Followed
1. Installed Home Assistant OS using VirtualBox on Windows.
2. Installed and configured Mosquitto MQTT broker.
3. Developed a Python script to publish sensor data to MQTT.
4. Configured MQTT integration in Home Assistant.
5. Displayed live sensor values on the Home Assistant dashboard.

## How to Run
1. Start Mosquitto on Windows.
2. Run the Python script:
   python sensor_publish.py
3. Open Home Assistant dashboard to view live updates.

## Output
Sensor values update every 5 seconds in Home Assistant.
