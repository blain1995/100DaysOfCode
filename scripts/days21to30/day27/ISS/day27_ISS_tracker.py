import requests
from datetime import datetime
import smtplib

# Input info before starting
EMAIL = ""
PASS = ""
MY_LAT = 0
MY_LNG = 0


def close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    if MY_LAT - 5 <= latitude <= MY_LAT + 5 and MY_LNG - 5 <= longitude <= MY_LNG + 5:
        return True
    else:
        return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }
    answer = requests.get(url="http://api.sunrise-sunset.org/json", params=parameters)
    answer.raise_for_status()
    data = answer.json()
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True
    else:
        return False

distance = close()
dark = is_night()

if dark and distance:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(EMAIL, PASS)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg="Subject: Internation Space Station is close! \n\n"
                                                                 "look up!")
