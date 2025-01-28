import paho.mqtt.client as mqtt

# MQTT broker details
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "test/mqtt/example"

# Callback when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker!")
        client.subscribe(TOPIC)  # Subscribe to the topic
        print(f"Subscribed to topic: {TOPIC}")
    else:
        print(f"Connection failed with code {rc}")

# Callback when a message is received
def on_message(client, userdata, msg):
    print(f"Received message: '{msg.payload.decode()}' on topic: '{msg.topic}'")

# Create an MQTT client instance using MQTTv311
client = mqtt.Client(protocol=mqtt.MQTTv311)

# Assign callback functions
client.on_connect = on_connect
client.on_message = on_message

def start_subscriber():
    try:
        # Connect to the broker
        client.connect(BROKER, PORT, keepalive=60)
        print(f"Connecting to MQTT broker at {BROKER}:{PORT}")

        # Start the loop to process network events
        client.loop_forever()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    start_subscriber()
