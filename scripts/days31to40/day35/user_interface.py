import requests
import os

spreadsheet_endpoint = os.environ.get("FLIGHT_USER_SPREADSHEET")

print("Welcome to Alex's Flight Club")
print("We find the best flight deals and email you.")
first_name = input("What is your first name?")
last_name = input("What is your last name?")
email = input("What is your email?: ").lower()
email_confirm = input("Please confirm your email: ").lower()

if email == email_confirm:
    print("Congratulations, you're in the club!")
    parameters = {
        "user": {
          "firstName": first_name,
          "lastName": last_name,
          "email": email
        }
    }

    response = requests.post(url=spreadsheet_endpoint, json=parameters)
    response.raise_for_status()
    print(response.json())

else:
    print("Sorry, those emails don't match")
