import paho.mqtt.client as mqtt

# MQTT Broker settings
BROKER = "13.127.101.6"
PORT = 1883
TOPIC = "new/test/topic"

# Create an MQTT client instance (updated API)
client = mqtt.Client(protocol=mqtt.MQTTv5)

# Connect to the broker
print(f"Connecting to broker at {BROKER}:{PORT}")
client.connect(BROKER, PORT, 60)

# Publish a test message to the new topic
message = "Battery:90%"
client.publish(TOPIC, payload=message, qos=0)
print(f"Published message: {message} to topic: {TOPIC}")

# Disconnect from the broker
client.disconnect()

