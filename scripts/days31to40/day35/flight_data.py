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


    def flight_info(self, city, stop_overs=0):
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
            "max_stopovers": stop_overs
        }
        response = requests.get(url=TEQUILA_API_ENDPOINT, params=parameters)
        response.raise_for_status()

        try:
            data = response.json()["data"][0]
        except IndexError:
            parameters['max_stopovers'] = 1
            response = requests.get(url=TEQUILA_API_ENDPOINT, params=parameters)
            try:
                data = response.json()["data"][0]
            except:
                return "unavailable"
            else:
                data['stop_overs'] = 1
                return data
        else:
            data['stop_overs'] = 0
            return data
