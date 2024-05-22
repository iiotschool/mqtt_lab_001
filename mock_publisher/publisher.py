import paho.mqtt.client as mqtt
import time
import random
from config import settings

# Define the MQTT broker details
broker = settings.MQTT_BROKER_HOST
port = 1883
username = settings.MQTT_BROKER_USERNAME
password = settings.MQTT_BROKER_PASSWORD
topic_power = "shellyplug/relay/0/power"
topic_temp = "shellyhygrometer/temperature"
topic_humidity = "shellyhygrometer/humidity"

# Create an MQTT client instance
client = mqtt.Client()

# Set username and password
client.username_pw_set(username, password)

# Connect to the MQTT broker
client.connect(broker, port, 60)

def publish_mock_data():
    while True:
        # Generate mock data
        power = random.uniform(10.0, 100.0)  # Power in watts
        temperature = random.uniform(15.0, 30.0)  # Temperature in Celsius
        humidity = random.uniform(30.0, 70.0)  # Humidity in percentage

        # Publish the mock data to the MQTT topics
        client.publish(topic_power, power)
        client.publish(topic_temp, temperature)
        client.publish(topic_humidity, humidity)

        print(f"Published: Power={power}, Temperature={temperature}, Humidity={humidity}")

        # Wait for 2 seconds before publishing the next set of mock data
        time.sleep(.5)

if __name__ == "__main__":
    publish_mock_data()
