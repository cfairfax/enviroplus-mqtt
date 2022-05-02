import json

def publish_discovery_topics(client, prefix):
    sensors = {
        "particulate/1_0": {"device_class": "pm1", "unit_of_measurement": "µg/m³"},
        "particulate/2_5": {"device_class": "pm25", "unit_of_measurement": "µg/m³"},
        "particulate/10_0": {"device_class": "pm10", "unit_of_measurement": "µg/m³"},
        "proximity": {"device_class": "proximity", "unit_of_measurement": "proximity"},
        "lux": {"device_class": "illuminance", "unit_of_measurement": "lux"},
        "temperature": {"device_class": "temperature", "unit_of_measurement": "°C"},
        "pressure": {"device_class": "pressure", "unit_of_measurement": "hPa"},
        "humidity": {"device_class": "humidity", "unit_of_measurement": "%"},
        "gas/oxidising": {"device_class": "voltage", "unit_of_measurement": "V"},
        "gas/reducing": {"device_class": "voltage", "unit_of_measurement": "V"},
        "gas/nh3" : {"device_class": "voltage", "unit_of_measurement": "V"}
        }
    for name, payload in sensors.items():
         print(name)
         discovery_topic = "homeassistant/sensor/" + name + "/config"
         topic = prefix + "/" + name
         discovery_payload = {"name": "enviro_" + name, "state_topic": topic}
         discovery_payload.update(payload)
         client.publish(discovery_topic, payload=json.dumps(discovery_payload), retain=True)



