import paho.mqtt.client as mqtt
from config import settings
# Define the MQTT broker details
broker = settings.MQTT_BROKER_HOST
port = 1883
username = settings.MQTT_BROKER_USERNAME
password = settings.MQTT_BROKER_PASSWORD

topics = [
    ("shellyplug/relay/0/power", 0), 
    ("shellyhygrometer/temperature", 0), 
    ("shellyhygrometer/humidity", 0)
    ]

# Define callback functions
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribe to the topics
    for topic in topics:
        client.subscribe(topic)

def on_message(client, userdata, msg):
    print(f"{msg.topic} {msg.payload.decode()}")

# Create an MQTT client instance
client = mqtt.Client()

# Set username and password
client.username_pw_set(username, password)

# Assign callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker, port, 60)

# Start the loop to process received messages
client.loop_forever()
