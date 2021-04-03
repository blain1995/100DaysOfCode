from twilio.rest import Client
import os

account_sid = os.environ.get("TWILLIO_SID")
auth_token = os.environ.get("TWILLIO_AUTH")
TWILL_PHONE = os.environ.get("TWILLIO_PHONE")
MY_PHONE = os.environ.get("PERSONAL_PHONE")


class NotificationManager:

    def send_message(self, text_message):
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=text_message,
            from_=TWILL_PHONE,
            to=MY_PHONE)
