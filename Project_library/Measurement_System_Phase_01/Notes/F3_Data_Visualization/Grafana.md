# Grafana

## Introduction

Grafana is an interactive visualization web application that allows users to query, visualize, and analyze data from various sources. It is an open-source platform compatible with data sources like time-series databases (InfluxDB), PostgreSQL, MySQL, CSV files and Prometheus. Grafana can produce charts, graphs, and alerts for the web when connected to the above mentioned supported data sources. Grafana dashboards provide a customizable interface to visualize data in various formats like graphs, heatmaps, histograms, and geo maps. Grafana is widely used for monitoring and visualizing operational data, system metrics, IoT data, and business analytics.

## Important Concepts for Grafana Dashboards

- Data Source : CSV, InfluxDB, PostgreSQL, MySQL
- Panels : Visualization options such as Graph, Guage, Bar chart, heatmap
- Queries : To retrieve measurements from data source
- Templating: To reuse parts of dashboards, for dynamic data sources and query
- Alerts: based on threshold, notification by email..

## Grafana API

- Grafana can be accessed from default HTTP port 3000 in localhost | `http://your-grafana-server:3000`
- To change the default port| Grafana's configuration file: `grafana.ini`
- Uses RESTful endpoints that can be accessed via HTTP requests
- Authentication : API Keys, OAuth tokens
- API clients: Using HTTP client libraraies in Python, Javascript | CLI Curl from terminal

## Connecting Grafna with InfluxDB

## Grafana Documentation
- [Grafana Introduction](https://grafana.com/docs/grafana/latest/)
- [Grafana Installation Guide](https://grafana.com/docs/grafana/latest/setup-grafana/installation/debian/)
- [Grafana data Source - CSV](https://grafana.com/docs/plugins/marcusolsson-csv-datasource/latest/)
- [Grafana data Source - InfluxDB](https://grafana.com/docs/grafana/latest/datasources/influxdb/)
- [Grafana data Source - Postgre SQL](https://grafana.com/docs/grafana/latest/datasources/postgres/).
