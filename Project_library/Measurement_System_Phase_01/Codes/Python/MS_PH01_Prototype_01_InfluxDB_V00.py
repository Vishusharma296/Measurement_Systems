'''
This Python Script performs the following Tasks:

    1. Runs on PC/RP400
    2. Connects with an InfluxDB Database with authentication
    3. Run queries on database to retrieve 3 measurements
    4. Extracts the data points and merge them into a single data
    5. Creates a CSV file with headers and write these extracted data points into CSV file

'''



import csv
from influxdb import InfluxDBClient

# Replace with your actual InfluxDB connection details
host = 'localhost'
port = 8086
username = '*****'
password = '*****'
database = 'SensorDB01'

# Connect to the InfluxDB client
client = InfluxDBClient(host=host, port=port, username=username, password=password, database=database)

# Defining the queries to retrieve data from each measurement

query_message_counter = f'SELECT "value" AS "Message_counter" FROM "Sensor/BMP280-01/Message_counter"'
query_temperature = f'SELECT "value" AS "Temperature" FROM "Sensor/BMP280-01/Temperature"'
query_pressure = f'SELECT "value" AS "Pressure" FROM "Sensor/BMP280-01/Pressure"'

# Querying the database

results_message_counter = client.query(query_message_counter)
results_temperature = client.query(query_temperature)
results_pressure = client.query(query_pressure)

# Extracting the data points

points_message_counter = list(results_message_counter.get_points())
points_temperature = list(results_temperature.get_points())
points_pressure = list(results_pressure.get_points())

# Merging the data based on timestamps

merged_data = []
for i in range(len(points_message_counter)):
    timestamp = points_message_counter[i]['time']
    message_counter = points_message_counter[i]['Message_counter']
    temperature = points_temperature[i]['Temperature'] if i < len(points_temperature) else None
    pressure = points_pressure[i]['Pressure'] if i < len(points_pressure) else None
    merged_data.append([message_counter, temperature, pressure, timestamp])

# Preparing data for CSV

csv_headers = ["Message_counter", "Temperature", "Pressure", "Timestamp"]
csv_file_name = "SD_Test-03_InfluxDB_extracted.csv"
csv_file_path = "/home/vishu_RP400/RP400_Sandbox_Git/Measurement system/Sensor Data/SD_Test-03_InfluxDB_extracted.csv"

# Writing  data to CSV

with open(csv_file_path, mode='a', newline='') as file:
    writer = csv.writer(file)
    
   # Checking if file is empty and writing headers if needed
    if file.tell() == 0:
        writer.writerow(csv_headers)

    # Writing the data points
    for row in merged_data:
        writer.writerow(row)


print(f"Data successfully written to {csv_file_name}")

# Close the client
client.close()
