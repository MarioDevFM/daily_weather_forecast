import requests
import os
from twilio.rest import Client


TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

MY_LAT = os.environ.get("MY_LAT")
MY_LONG = os.environ.get("MY_LONG")
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.environ.get("OWN_API_KEY")
MY_NUMBER = os.environ.get("MY_NUMBER")
VIRTUAL_NUMBER = os.environ.get("VIRTUAL_NUMBER")

weather_params = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'appid': API_KEY,
    'count': 4,
    'units': 'metric',
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

# check in if rains and sent SMS
hour_counter = 0
temp_list = []
weather_id_list = []

"""collects todays temperature"""
for hour_data in range(0,6):
    temp_min = weather_data['list'][hour_counter]['main']['temp_min']
    temp_max = weather_data['list'][hour_counter]['main']['temp_max']
    hour_counter += 1
    temp_list.append(temp_min)
    temp_list.append(temp_max)

todays_max_temp = max(temp_list)
todays_min_temp = min(temp_list)


"""check if it will rain today"""
hour_counter = 0
weather_id_list = []

for hour_data in range(0,6):
    weather_id = weather_data['list'][hour_counter]['weather'][0]['id']
    hour_counter += 1
    weather_id_list.append(weather_id)


id_for_rain = 700
counter = 0

for w_i in weather_id_list:
    if w_i >= id_for_rain:
        counter += 1
if counter >= 1:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=f"Heute werden es zwischen {todays_min_temp}°C und {todays_max_temp}°C. Du brauchst heute keinen ☂️.",
        from_=f"{VIRTUAL_NUMBER}",
        to=f"{MY_NUMBER}",
    )
else:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=f"Heute werden es zwischen {todays_min_temp}°C und {todays_max_temp}°C.Heute brauchst du einen ☂️.",
        from_=f"{VIRTUAL_NUMBER}",
        to=f"{MY_NUMBER}",
    )










