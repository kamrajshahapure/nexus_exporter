# nexus_exporter
This is an exporter for pulling metrics from SonaType Nexus for Prometheus monitoring

# Tested On
1. Python 3
2. Nexus 3.15.2

# Metrics Supported as of April 2019 (Other metrics will be added soon)
1. Number of repositories in Nexus
2. Number of logical CPUs
3. Free Memory
4. Total Memory
5. Max Memory
6. Number of 1XX, 2XX, 3XX, 4XX, 5XX requests

Running it is as simple as running any python script 

# Plan
1. Dockerizing the exporter
2. Creating a grafana dashboard
3. Adding more relevant metrics
