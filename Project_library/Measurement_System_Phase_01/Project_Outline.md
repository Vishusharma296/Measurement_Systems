April 2024

Start date: 24.03.2024

Tasks to achieve:

# Project 1: Wireless Sensor Data Measurement and Visualization System 

Project Goal for phase 1: To build a sensor data acquisition, measurement and visualization system with RP picoW board, RP400, BMP280 sensor and other hardware
  
  #### Features: 
  
  - Wirelessly transmit the sensor data to RP400 1) Using MQTT , 2) Using HTTP
  - Log the data in CSV files 1) - Using node red, 2) - Using python scripts
  - data Visualization: Display the data on a dashboard from 1) Node-red dashboards, Grafana dashboards, HTML based pages
  - Presentation: Option to download images from specific timestamps, option to save data in CSV
  - Networking: Dashboard should be accesible to other non-admin user via HTTP/APIs/MQTT
  - Building a local data server on RP400 using CSV files, TS DB, SQL DB
  
## Required Skills for Project
 
 - HTTP Protocol (python and micropython libraries)
 - MQTT Protocol
 - Working with HTML
 - Working with concurrent programming in Micropython
 - ~~Node-red dashboard - creation and accesing it remotely~~
 - Github - Project documentation Markdown files, CLI commands, Branches, Security
 - Working with APIs in Python and Micropython
 - ~~Designing a GUI in Python (TKinter)~~
 - SQL and database systems
 - ~~Python Django framework~~
 - Time Series Database - InfluxDB
 - PostgreSQL
 - Graffana Dashboard
 - React.js for data visulaization and charts
 
## Subproject 1.1) Communication Protocols: HTTP and MQTT in Python and MicroPython 

### HTTP

- HTTP requests - GET, POST, UPDATE, DELETE
- urequest 
- ujson

### MQTT

- Pub-sub model
- Broker-client relation
- MQTT control packets
- QoS (Quality of Service)
- umqtt
- Mosquito broker
- Paho Client
- Publisher scripts
- Subscriber scripts
 
## Sub Project 1.2) Concurrent programming in Micro Python

- Event driven programming
- Multi-threading
- Cooperative vs preemptive multithreading
- Coroutines, Lightweight threads
- Deadlocks
- Race conditions
- Asynchronous functions
- Locks
- Semaphores 
- Scheduling
- Concurrency Primitives
- Asynchronous I/O
- Queues
- Event loops, Event flags, Event Handlers, Event Emitters
- Awaitable Objects
- Shared resources
- Callbacks
- Design of concurrency model

## Subproject 1.3) Data visualisation using: Jupyter Notebooks, HTML pages, Node-Red dashboards, Grafana dashboards, React.js charts 

### Jupyter Notebooks

- Markdown
- Python libraries and modules
- Handling relational data from sensors with NumPy, SciPy, Pandas dataframes and Polars
- Data visualization using Matplotlib, Seaborn and Plotly express  

### HTML

- HTML - opening and closing tags 
- Index     
- Title     
- Head     
- Body     
- Headers tags h1, h2, ...h6 
- Breaks  
- Paragraphs 
- Horizontal rule 
- Comments
- Lists: Ordered and unordered lists
- Hyperlinks
- Inserting images, audio, video
- Buttons
- Forms
- Tables
- Metadata
- HTML APIs - Geolocation, local storage, canvas
- Responsive Webdesign
- Web accesibility and Aria roles

### Grafana Dashboards

See detailed notes on Grafana in Data Visualization

### React Framework

## Subproject 1.4) Sensor Data Logging System - Node-red flow based CSV files, Time-Series Databse, SQL Database 

### Storing data using Node-Red flows

- Local MQTT server and Client in Node-red/Python scripts
- Data logging in CSV files by using Node-red flows
- Node-red basics : [Node-red](https://nodered.org/)
- Node-red inbuilt dashboards
- Graffana Dashboards : [Grafana](https://grafana.com/docs/grafana/latest/)
- Flowfuse Dashboards : [Flowfuse](https://flows.nodered.org/node/@flowfuse/node-red-dashboard)

### Influx DB

See detailed notes on Influx DB in Database Systems

### PostgreSQL

## Subproject 1.7) Github 

- Github basics [Github](https://docs.github.com/en)
- Installing Git
- Configuring Git with email, HTTP/SSH keys on local machine
- Documentation via Markdown, Project management
- Version control via branching
- Collaboration
- Issue tracking
- Continous Integration and development CI/CD
- Branches, Issues, Milestones, pull requests, code reviews

## Subproject 1.8) Containerization with Docker 
- Need for Containerization
- Introduction to docker: [Docker]( https://docs.docker.com/)
- Installation on linux machine
- Docker Conatainer basics
- Kubernetes Basics
- Creating docker images, dockerfile
- Docker CLI
- Container Orchestraion, Docker Compose
- Networking - Connecting Containers
- Docker Hub
- Docker Registry
- Docker Security
- Docker Swarm for scaling
- Docker SDKs and APIs
- Docker Multistage builds
