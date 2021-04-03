import requests
import os
from datetime import date, timedelta

FLIGHT_API_KEY = os.environ.get("FLIGHT_API_KEY")
TEQUILA_API_ENDPOINT = 'https://tequila-api.kiwi.com/v2/search'

today = date.today().strftime('%d/%m/%Y')
six_months = date.today() + timedelta(days=180)
six_months = six_months.strftime('%d/%m/%Y')


class FlightData:
    def __init__(self):
        self.today = date.today().strftime('%d/%m/%Y')
        self.six_months = date.today() + timedelta(days=180)
        self.six_months = self.six_months.strftime('%d/%m/%Y')

    def flight_info(self, city):
        parameters = {
            'apikey': FLIGHT_API_KEY,
            "fly_from": "LON",
            "fly_to": city,
            "date_from": self.today,
            "date_to": self.six_months,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "adults": 1,
            "curr": "GBP",
            "max_stopovers": 0
        }
        response = requests.get(url=TEQUILA_API_ENDPOINT, params=parameters)
        response.raise_for_status()

        try:
            data = response.json()["data"][0]
        except IndexError:
            return "unavailable"
        else:
            return data
