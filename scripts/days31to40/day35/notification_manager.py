from twilio.rest import Client
import smtplib
import requests
import os

account_sid = os.environ.get("TWILLIO_SID")
auth_token = os.environ.get("TWILLIO_AUTH")
TWILL_PHONE = os.environ.get("TWILLIO_PHONE")
MY_PHONE = os.environ.get("PERSONAL_PHONE")

FLIGHT_USER_SHEET = os.environ.get("FLIGHT_USER_SPREADSHEET")
MY_EMAIL = os.environ.get("MY_EMAIL")
PASS = os.environ.get("EMAIL_PASS")

class NotificationManager:

    def send_message(self, text_message):
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=text_message,
            from_=TWILL_PHONE,
            to=MY_PHONE)

    def send_emails(self, message, email_mess):
        response = requests.get(url=FLIGHT_USER_SHEET)
        response.raise_for_status()
        data = response.json()["users"]

        for user in data:
            recipient_email = user['email']

            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASS)
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=recipient_email,
                                    msg=f"Subject: Cheap flight! \n\n{message} \n {email_mess}".encode('utf-8'))
