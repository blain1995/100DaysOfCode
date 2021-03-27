import smtplib
import datetime as dt
import random

now = dt.datetime.now()
day = now.weekday()

# Input info before starting
my_email = ""
password = ""

if day == 5:
    with open("quotes.txt", "r") as data:
        quotes = data.readlines()
    message = random.choice(quotes)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="",
                            msg=f"Subject:Monday Motivation\n\n{message}")
