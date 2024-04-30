'''
This script connects to Wifi with input credentials
Establish the MQTT connection with broker
If the connection is successfull it publishes JSON messages and flashes an led


----------Changes from the last version-----------------

Changed the MQTT Topic structure,
Changed the sensor polling frequency from 10 seconds to 30 seconds
Introduced the concept of a Unique Device ID for each sensor node
Now the published json message sends device ID, MQTT topic, message counter and sensor readings

Version: MS1_EXP01_main_V1.02.py
Last Update: 29.04.2024
'''

from machine import I2C, Pin
from time import sleep
import network
import utime
import ujson
from umqtt import MQTTClient
from bmp280 import *

# WiFi Connection Details

SSID = "VISHU_WIFI"
PASSWORD = "123456789"

# MQTT Connection Details

MQTT_BROKER = "192.168.0.103"
BROKER_PORT = 1883
CLIENT_ID = "DevEUI-Pub_pico-01"
MQTT_TOPIC_01 = "Sensor/BMP280-01/Temperature"
MQTT_TOPIC_02 = "Sensor/BMP280-01/Pressure"

# General variable declaraion
Polling_interval = 10
label = 1                  # label for CSV headers
count = 0                  # Message counter
Device_UID = CLIENT_ID     # Unique device ID same as MQTT client ID here

# Pin assignment 

led = Pin("LED", Pin.OUT)
Pin_SDA = Pin(14)
Pin_SCL = Pin(15)

# Creating i2c object

i2c_bus = I2C(1, scl = Pin_SCL, sda = Pin_SDA, freq = 40000)
scan_result = I2C.scan(i2c_bus)
print(scan_result)

# BMP object Settings
bmp_object = BMP280(i2c_bus, addr = 0x76, use_case = BMP280_CASE_INDOOR)

# Function to connect with the WiFi

def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        pass
    print("Connected to WiFi")
    
# Function to connect with the MQTT broker

def connect_to_mqtt():
    client = MQTTClient(CLIENT_ID, MQTT_BROKER)
    client.connect()
    print("Connected to MQTT broker")
    return client

# Function to publish message

def publish_message(client, message):
    client.publish("Sensor/BMP280-01", ujson.dumps(message))
    print("Message published")

# Main loop

connect_to_wifi(SSID, PASSWORD)
client = connect_to_mqtt()

while True:
    
    temperature = bmp_object.temperature
    pressure = bmp_object.pressure
        
    Sensor_data = {

        "DevUID"   : Device_UID,
        "MQTT_Topic" : "Sensor/BMP280-01",
        "Message_counter": count,
        "Temperature_C": temperature,
        "Pressure_P" : pressure
        }
    
    publish_message(client, Sensor_data)
    print('Sensor Data:', Sensor_data)
    count = count + 1
    led.value(1)
    utime.sleep(1)
    led.value(0)
    utime.sleep(29)  # Send message every 30 seconds