
#! ---------------------------------------
#! Created By: Satyajit
#! Date Created: 2024-05-31
#! Date Modified: 2024-05-31
#! ---------------------------------------

# myapp/management/commands/mqtt_listener.py
from django.core.management.base import BaseCommand
from app1.management.mqtt.mqtt_script import MqttConnect
from paho.mqtt.client import Client
import time
import json

class Command(BaseCommand):
    help = 'Starts the MQTT message listener'

    def handle(self, *args, **options):
        mq = MqttConnect()
        mq.topic = ["299104867328041/data"]
        
        def on_sub_message(client, userdata, message):
            global status
            data = json.loads(message.payload.decode('utf-8'))
            print(data)
        
        def data_subscribe():
            mqtt_client = Client()
            mqtt_client.on_connect = mq.on_connect
            mqtt_client.on_message = on_sub_message
            mqtt_client.username_pw_set(mq._username, mq._password)
            mqtt_client.connect(mq._mqttBroker, port=mq._port)
            mqtt_client.loop_start()
            
            print("MQTT client started and waiting for messages...")

            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                print("MQTT client stopping...")
                mqtt_client.loop_stop()
        
        data_subscribe()
        print("MQTT listener started. Press Ctrl+C to stop.")
