import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = ""
account_sid = ""
auth_token = ""
NCL_lat = 54.978252
NCL_lon = -1.617780

parameters = {
    "appid": api_key,
    "lat": NCL_lat,
    "lon": NCL_lon,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

hourly = weather_data["hourly"][:12]
rain = False
for hour in hourly:
    if hour['weather'][0]['id'] < 800:
        rain = True

if rain:
    print("You will need an umbrella")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Looks like you'll need an umbrella ☔️",
        from_='',
        to=''
    )
    print(message.status)
