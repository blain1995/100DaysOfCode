import requests
import os

sheety_worksheet_endpoint = os.environ.get("FLIGHT_SPREADSHEET")


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_data(self):
        response = requests.get(url=sheety_worksheet_endpoint)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def input_data(self):
        for city in self.destination_data:
            parameters = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            edit_response = requests.put(url=f'{sheety_worksheet_endpoint}/{city["id"]}', json=parameters)
            print(edit_response.text)
