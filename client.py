import paho.mqtt.client as mqtt
import time

# MQTT broker details
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "test/mqtt/example"

# Create an MQTT client instance using MQTTv311
client = mqtt.Client(protocol=mqtt.MQTTv311)

def publish_messages():
    try:
        # Connect to the broker
        client.connect(BROKER, PORT, keepalive=60)
        print(f"Connected to MQTT broker at {BROKER}:{PORT}")

        # Publish messages
        for i in range(1, 6):
            message = f"Message {i}"
            client.publish(TOPIC, message)
            print(f"Published: {message} to topic: {TOPIC}")
            time.sleep(1)

        # Disconnect from the broker
        client.disconnect()
        print("Disconnected from the MQTT broker")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    publish_messages()
