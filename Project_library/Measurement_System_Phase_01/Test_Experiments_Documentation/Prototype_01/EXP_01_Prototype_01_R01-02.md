# Experiment 01, Prototype-01, Run 01-02 

## Detailed Description of Experiment 01 - Part one

### Objective: Create a wireless sensor data measurement system. 

Its various sub systems performs the following tasks:
- RPI picoW reads the sensor data from a BMP280 sensor using I2C every 10 seconds.
- RPI picoW sends the sensor data to an MQTT server (hosted by RPI400) in JSON format by acting as an MQTT publisher.
- A Node-RED client(Subscribing client) running on the same RPI400 acts as an MQTT subscriber. Node-Red flow parses the incoming JSON messages and converts them into CSV format.
- A Node-RED client logs these messages in a CSV file in the local machine continously
- Later, the collected data is visualized using Python and Jupyter notebooks


## Key Info:

### General information about the experimental setup:

- Communication Protocols: MQTT for publishing node to broker, I2C from sensor to MCU
- Database System: CSV file Writing
- Data Visualization: Using Python and Jupyter notebooks
- Network backbone connection: TCP/IP via VLAN router between publisher, brokers and subscribers. See system architechture of the prototype 01 for more information

### Software Tools used: 
- Mosquitto MQTT broker
- Node-RED flows for MQTT client and data logging
- BMP280 and umqtt python libraray
- Thonny IDE for firmware in Micropython
- VS Code for writing jupyter notebooks

### Hardware Tools used:
- RPI picoW board as MQTT publisher
- RPI400 as MQTT server, MQTT subscribing client, database system for logged sensor data in CSV format
- BMP280 temperature pressure sensor
- Mi Powerbank 2i (10,000 mAh) to power sensor node
- Jumper wires and USB cables for connection

### Publishing sensor Node-01

![MS1_PH01_Pub_node01](https://github.com/Vishusharma296/Measurement_Systems/assets/73486657/69cfb9e0-d3d5-4f8f-9423-272c57b5eb66)

### Software Description

#### Firmware for publishing node:

Firmware for the publishing node written on RPI picoW performs the following functions:
- It connects to the WiFi connection (Home WLAN router) with known SSID and Password
- It establishes the MQTT connection with broker at the local IP address. (MQTT broker address is same as that of Raspberry Pi400 server)
- If the connection is successfull it reads the temperature and pressure data from BMP280 sensor (Here every 10 seconds)
- It publishes JSON message containing sensor data and other information (metadata) about the sensor node to a pre-specified MQTT topic
- Sensor data is sent every 10 seconds and it flashes an led for one second on successful publication of the message. 

#### Node-RED Flow

![MS1_PH1_P1_Node-red_flow_01](https://github.com/Vishusharma296/Measurement_Systems/assets/73486657/a8e0d1e2-3292-4739-8997-f6b91718b608)

This Node-RED flow, an MQTT subscribing client establishes connection with broker, converts the incoming JSON message to CSV format and logs the data on the local disk in CSV format.

#### Data analysis and results

**Run 01**
- Duration: 29.03.2024 - 03.04.2024
- Polling frequency for sensor: 10 sec
- Total number of samples: 43,416

  ![EXP_01_R01_Results](https://github.com/Vishusharma296/Measurement_Systems/assets/73486657/2919b6bc-8aaf-4a70-8f2e-862577499e1f)


**Run 02**
- Duration: 06.04.2024 - 10.04.2024
- Polling frequency for sensor: 10 sec
- Total number of samples: 37,436

![EXP_01_R02_Results](https://github.com/Vishusharma296/Measurement_Systems/assets/73486657/6c525492-3099-43eb-9f68-07c8f439af66)


**Description of the code in jupyter notebooks**
- CSV data was cleaned and imported into the notebook as a Pandas dataframe
- Dataframe was modified to include timestamp vectors for the collected sensor data
- Temperature and pressure data over the days was plotted as time series charts
- In another graph, pressure was changed from pascal to kPa and plotted on the same graph as time series

### Planned changes for next iterations of the experiment:

#### Firmware

- Change firmware by using concurrent programming: multi-threading and uasync io in Micropython.
- Now the sensor should poll the data every 10 seconds but connects to WiFi and sends the data say every 2-5 minutes and blinks LED.
- This data should be stored in the buffer memory. Old buffer should be cleared every 2-5 minutes even if node is not able to connect to the WiFi and MQTT Server
- Structure of the sent messages needs to be changed. It should include a unique device Id, sensor data, and a message counter
- Later efforts should be made to change the messages in JSON format to byte text (Hopefully base64/Hex).
- The purpose of doing this task is to make the message as short as possible. There should be option to convert back this byte text into plain human readable format.

#### Database and logging system

- Change the data logging system from CSV to time-series database using influx DB.
- Why?? Influx DB inserts the timestamp automatically. It reduces the amount of python code written to manipulate the pandas dataframes for inserting timestamp.


#### Data visualization

- Change the data visualization from jupyter notebooks to react charts/ graffana dashboards.











