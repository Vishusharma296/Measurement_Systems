April 2024

Start date: 24.03.2024

Tasks to achieve:

# Project 1: Wireless Sensor Data Measurement and Visualization System 

Project Goal: To build a measurement system with RP picoW board, RP400, BMP280 sensor and other hardware
  
  #### Features: 
  
  - Wirelessly transmit the sensor data to RP400 1) Using MQTT , 2) Using HTTP
  - Log the data in CSV files 1) - Using node red, 2) - Using python scripts
  - Display the data on a dashboard from 1) Node - Red, HTML based page
  - Presentation: Option to download images from specific timestamps, option to save data in CSV
  - Networking: Dashboard accesible to other non-admin user via HTTP/API/MQTT
  - Building a local data server on RP400
  
## Skills to learn
 
 - HTTP Protocol (python and micropython libraries)
 - MQTT Protocol
 - Working with HTML
 - Working with concurrent programming in Micropython
 - Node-red dashboard - creation and accesing it remotely
 - Github - Project documentation Markdown files, CLI commands, Branches, Security
 - Working with APIs in Python and Micropython
 - Designing a GUI in Python (TKinter)
 - SQL and database systems
 - Python Django framework
 - PostgreSQL
 - Time Series Database - InfluxDB
 - Graffana Dashboard
 
## Subproject 1.1) HTTP and MQTT in Micro Python 

### HTTP

- urequest 
- ujson

### MQTT

- Pub-sub model
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

## Subproject 1.3) HTML 

#### HTML

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

## subproject 1.4) Database system

- Local server and CSV files
- PostgreSQL
- Influx DB


## Subproject 1.5) Node-Red flows and creating dashboards

Tasks: Create a Node Red dashboard which displays the sensor data
- Node-red basics : [Node-red](https://nodered.org/)
- Node-red inbuilt dashboards
- Graffana Dashboards : [Grafana](https://grafana.com/docs/grafana/latest/)
- Flowfuse dashboards : [Flowfuse](https://flows.nodered.org/node/@flowfuse/node-red-dashboard)

## Subproject 1.7) Github 

- Github basics [Github](https://docs.github.com/en)
- Installing Git
- Configuring Git with email, SSH keys
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