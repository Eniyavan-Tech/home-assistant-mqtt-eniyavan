import time
import json
import paho.mqtt.client as mqtt

student_name = "Eniyavan.M"
unique_id = "42110332"
topic = "home/eniyavan-2025/sensor"

broker = "192.168.56.1"
port = 1883

client = mqtt.Client("publisher-eniyavan")
client.connect(broker, port)

while True:
    payload = {
        "name": student_name,
        "register_no": unique_id,
        "temperature": 25,
        "humidity": 60,
        "light": 300
    }

    client.publish(topic, json.dumps(payload))
    print("Published:", payload)
    time.sleep(5)
