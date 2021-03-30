import requests
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY_NEWS = os.environ.get("NEWS_API_KEY")
account_sid = os.environ.get("TWILLIO_SID")
auth_token = os.environ.get("TWILLIO_AUTH")
TWILLIO_PHONE = os.environ.get("TWILLIO_PHONE")
PERSONAL_PHONE = os.environ.get("PERSONAL_PHONE")

parameters_stocks = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "datatype": "json",
    "outputsize": "compact",
    "apikey": API_KEY
}

parameters_news = {
    'apiKey': API_KEY_NEWS,
    'qInTitle': "Tesla",
    'language': 'en'
}

up = True

def get_difference():
    global up
    if float(last_two_days[0]) - float(last_two_days[1]) < 0:
        up = False
        value = (float(last_two_days[0]) - float(last_two_days[1])) * -1
        return value
    else:
        return float(last_two_days[0]) - float(last_two_days[1])

response = requests.get(url=STOCK_ENDPOINT, params=parameters_stocks)
response.raise_for_status()


stock_data = response.json()["Time Series (Daily)"]
stock_list = [value for (key,value) in stock_data.items()]
last_two_days = [stock_list[0]["4. close"], stock_list[1]["4. close"]]

difference = get_difference()
five_percent = float(last_two_days[0]) * 0.05

percentage = (difference / float(last_two_days[1])) * 100


if difference > five_percent:
    news_response = requests.get(url=NEWS_ENDPOINT, params=parameters_news)
    news_response.raise_for_status()
    articles = news_response.json()['articles'][:3]
    print(articles)
    client = Client(account_sid, auth_token)
    for i in articles:
        if up:
            emoji = "🔺"
        else:
            emoji = "🔻"
        message = client.messages \
            .create(
            body=f"Tesla {emoji} {percentage}% \n"
                 f"Headline: {i['title']} \n Brief: {i['description']}",
            from_=TWILLIO_PHONE,
            to=PERSONAL_PHONE
        )
