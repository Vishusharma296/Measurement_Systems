# Experiment 02, Prototype-01, Run 01 

## Detailed Description of Experiment 02 

### Changes and update: 

- The Node-RED flow parses the incoming JSON messages and converts them into CSV format as well as into measurements for InfluxDB.
- So now the Measurement System logs the data into CSV as well as into the InfluxDB database.
- In the firmware on the publishing sensor node, JSON message structure is changed to accomodate a unique device ID (DevUID).
- This DevUID is same as client ID of MQTT publishing client. MQTT Topic structure is also improved by using the concept of logical hierarchy
- Grafana visualization system was installed on RP400 to visualize the data in real time by using charts and the guages.

### Software Description

#### Firmware for publishing node (Pico-01):

Firmware for the publishing node written on RPI picoW has the following changes:
- Sensor data is sent every 30 seconds instead on every 10 seconds
- Now the JSON message contains DevUID, MQTT Topic, Message Counter and usual sensor data. See the image below to see the structure of the JSON message.

![MS_PH01_P1_JSON_Message_V2](https://github.com/Vishusharma296/Measurement_Systems/assets/73486657/28b546f6-d843-489c-9ee2-23c825aabf4a)

#### Node-RED Flow

![MS1_PH1_P1_Node-red_flow_02](https://github.com/Vishusharma296/Measurement_Systems/assets/73486657/ca30ae14-3351-422d-814d-f413199d3fd6)

The Node-RED flow used in this experiment has two sub flows. First subflow converts the JSON message into CSV format and then log this data into CSV file whenever a new message comes. Second sublow, extracts the temperature, pressure and message counter key-value pairs from the incoming JSON message. It then feeds these three extracted values in the InfluxDB database named as `Sensor DB01` as sepearate measurements. The measurement in the database follows the MQTT Topic heirarchy structure as shown in the figure below.

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
- Mi Powerbank 2i (10,000 mAh) to power the sensor node

#### Data analysis 

**Run 01**
- Duration: 01.05.2024 - 
- Polling frequency for sensor: 30 sec
- Total number of samples: 10,000+ ...continued

**Data Visualization: desscription of Grafana dashboard**

![MS_PH01_P1_Grafana_Dashboard_V1](https://github.com/Vishusharma296/Measurement_Systems/assets/73486657/d5c2e696-8133-4c95-a9f3-cffb35018f67)

### Limitations of the current network architechture:

- Data is sent as without encryption as plain JSON text message to the MQTT broker
- Telemetry data stops when the connection to WLAN is interrupted for MQTT broker (RPI400) and publisher (RPI picoW)
- Quality of the firmware is poor. It uses too much energy. A fully charged 10,000 mAh power bank runs for about(... reading and ... days)

### Planned changes for further Experiments:

#### Possible improvement in firmware
- Make use of concurrent programming in micropython to improve the firmware.
- Try multi-threadingding and event driven programming with uasync io in Micropython.
- `{"DevUID":"DevEUI-Pub_pico-01","MQTT_Topic":"Sensor/BMP280-01","Temperature_C":21.97,"Message_counter":482,"Pressure_P":97107.59}`
- The size of the current pubilshed message is 129 Bytes. This is too large and need to be reduced in size

#### Data Visualization
- Learn about the Grafana Kiosk mode.
- Try to access the Grafana dashboard from a computer outside the local network.

#### Experiment 03

- Program the temperature pressure node picoW-01 with concurrent programming.
- PicoW takes temperature and pressure reading every 30 seconds.
- Stores the readings on the local buffer on PicoW board
- Try to connect with WiFi every 5-10 minutes and light the onboard LED for 1-2 seconds.
- Try to connect and publish data to MQTT broker every 5-10 minutes

#### Experiment  04

**Goals** : Program another picoW /ESP32 board to do the following tasks:
Task1: Read ADC value from one of the pins 10-1000 times every second (Say antenna)
Task2: Store the data into a vector
Task3: Perform FFT for the incoming signal in real time.
Task4: Show the fequency spectrum result in a graph .












