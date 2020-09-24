import requests
import os


API_URL = 'http://api.openweathermap.org/data/2.5/weather'

API_KEY = os.environ.get('API_KEY')


def get_weather_data(city_name):
    response = requests.get(API_URL + f'?q={city_name}&appid={API_KEY}&units=metric').json()
    if response['cod'] == 200:
        response_formatted = format_data(response)
        return response_formatted
    return None

def format_data(response):
    return {
        'weather': response['weather'][0]['description'],
        'temp': response['main']['temp'],
        'feels_like': response['main']['feels_like'],
        'wind_sp': response['wind']['speed']
    }