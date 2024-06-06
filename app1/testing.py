from django.core.management.base import BaseCommand

from paho.mqtt.client import Client
import time
import threading
from PIL import Image
from io import BytesIO
import numpy as np
import json



broker_address = "4.240.114.7"
broker_port = 1883
username = "BarifloLabs"
password = "Bfl@123"
topics = ["307452396536950"] # Replace with your MQTT topic


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        for topic in topics:
            client.subscribe(str(topic))
    else:
        print(f"Connection failed with code {rc}")
def on_message(client, userdata, message):
    
    payload = message.payload
    # print(f"Received message: {payload}")
    try:
        data = (payload.decode('utf-8'))
        print(f"Received message: {data}")
    except Exception as e:
        print("Error converting received message to image:", str(e))
    
if __name__ == "__main__":
    mqtt_client = Client("client")
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    mqtt_client.username_pw_set(username, password)
    mqtt_client.connect(broker_address, broker_port)
    mqtt_client.loop_start()

try:
    while True:
        pass
except:
    print("Disconnected")