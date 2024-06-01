# Experiment 02, Prototype-01, Run 01 


## Changes, updates and upgrades: 

- Now the Measurement System logs the data into CSV as well as into the InfluxDB database.
- Now the Node-RED flow parses the incoming JSON messages and converts them into CSV format as well as into measurements for the InfluxDB.
- Earlier there was no provision for storing timestamp with the received data in CSV files. InfluxDB inserts an automatic Timestamp for each received data point.
- In firmware on the publishing sensor node, JSON message structure is changed to accomodate a unique device ID (DevUID).
- This DevUID: `DevEUI-Pub_pico-01` is same as the client ID of the MQTT publishing client.
- MQTT Topic structure is also improved by using the concept of logical hierarchy
- To Visiualize the sensor data in real time, a Grafana dashboard is created. This dashboard uses InfluxDB database as the source.
- Grafana visualization system was installed on RP400 to visualize the data in real time by using charts and the guages.

## Key information about the experimental setup::

### General 

- Network Communication Protocols: WiFi connection using a home router to connect sensor nodes and the RPI400 Server
- IoT Communication Protocols: MQTT for publishing sensor data from the node to the MQTT broker.
- Serial communication protocols: I2C from sensor BMP280 to the MCU
- Database System: CSV file writing and Influx DB
- Data Visualization: Using Grafana

### Software Tools used: 

- Mosquitto MQTT broker
- Node-RED flow for MQTT client connection with broker and data logging
- BMP280 and umqtt python libraray
- InfluxDB (v1.xxx)
- Grafana Dashboards

### Hardware tools and components used:

- RPI picoW board as MQTT publisher
- RPI400 as MQTT server, MQTT subscribing client, database system for logged sensor data in CSV format
- BMP280 temperature pressure sensor
- Mi Powerbank 2i (10,000 mAh) to power the sensor node.
- Jumper Wires and the microUSB cables
- Multimeter for debugging electronics

### Publishing sensor Node-01

![MS1_PH01_Pub_node01](https://github.com/Vishusharma296/Measurement_Systems/assets/73486657/69cfb9e0-d3d5-4f8f-9423-272c57b5eb66)


## Software Description

### Firmware for the publishing node (PicoW-01):

Firmware written for the publishing sensor node RPI picoW-01 has the following changes:
- Sensor data is sent every 30 seconds instead on every 10 seconds
- Now the JSON message contains DevUID, MQTT Topic, Message Counter and the usual sensor data.
- See the image below to see the structure of the JSON message.

![MS_PH01_P1_JSON_Message_V2](https://github.com/Vishusharma296/Measurement_Systems/assets/73486657/28b546f6-d843-489c-9ee2-23c825aabf4a)

### Node-RED Flow

![MS1_PH1_P1_Node-red_flow_02](https://github.com/Vishusharma296/Measurement_Systems/assets/73486657/ca30ae14-3351-422d-814d-f413199d3fd6)

The Node-RED flow used in this experiment has two sub flows. First subflow converts the JSON message into CSV format and then log this data into CSV file whenever a new message comes. Second sublow, extracts the temperature, pressure and message counter key-value pairs from the received JSON message. It then feeds these three extracted values in the InfluxDB database named as `SensorDB01` as sepearate measurements. The names of the measurements in the database follows the MQTT Topic heirarchy structure as shown in the figure below. For example title of the measurement related to the Message counter is `Sensor/BMP280-01/Message_counter`.

### InfluxDB Database

**_Configuring the Influx DB_**

After successfull intallation of InfluxDB (**InfluxDB version: 1.6xx **) on RPI400, InfluxDB needs to be configured. To configure the Influx DB for inserting the Time-Series data in the Database, following list of steps needed to be performed:

1. In the Linux terminal write: `influx`

Create a user with password using this command

`CREATE USER admin WITH PASSWORD '******' WITH ALL PRIVILEGES`

Now, exit the influxDB using `exit`

2. Make changes to the influx configuration file so that Influx DB can use authentication. Use the command below to access the configuration file of the influx DB.

`sudo nano /etc/influxdb/influxdb.conf`

3. Now navigate the influxdb configuration file. Find the HTTP section. Under http section in conf file write these lines:

```
auth-eanbled = true
pprof-enabled = true
pprof-auth-enabled = true
ping-auth-enabled = true
```

After making these changes, save and exit the conf file.

4. After exiting the conf file restart InfluxDB using the following command

`sudo systemctl restart influxdb`

5. Do the first login to the influxdb after making changes:

```
influx -username admin -password *****
```

6. Configure the InfluxDB in the Node-RED. After cofiguring the Node-RED flow for inserting the data in InfluxDB, Check if the sensor data is being looged in the desired database.

![MS1_PH01_P1_Influxdb](https://github.com/Vishusharma296/Measurement_Systems/assets/73486657/58702692-c523-43db-91b8-7b7e144b517a)


### Data analysis 

**Run 01**
- Duration: 01.05.2024 - 01.06.2024
- Polling frequency for sensor: 30 sec
- Total number of samples: 81,496

**Data Visualization: desscription of Grafana dashboard**

![MS_PH01_P1_Grafana_Dashboard_V1](https://github.com/Vishusharma296/Measurement_Systems/assets/73486657/d5c2e696-8133-4c95-a9f3-cffb35018f67)
![MS_PH01_P1_Grafana_Dashboard_V_Final](https://github.com/Vishusharma296/Measurement_Systems/assets/73486657/c09a531c-3129-4a61-a9cb-e774c4ef3e2c)

### Limitations of the current network architechture:

- Data is sent as without encryption as plain JSON text message to the MQTT broker
- Telemetry data stops when the connection to WLAN is interrupted for MQTT broker (RPI400) and the publisher node (RPI picoW-01)
- Quality of the firmware is poor. It uses too much energy. A fully charged 10,000 mAh power bank runs for about(... reading and ... days)
- LED was blinking even when the message was not published successfully



#### Prototype 01 Experiment 02 Tasks

- [x] Use Python Scripts to make connection to the Broker and subscribing to specific topics on which sensor node is publishing
- [x] Use Python Scripts to log the sensor data instead of/in addition to Node-RED. Convert the received JSON messages into CSV for logging.
- [x] Use Python Scripts to extract the sensor data from influxdb Database

### Planned changes for further Experiments and prototypes:


#### Possible improvement in firmware

- [ ] Make use of concurrent programming in micropython to improve the firmware.
- [ ] Try multi-threadingding and event driven programming with uasync io in Micropython.
- [ ] The size of the current pubilshed message is 129 Bytes. This is too large and need to be reduced in size

#### Data Visualization

- [ ] Learn about the Grafana Kiosk mode.
- [ ] Try to access the Grafana dashboard from a computer outside the local network.


#### Prototype 02 Experiment 01 Plan
- [ ] Create another node with LDR and internal temperature sensor
- [ ] Use Python scripts to log the Data into influx DB instead of/in addition to Node-RED
- [ ] Program the temperature pressure node picoW-01 with concurrent programming.
- [ ] PicoW-01 takes temperature and pressure reading every 10-30 seconds.
- [ ] Stores the readings on the local buffer on PicoW board
- [ ] Try to connect with WiFi every 5-10 minutes and flash the onboard LED for 1-2 seconds when connection is made.
- [ ] Try to connect and publish data to MQTT broker every 5-10 minutes and flash the onboard LED for 1-2 seconds when data is sent.

#### Prototype 02 Experiment 02 Plan

**Goals** 
: Program another picoW /ESP32 board to do the following tasks:
- [ ] Task1: Read ADC value from one of the pins 10-1000 times every second (Say antenna)
- [ ] Task2: Store the data into a vector
- [ ] Task3: Perform FFT for the incoming signal in real time.
- [ ] Task4: Show the fequency spectrum result in a the graph .












