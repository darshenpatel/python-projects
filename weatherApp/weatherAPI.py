import json
from typing import Final
from model import Weather, dt
import requests

API_KEY: Final[str] = '1501d73fd8458bf760978520eb026ee2'
BASE_URL: Final[str] = 'https://api.openweathermap.org/data/2.5/forecast'


def get_weather(city: str, mock: bool = True) -> dict:
    if mock:
        with open('mock-data.json') as file:
            return json.load(file)

    # Request live data
    payload: dict = {'q': city, 'appid': API_KEY, 'units': 'imperial'}
    request = requests.get(url=BASE_URL, params=payload)
    data: dict = request.json()

    # # Write mock data to the json file
    # with open('mock-data.json', 'w') as file:
    #     json.dump(data, file)

    return data


def get_weather_details(weather: dict) -> list[Weather]:
    days: list[dict] = weather.get('list')

    if not days:
        raise Exception(f'Problem with json: {weather}')

    weather_list: list[Weather] = []
    for day in days:
        w: Weather = Weather(date=dt.fromtimestamp(day.get('dt')),
                             details=(details := day.get('main')),
                             temp=(details.get('temp')),
                             weather=(weather := day.get('weather')),
                             description=weather[0].get('description')
                             )
        weather_list.append(w)

    return weather_list
