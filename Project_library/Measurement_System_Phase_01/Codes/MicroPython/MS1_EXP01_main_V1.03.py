'''
This script connects to Wifi with input credentials
Establish the MQTT connection with broker
If the connection is successfull,
it publishes JSON messages every 30 seconds
and flashes an led for 1 second


----------Changes from the last version-----------------

Issues with last version of the firmware:

- Redundant import of time statement.
- Redundant Message Publishing
- Redundant Import of utime
- Lack of error handling and robustness in WiFi and MQTT
- Inefficient WiFi Connection Loop: Code for WiFi was blocking
- Hardcoded WiFi and MQTT Details
- MQTT Topic Hardcoded in publish_message Function
- I2C Frequency too High
- Polling Interval Constant Not Updated


Version: MS1_EXP01_main_V1.03.py
Last Update: 17.05.2024
'''

from machine import I2C, Pin
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
MQTT_TOPIC = "Sensor/BMP280-01"

# General variable declaration
Polling_interval = 30  # Changed polling interval to 30 seconds
count = 0
Device_UID = CLIENT_ID

# Pin assignment
led = Pin("LED", Pin.OUT)  # Correct pin assignment for Pico W
Pin_SDA = Pin(14)
Pin_SCL = Pin(15)

# Creating I2C object
i2c_bus = I2C(1, scl=Pin_SCL, sda=Pin_SDA, freq=100000)  # Use standard I2C frequency
scan_result = i2c_bus.scan()
print("I2C scan result:", scan_result)

# BMP object settings
bmp_object = BMP280(i2c_bus, addr=0x76, use_case=BMP280_CASE_INDOOR)

# Function to connect with the WiFi
def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    timeout = 10  # 10 seconds timeout
    while not wlan.isconnected() and timeout > 0:
        print("Connecting to WiFi...")
        utime.sleep(1)
        timeout -= 1
    if wlan.isconnected():
        print("Connected to WiFi")
        print("Network config:", wlan.ifconfig())
    else:
        print("Failed to connect to WiFi")
        return False
    return True

# Function to connect with the MQTT broker
def connect_to_mqtt():
    try:
        client = MQTTClient(CLIENT_ID, MQTT_BROKER, BROKER_PORT)
        client.connect()
        print("Connected to MQTT broker")
        return client
    except Exception as e:
        print("Failed to connect to MQTT broker:", e)
        return None

# Function to publish message
def publish_message(client, topic, message):
    try:
        client.publish(topic, ujson.dumps(message))
        print("Message published to", topic)
    except Exception as e:
        print("Failed to publish message:", e)

# Main loop
if connect_to_wifi(SSID, PASSWORD):
    client = connect_to_mqtt()
    if client:
        while True:
            temperature = bmp_object.temperature
            pressure = bmp_object.pressure
            
            Sensor_data = {
                "DevUID": Device_UID,
                "MQTT_Topic": MQTT_TOPIC,
                "Message_counter": count,
                "Temperature_C": temperature,
                "Pressure_P": pressure
            }
            
            publish_message(client, MQTT_TOPIC, Sensor_data)
            
            print('Sensor Data:', Sensor_data)
            count += 1
            led.value(1)
            utime.sleep(1)
            led.value(0)
            utime.sleep(Polling_interval - 1)  # Ensure the total delay is 30 seconds
    else:
        print("MQTT client not available.")
else:
    print("WiFi connection failed.")

