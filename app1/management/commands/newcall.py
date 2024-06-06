
#! ---------------------------------------
#! Created By: Satyajit
#! Date Created: 2024-05-31
#! Date Modified: 2024-05-31
#! ---------------------------------------

# myapp/management/commands/mqtt_listener.py
from django.core.management.base import BaseCommand
import time
import redis
from app1.management.Scripts.callfunction import MakeCall
from app1.management.Scripts.custom_looger import setup_logger


class Command(BaseCommand):
    help = 'Call the user whose Gateway has stopped'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.redis_cli = redis.Redis(host="98.70.76.242", port=6379, password="Bfl@2024#redis", db=0)
        self.logger = setup_logger()
        self.call = MakeCall()

    def handle(self, *args, **options):
        while True:
            try:
                device_ids = self.redis_cli.smembers("device_ids")
                if not device_ids:
                    self.logger.info("No devices found.")
                    time.sleep(5)
                    continue
                    
                for device_id_bytes in device_ids:
                    device_id = device_id_bytes.decode("utf-8")
                    cpu_temp_data = self.redis_cli.hgetall(f"cpu_temp/{device_id}")
                    if cpu_temp_data:
                        self.logger.info(f"Device ID: {device_id}, CPU Temp Data: {cpu_temp_data}")
                    else:
                        self.logger.info(f"No CPU temp data found for Device ID: {device_id}")
                        self.call.make_call(device_id)

            except KeyboardInterrupt:
                self.logger.info("MQTT client stopping...")
                return

            except Exception as e:
                self.logger.error(f"Error: {str(e)}")
            time.sleep(1)


