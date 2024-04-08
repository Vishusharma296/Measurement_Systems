# Measurement Systems

Repository for wireless sensor data measurement system. 

## Measurement System Phase I


### Project Description

- Goal: Implementation of a standalone wireless sensor data measurement system. Measurement system will do FSA and HHT + HSA  and other time series analysis on raspberry Pi for processing real time sensor data (Updating graphs every 1-5 minutes). 

- For first phase of the measurement system, a temperature-pressure sensor (Bosch BMP280) with a rpi PicoW board will be used for wirelessly transmitting data to a server (using MQTT/HTTP).
- Initial data logging system will be based on CSV files, later logging systems will move from CSV to SQL/Time Series DB (Postgre SQL / Influx DB)
- Backend logic for FSA, HSA and other Time-series data analysis functions will be implemented in Python/JavaScript.
- Initial data manipulation and visualization will be done using Python and Jupyter Notebooks
- GUI implementation will be done on rpi for interaction with the measurement system (HTML5 or React based) in the later prototypes 2,3 ....
- Experiments with system architechture will be done by trying and changing communication protocols- (MQTT, HTTP Restful APIs), sensor data logging system (CSV, PostgreSQL, InfluxDB), Data Visualization System (Jupyter notebooks, PowerBI, HTML/React based GUI)

### Measurement System | Phase 1 | Prototype - 1 | System Architechture

![System Architechture](Project_library/Measurement_System_Phase_01/Images_Diagrams_Schematics/Images_Schematics/MS1_Phase1_P1_Sys_Architechture_V1.jpg)

#### Measurement System Phase II

- Implementation of the measurement system backend logic (With reduced functionalities) on $10 Microcontroller like ESP32 / RP PicoW in MicroPython/Arduino framework. (Edge Computing)
- Running the board on battery source and visualization of results via Mobile device using a Wifi Connection

#### Measurement System Phase III

- Building a custom PCB for sensor data acquisition, logging, computing algorithms, and visualization of sensor data using Mobile device with WiFi connection.
- Cyber Security -- Password protection, Hardware encryption, Sensor data encryption using ECC(Elliptic Curve Cryptography) / other suitable crytographic algorithms for IoT devices.
- Upload of telemetry data to the cloud account/remote server.

#### Hardware specifications for custom PCB:

**Prtotype Hardware Device I**

  - PCB with ESP32/RP2040 | (Wroom/Wrover module), ESP32 S/C/P series, PicoW board
  - UART-USB bridge | (CP2102)
  - Inbuilt accelerometer/IMU unit | (SPI/I2C)
  - Inbuilt temperature, humidity, pressure sensor | (Bosch BME280, BMP280 series) | (I2C)
  - Inbuilt LDR
  - Inbuilt Flash/EPROM storage + removable memory card support | (SPI)
  - Option for programming the chip (RP2040) via SWD and USB| (USB to UART bridge) | CP2102
  - Native USB support, USB OTG, WiFi and BLE capabilities | ESP32 S series chips
  - Power supply via USB and 3.3V cheap Li-ion battery.
  - Charging circuit for Li-ion battery
  - Programming via USB interface using MicroPython/Arduino framework/ Embedded C
  - Future boards to have LoRaWAN communication capabilities by adding the module/SOC | Semtech Sx1276 series chips


#### Functional software specifications and requirements

### Algorithm and analysis

- In depth study of the variants of EMD/HHT
- In depth study of time and memory complexity of HHT and its variants
- Implementation of advance variants of HHT/EMD/HSA algorithms in a) Python b) C++
- First sandbox to be in Jupyter Notebooks --> Python Modules
- Developing Python libraries for implementation of HHT and its variants  -- EEMD, MEMD, HHSA






