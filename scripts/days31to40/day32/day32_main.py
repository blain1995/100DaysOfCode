import requests
import os
from datetime import datetime

date = datetime.now().strftime("%Y-%m-%d")
time = datetime.now().strftime("%H:%M")

NUTRITION_APP_ID = os.environ.get("NUTRITION_APP_ID")
NUTRITION_API_KEY = os.environ.get("NUTRITION_API_KEY")
endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = os.environ.get("WORKOUT_SPREADSHEET")
sheety_token = os.environ.get("SHEETY_TOKEN")

parameters = {
    "query": input("what exercise did you do today?"),
    "gender": "female",
    "weight_kg": 78,
    "height_cm": 169,
    "age": 25
}

headers = {
    "x-app-id": NUTRITION_APP_ID,
    "x-app-key": NUTRITION_API_KEY,
}

headers_sheety = {
    "Authorization": sheety_token
}

response = requests.post(url=endpoint, json=parameters, headers=headers)
response.raise_for_status()
data = response.json()
exercise = data["exercises"]

for activity in exercise:
    exercise_parameters = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": activity['name'],
            "duration": activity['duration_min'],
            "calories": activity['nf_calories']
        }
    }
    response_sheety = requests.post(url=sheety_endpoint, json=exercise_parameters, headers=headers_sheety)
    response_sheety.raise_for_status()
    print(response_sheety.text)
