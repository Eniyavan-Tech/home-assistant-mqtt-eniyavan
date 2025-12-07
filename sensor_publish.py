import time
import json
import random
import paho.mqtt.client as mqtt

student_name = "Eniyavan.M"
unique_id = "42110332"
topic = "home/eniyavan-2025/sensor"

broker = "192.168.56.1"
port = 1883

client = mqtt.Client("publisher-eniyavan")
client.connect(broker, port)

temperature = 25
humidity = 60
light = 300

while True:
    # simulate live sensor variation
    temperature += random.choice([-1, 0, 1])
    humidity += random.choice([-1, 0, 1])
    light += random.choice([-10, 0, 10])

    payload = {
        "name": student_name,
        "register_no": unique_id,
        "temperature": temperature,
        "humidity": humidity,
        "light": light
    }

    client.publish(topic, json.dumps(payload))
    print("Published:", payload)
    time.sleep(5)
