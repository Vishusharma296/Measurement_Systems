# Influx DB

[Official Influx DB documentation](https://docs.influxdata.com/influxdb/v2/)
[InfluxDB installation tutorial](https://randomnerdtutorials.com/install-influxdb-2-raspberry-pi/)

## Basics of InfluxDB and Time-Series Database

Time series data is a sequence of data points indexed in time order. InfluxDB is an open-source time series database designed to handle high write and query loads for time-stamped data.
It is optimized for fast, high-availability storage and retrieval of time series data in fields such as industrial sensor data monitoring, server performance metrics, sensor data, real-time analytics for finance etc.

### Key features of InfluxDB

- Time Series data handling (automatic insertion of timestamp)
- Schemaless design
- Retenetion policies for data
- Continous Queries
- High availability and scalability with cluster
- Integration with other software platforms like Node-red, Grafana, Telegraf, Chronograf, Kapacitor

### Key Concepts for InfluxDB

#### Data organization in Influx DB

- Bucket: Named location where time series data is stored. A bucket can contain multiple measurements.
- Measurement: Logical grouping for time series data. All points in a given measurement should have the same tags. A measurement contains multiple tags and fields.
- Fields: Key-value pairs with values that change over time–for example: temperature, pressure, stock price, etc.
- Tags: Key-value pairs with values that differ, but do not change often.
- Tags are meant for storing metadata for each point–for example, something to identify the source of the data like host, location, station, etc.
- Timestamp: Timestamp associated with the data. When stored on disk and queried, all data is ordered by time.

## Learning Plan for InfluxDB

### 1. Foundation of Time Series Data and InfluxDB Basics

- **Objective**: Understand the fundamentals of time series data and InfluxDB's architecture so that it can be implemented for the Measurement system database.

  - Reading time series database, its need and comparison with traditional SQL databases
  - Learn about InfluxDB's features, data model, and use cases.
  - Key components of InfluxDB: Databases, measurements, tags, fields.

### 2. Installation and Setup

- **Objective**: Installing InfluxDB and setting up a local environment on RP400 for practice.

  - Install InfluxDB Raspberry Pi
  - Configure and start InfluxDB service (automatic start).
  - Access the InfluxDB CLI, InfluxDB UI (localhost:8086) and later InfluxDB HTTP API

### 3. Basic Operations and Queries

- **Objective**: Learn to perform basic operations and queries in InfluxDB.

  - Use InfluxDB CLI to create databases, measurements, and retention policies.
  - Insert data into InfluxDB using Node-red.
  - Retrieve and query 

### 4. Data Management

- **Objective**: Understand how to manage data effectively in InfluxDB.

  - Data retention policies and continuous queries.
  - Data downsampling and aggregation.
  - Best practices for data organization
    
### 5. Monitoring and Alerting

- **Objective**: Using InfluxDB for real-time monitoring of sensor data.
  
  - Exploring visualization options using Grafana.

### 6. Advanced Topics

  - InfluxDB clustering and high availability.
  - Data backup and restore strategies.
  - InfluxDB’s integration with other tools and platforms (e.g., Node-red, Grafana, Prometheus).
  - Kapacitor for stream processing and anomaly detection.

### Important linux commands for installation of InfluxDB

| Command                                           | Description                                                                   |
|---------------------------------------------------|-------------------------------------------------------------------------------|
| `sudo apt install curl apt-transport-https`       | Install necessary packages (`curl` and `apt-transport-https`) for InfluxDB installation.|
| `curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -` | Download and add the InfluxDB repository key to the system's list of trusted keys.|
| `sudo apt install influxdb`                       | Install InfluxDB package.                                                      |
| `sudo systemctl start influxdb`                   | Start the InfluxDB service.                                                    |
| `sudo systemctl enable influxdb`                  | Enable InfluxDB service to start on boot.                                      |
| `influx`                                          | Launch the InfluxDB command line interface (CLI).                              |
| `CREATE DATABASE mydatabase`                      | Create a new database named `mydatabase` in InfluxDB.                          |
| `SHOW DATABASES`                                  | Show a list of all databases in InfluxDB.                                      |
| `exit`                                            | Exit the InfluxDB CLI.                                                         |

### Important InfluxDB commands and querries

| Command/Query                                      | Description                                                                   |
|-----------------------------------------------------|-------------------------------------------------------------------------------|
| `CREATE DATABASE <database_name>`                   | Create a new database in InfluxDB.                                            |
| `SHOW DATABASES`                                   | Show a list of all databases in InfluxDB.                                      |
| `USE <database_name>`                               | Switch to a specific database for subsequent queries.                          |
| `DROP DATABASE <database_name>`                     | Delete a database and all associated data from InfluxDB.                       |
| `SHOW MEASUREMENTS`                                 | List all measurements (tables) in the current database context.                |
| `SHOW FIELD KEYS FROM <measurement_name>`            | Display all field keys (columns) for a specific measurement.                   |
| `SELECT * FROM <measurement_name>`                  | Retrieve all data points from a specific measurement.                          |
| `SELECT <field_name(s)> FROM <measurement_name>`     | Retrieve specific field(s) from a measurement.                                 |
| `SELECT * FROM <measurement_name> WHERE <condition>` | Filter data based on specified conditions (e.g., time range, tag values).      |
| `SELECT COUNT(<field_name>) FROM <measurement_name>` | Calculate the count of non-null values for a field in a measurement.           |
| `SHOW RETENTION POLICIES ON <database_name>`         | Display retention policies defined for a database.                             |
| `CREATE RETENTION POLICY <policy_name> ON <database_name> DURATION <duration> REPLICATION <n>` | Create a new retention policy for a database. |
| `DROP RETENTION POLICY <policy_name> ON <database_name>` | Delete a retention policy from a database.                               |
| `SHOW TAG KEYS FROM <measurement_name>`              | Display all tag keys (index keys) for a specific measurement.                  |
| `SHOW TAG VALUES FROM <measurement_name> WITH KEY = <tag_key>` | Display unique tag values for a specific tag key in a measurement.     |
| `DELETE FROM <measurement_name> WHERE <condition>`   | Delete data points based on specified conditions (e.g., time range).          |
| `SHOW CONTINUOUS QUERIES`                           | List all continuous queries configured in InfluxDB.                            |
| `CREATE CONTINUOUS QUERY <cq_name> ON <database_name> BEGIN <query_definition> END` | Create a continuous query to aggregate and downsample data. |
| `DROP CONTINUOUS QUERY <cq_name> ON <database_name>` | Delete a continuous query from a database.                                      |
| `SHOW DIAGNOSTICS`                                  | Display diagnostic information about the InfluxDB instance.                    |
| `SHOW STATS`                                        | Show statistics and performance metrics for InfluxDB.                          |



### Learning Resources

[Telegraf Documentation](https://docs.influxdata.com/telegraf/v1/)
[Influx DB Documentation](https://docs.influxdata.com/influxdb/v2/)


