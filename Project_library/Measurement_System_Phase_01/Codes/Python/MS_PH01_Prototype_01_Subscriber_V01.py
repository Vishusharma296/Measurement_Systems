'''

This Program performs the following Tasks:
    
    0. Suitable for running on PC/ Server
    1. Connects with an MQTT Broker
    2. Handles the connection to a locally hosted MQTT Broker
    3. Subscribe to the MQTT Topic and decodes the JSON message
    4. On receiving message, it prints the recieved message
    
'''

import paho.mqtt.client as mqtt
import json

# MQTT Connection details

MQTT_BROKER = "192.168.0.103"   # MQTT Broker address
BROKER_PORT = 1883
CLIENT_ID = "DevEUI-Pub_pico-01"
MQTT_TOPIC_01 = "Sensor/BMP280-01/Temperature"
MQTT_TOPIC_02 = "Sensor/BMP280-01/Pressure"
MQTT_TOPIC_M = "Sensor/BMP280-01/#"
keep_alive = 60


# Callback function when connecting to the broker

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribe to the topic when connected
    client.subscribe(MQTT_TOPIC_M)

# Callback function when receiving a message

def on_message(client, userdata, msg):
    # Decode the incoming message payload as JSON
    try:
        message_json = json.loads(msg.payload.decode())
        # Print the message to the terminal
        print("Received message:")
        print(json.dumps(message_json, indent=4))  # Pretty-print the JSON message
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
    except Exception as e:
        print("An error occurred:", e)

# Create an MQTT client instance
MQTT_client = mqtt.Client()

# Set callback functions
MQTT_client.on_connect = on_connect
MQTT_client.on_message = on_message

# Connect to the MQTT broker
MQTT_client.connect(MQTT_BROKER, BROKER_PORT, keep_alive)

# Loop to maintain connection and continue listening for messages
MQTT_client.loop_forever()
