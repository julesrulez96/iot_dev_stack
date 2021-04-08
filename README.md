# iot_dev_stack

docker-compose v3.0

containers:
  - Portainer (Container-Monitoring)
  - Mosquitto (MQTT-Broker)
  - Node-Red  (automation)
  - InfluxDB  (timeseries database)

volumes:

all volumes are mounted in the directory where the compose files is.
all containers have persistent data on the host.

mosquitto:

conf is set to= anonymous auth.
