# Experiment 02, Run 01 

## Detailed Description of Experiment 02 - Part one

### Changes and update: 

- The Node-RED flow parses the incoming JSON messages and converts them into CSV format as well as into measurements for InfluxDB.
- So now the Measurement System logs the data into CSV as well as an InfluxDB database.
- In the firmware on the publishing sensor node, JSON message structure is changed to accomodate a unique device ID (DevUID).
- This DevUID is same as client ID of MQTT publishing client. MQTT Topic structure is also improved withe concept of logical hierarchy
- Grafana visualization system was installed on RP400 to visualize the data in real time by using charts and the guages.

### Software Description

#### Firmware for publishing node:

Firmware for the publishing node written on RPI picoW has the following changes:
- Sensor data is sent every 30 seconds instead on every 10 seconds
- Now the JSON message contains DevUID, MQTT Topic, Message Counter and usual sensor data.

![MS_PH01_P1_JSON_Message_V2](https://github.com/Vishusharma296/Measurement_Systems/assets/73486657/28b546f6-d843-489c-9ee2-23c825aabf4a)

#### Node-Red Flow

![MS1_PH1_P1_Node-red_flow_02](https://github.com/Vishusharma296/Measurement_Systems/assets/73486657/ca30ae14-3351-422d-814d-f413199d3fd6)

#### InfluxDB Database

![MS1_PH01_P1_Influxdb](https://github.com/Vishusharma296/Measurement_Systems/assets/73486657/58702692-c523-43db-91b8-7b7e144b517a)


### Publishing sensor Node-01

![MS1_PH01_Pub_node01](https://github.com/Vishusharma296/Measurement_Systems/assets/73486657/69cfb9e0-d3d5-4f8f-9423-272c57b5eb66)

## Key Info:

### General information about the experimental setup:

- Communication Protocols: MQTT for publishing node to broker, I2C from sensor to MCU
- Database System: CSV file Writing and Influx DB
- Data Visualization: Using Grafana

### Software Tools used: 
- InfluxDB (v1.xxx)
- Grafana Dashboards
- Mosquitto MQTT broker
- Node-red flow for MQTT client and data logging
- BMP280 and umqtt python libraray

### Hardware Tools used:
- RPI picoW board as MQTT publisher
- RPI400 as MQTT server, MQTT subscribing client, database system for logged sensor data in CSV format
- BMP280 temperature pressure sensor
- Mi Powerbank 2i (10,000 mAh) to power sensor node

#### Data analysis 

**Run 01**
- Duration: 01.05.2024 - 
- Polling frequency for sensor: 30 sec
- Total number of samples: 1500+ ...continued

**Data Visualization: desscription of Grafana dashboard**

![MS_PH01_P1_Grafana_Dashboard_V1](https://github.com/Vishusharma296/Measurement_Systems/assets/73486657/d5c2e696-8133-4c95-a9f3-cffb35018f67)


### Planned changes for next iterations of the experiment:














