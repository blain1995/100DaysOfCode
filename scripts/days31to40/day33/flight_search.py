import requests
import os

FLIGHT_API_KEY = os.environ.get("FLIGHT_API_KEY")
FLIGHT_API_ENDPOINT = 'https://tequila-api.kiwi.com/locations/query'


class FlightSearch:

    def get_city_code(self, city):
        header = {'apikey': FLIGHT_API_KEY}
        parameters = {"term": city, "location_types": "city"}
        response = requests.get(url=FLIGHT_API_ENDPOINT, headers=header, params=parameters)
        data = response.json()["locations"]
        code = data[0]["code"]
        return code
