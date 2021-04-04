from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_data()

if sheet_data[0]['iataCode'] == "":
    flight_search = FlightSearch()
    for city in sheet_data:
        city["iataCode"] = flight_search.get_city_code(city["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.input_data()

flight_data = FlightData()

for city in sheet_data:
    data = flight_data.flight_info(city["iataCode"])
    if data == "unavailable":
        print(f"{city['city']}: not available, even with stopover")
        continue
    else:
        price = data["price"]
        print(f"{city['city']}: £{price}")
    if price is not None:
        if int(price) < city["lowestPrice"]:
            routes = data['route']
            depart = routes[0]['local_arrival'].split("T")[0]
            return_flight = routes[1]['local_arrival'].split("T")[0]

            message = f"Low price alert! Only £{price} to fly from {data['cityFrom']}-{data['flyFrom']} to" \
                      f" {data['cityTo']}-{data['flyTo']}, departing {depart} and returning {return_flight}"

            stop_overs = data['stop_overs']
            if stop_overs > 0:
                via_city = data['route'][0]["cityTo"]
                message += f"\n Flight has {stop_overs} stop over, via {via_city}"

            email_messs = f"https://www.google.co.uk/flights?hl=en#flt={data['flyFrom']}.{data['flyTo']}.{depart}*{data['flyTo']}.{data['flyFrom']}.{return_flight}"

            notification = NotificationManager()
            # notification.send_message(message)

            notification.send_emails(message, email_messs)