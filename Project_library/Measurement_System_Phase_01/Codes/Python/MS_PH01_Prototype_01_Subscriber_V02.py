'''

This Program performs the following Tasks:
    
    0. Suitable for running on PC/ Server
    1. Connects with an MQTT Broker
    2. Handles the connection to a locally hosted MQTT Broker
    3. Subscribe to the MQTT Topic and decodes the JSON message
    4. On receiving message, it prints the recieved message
    5. It extracts the measurement values from the JSON message
    6. It converts these extracted values from JSON to CSV with an extra Time-Stamp column
    7. Note this Time is UTC and Berlin is UTC + 2 CEST. So time stamp is 2 hours behind
    8. It logs each received message in the CSV file
    
'''

# External Modules and libraries 

import paho.mqtt.client as mqtt
import json
import csv
from datetime import datetime

# MQTT Connection details

MQTT_BROKER = "192.168.0.103"   # MQTT Broker address
BROKER_PORT = 1883
CLIENT_ID = "DevEUI-Pub_pico-01"
MQTT_TOPIC_01 = "Sensor/BMP280-01/Temperature"
MQTT_TOPIC_02 = "Sensor/BMP280-01/Pressure"
MQTT_TOPIC_M = "Sensor/BMP280-01/#"
keep_alive = 60


# CSV file path and headers
csv_file_name = "SD_Test-05_CSVFile.csv"
csv_file_path = "/home/vishu_RP400/RP400_Sandbox_Git/Measurement system/Sensor Data/SD_Test-05_CSVFile.csv"
csv_headers = ["MQTT_Topic","Message_counter","Temperature_C","Pressure_P","Time_Stamp"]

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

        # Extract values from the message
        MQTT_Topic = message_json["MQTT_Topic"]
        Message_counter = message_json["Message_counter"]
        Temperature_C = message_json["Temperature_C"]
        Pressure_P = message_json["Pressure_P"]

        # Get current timestamp in ISO-8601 format
        Timestamp = datetime.utcnow().isoformat()

        # Print the message to the console
        print("Received message:")
        print(json.dumps(message_json, indent=4))  # Pretty-print the JSON message

        # Writing data to CSV file
        write_to_csv(MQTT_Topic,Message_counter,Temperature_C,Pressure_P,Timestamp)

    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
    except Exception as e:
        print("An error occurred:", e)

def write_to_csv(MQTT_Topic,Message_counter,Temperature_C,Pressure_P,Timestamp):
    
    # Preparing data to write to CSV file
    data = [MQTT_Topic,Message_counter,Temperature_C,Pressure_P,Timestamp]

    # Writing data to CSV file
    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Checking if file is empty and writing headers if needed
        if file.tell() == 0:
            writer.writerow(csv_headers)
        writer.writerow(data)

    print("Data written to CSV file successfully")

# Create an MQTT client instance
MQTT_client = mqtt.Client()

# Set callback functions
MQTT_client.on_connect = on_connect
MQTT_client.on_message = on_message

# Connect to the MQTT broker
MQTT_client.connect(MQTT_BROKER, BROKER_PORT, keep_alive)

# Loop to maintain connection and continue listening for messages
MQTT_client.loop_forever()
