import pandas as pd
import datetime as dt
import smtplib
import random

# Input info before starting
MY_EMAIL = ""
PASSWORD = ""

birthdays = pd.read_csv("birthdays.csv").to_dict(orient="records")

now = dt.datetime.now()
month = now.month
day = now.day

for entry in birthdays:
    if entry["month"] == month and entry["day"] == day:
        name = entry["name"]
        recipient_email = entry["email"]

        letter_number = random.randint(1, 3)
        with open(f"letter_templates/letter_{letter_number}.txt", "r") as data:
            letter = data.read()
            letter = letter.replace("[NAME]", name)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=recipient_email,
                                msg=f"Subject: Happy Birthday\n\n{letter}")
