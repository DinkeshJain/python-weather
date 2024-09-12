from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="Visakhapatnam"):
    request_url=f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv("API_KEY")}&units=imperial'
    weather_data=requests.get(request_url).json()
    return weather_data

if __name__ == '__main__':
    print('\n *** Get Current Weather Conditions ***\n')
    city=input('Enter a city name:')
    if not bool(city.strip()):
        city="Visakhapatnam"
    weather_data=get_current_weather(city)
    print()
    pprint(weather_data)