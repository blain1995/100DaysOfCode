import requests
import datetime
import os

pixela_username = os.environ.get("PIXELA_USERNAME")
pixela_token = os.environ.get("PIXELA_TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"https://pixe.la/v1/users/{pixela_username}/graphs"
pixel_endpoint = f"https://pixe.la/v1/users/{pixela_username}/graphs/graph1"

today = datetime.datetime.now()

user_params = {
    "token": pixela_token,
    "username": pixela_username,
    "agreeTermsOfService":  "yes",
    "notMinor": "yes"
}

graph_params = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

pixel_config = {
    "date": today.strftime('%Y%m%d'),
    "quantity": input("How many kilometers did you cycle today?"),
}

pixel_update_params = {
    "quantity": "3"
}


headers = {
    "X-USER-TOKEN": pixela_token
}

# ---------------------- uncomment this section as required-----------------------

# Create user (only do first time)
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Build the graph
# graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(graph_response.text)

# post a pixel to the graph
# pixel_response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(pixel_response.text)

# Update a pixel
# pixel_update = requests.put(url=f"https://pixe.la/v1/users/{pixela_username}/graphs/graph1/20210330",
#                             json=pixel_update_params, headers=headers)
#
# print(pixel_update.text)

# Delete a pixel
# pixel_delete = requests.delete(url=f"https://pixe.la/v1/users/{pixela_username}/graphs/graph1/20210330", headers=headers)
# print(pixel_delete.text)
