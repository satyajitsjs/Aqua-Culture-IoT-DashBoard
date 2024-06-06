
#! ---------------------------------------
#! Created By: Satyajit
#! Date Created: 2024-05-31
#! Date Modified: 2024-05-31
#! ---------------------------------------
from twilio.rest import Client
from app1.models import Device
import redis
from app1.management.Scripts.custom_looger import setup_logger
class MakeCall:
    
    def __init__(self):
        self.logger = setup_logger()
        self.__redis_cli = redis.Redis(host="98.70.76.242", port=6379, password="Bfl@2024#redis", db=0)
    
    def make_call(self,device_id):
        try:
            self.logger.info(f"Making call for Device ID: {device_id}")
            twiml_message = f'<Response><Say>Hello. Your device with ID {device_id} has stopped operating. Please check it for any issues. Thank you. Goodbye.</Say><Hangup/></Response>'
            device = Device.objects.select_related('account__user').get(device_id=device_id)
            mobile_number = device.account.user.Mobno
            self.twilio_call(twiml_message, mobile_number)
            result = self.__redis_cli.srem("device_ids",device_id)
            self.logger.info(f"Device ID: {device_id} removed from device_ids set")
        except Exception as e:
            self.logger.error(f"Error in make_call for Device ID {device_id}: {str(e)}")

    def twilio_call(self,twiml_message, mobile_number):
        try:
            account_sid = "AC91845037a84cef29dc2a9baa2cf66548"
            auth_token = "cc059db10a170318b3f9f353209c54c7"
            client = Client(account_sid, auth_token)

            call = client.calls.create(
                twiml=twiml_message,
                to=f'+91{mobile_number}',
                from_='+12182204752'
            )

            self.logger.info(f"Twilio call SID: {call.sid}")
        except Exception as e:
            self.logger.error(f"Error in Twilio call: {str(e)}")


