import paho.mqtt.client as mqtt

# MQTT Broker settings
BROKER = "13.127.101.6"
PORT = 1883
TOPIC = "new/test/topic"

# Callback for when the client connects to the broker
def on_connect(client, userdata, flags, reason_code, properties):
    print("Connected successfully to broker!")
    # Subscribe to the topic
    client.subscribe(TOPIC)
    print(f"Subscribed to topic: {TOPIC}")

# Callback for when a message is received from the broker
def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic: {msg.topic}")

# Create an MQTT client instance (updated API)
client = mqtt.Client(protocol=mqtt.MQTTv5)

# Assign callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
print(f"Connecting to broker at {BROKER}:{PORT}")
client.connect(BROKER, PORT, 60)

# Start the loop to process incoming messages
try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\nDisconnecting from broker...")
    client.disconnect()

