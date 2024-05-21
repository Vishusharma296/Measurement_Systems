"""
Micro Python Firmware for Raspberry Pi PicoW
For Node 2 with LDR sensor and LEDs

### Program Tasks:

1) To read the analog signal from adc capable pin
2) To print the value of analog signal from adc pin every 1-5 seconds
3) At ADC pin 26 an LDR input is connected with its other leg connected to 5.1K Ohm resistor
4) If brightness percent is less than set thresholds it controls the external LED
5) MCU prints the JSON message containing Raw adc value, brightness percentage, message counter
6) It establishes a WiFi and an MQTT connection with the Broker
7) It publishes the sensor data to the broker


--- Firmware information -----

Current Version: MS1_EXP03_main_V2.01

First version: 14.05.2024
Last update: 21.05.2024

----- Changes and improvements from the last version -----

  1. Use of functions to read LDR and control LEDs
  2. Use of error handling in the functions
  3. Code for WiFi Connection
  4. Code for MQTT Connection
  5. Code to publish JSON message to the MQTT server

"""

# Libraries and modules

from machine import I2C, Pin
import time
import network
import utime
import ujson
from umqtt import MQTTClient

# System Parameters and pin assignment

# WiFi Connection Details

SSID = "VISHU_WIFI"
PASSWORD = "123456789"

# MQTT Connection Details

MQTT_BROKER = "192.168.0.103"
BROKER_PORT = 1883
CLIENT_ID = "DevEUI-Pub_pico-02"
MQTT_TOPIC = "Sensor/LDR-01"

Device_UID = CLIENT_ID
Polling_interval = 2                          # Sensor Polling Frequency
count = 0                                     # Message counter
ADC16_PC = 0.0015                             # 100/65535 = 0.001525902  
Brightness_percent = 0.0                      # Brightness level

# LDR Threshold variables

LDR_threshold1 = 2                            # For completely dark room
LDR_threshold2 = 16                           # Low light/ Table lamp on

# Pin Assignment

GPIO_ADC0 = 26                                # Pin 26 is ADC
LED_onboard = machine.Pin("LED", Pin.OUT)     # Onboard LED
LED_ext = machine.Pin(15, machine.Pin.OUT)    # External LED

# Setting up ADC on Pin 26
adc_0 = machine.ADC(machine.Pin(GPIO_ADC0))   # Pin 26

# Initial startup
time.sleep(3)

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
    
    
# Function to publish message to MQTT broker

def publish_message(client, topic, message):
    try:
        client.publish(topic, ujson.dumps(message))
        print("Message published to", topic)
    except Exception as e:
        print("Failed to publish message:", e)
    
# Function to read LDR
"""Reads the analog value from the LDR and calculates brightness percentage."""

def read_LDR(adc_0):
    
    try:
        ADC0_val = adc_0.read_u16()
        Brightness_percent = ADC0_val * ADC16_PC
        print(Brightness_percent, ADC0_val, sep=',')
        return  ADC0_val,Brightness_percent
    except Exception as e:
        print(f"Error reading ADC value: {e}")
        return None
    
# Function to control LEDs
"""Controls the LEDs based on brightness and threshold values."""

def control_LEDs(brightness, threshold1, threshold2):
    
    if brightness is not None:
        if brightness < threshold1:
            LED_ext.on()
            LED_onboard.off()
        elif brightness < threshold2:
            LED_ext.off()
            LED_onboard.on()
        else:
            LED_ext.off()
            LED_onboard.off()
    else:
        LED_ext.off()
        LED_onboard.off()
        
        
# -------Main Loop---------

if connect_to_wifi(SSID, PASSWORD):
    client = connect_to_mqtt()
    if client:
        while True:
            LDR_adc_value, Brightness_percent = read_LDR(adc_0)
            control_LEDs(Brightness_percent, LDR_threshold1, LDR_threshold2)
            
            # Sensor Data JSON Message
            
            Sensor_data = {
                "DevUID": Device_UID,
                "MQTT_Topic": MQTT_TOPIC,
                "Message_counter": count,
                "LDR_Brightness": Brightness_percent,
                "LDR_adc_value": LDR_adc_value
            }
            
            print(Sensor_data)
            publish_message(client, MQTT_TOPIC, Sensor_data)
            count = count + 1   # Updating counter
            utime.sleep(Polling_interval) 
            
    else:
        print("MQTT client not available.")
else:
    print("WiFi connection failed.")



