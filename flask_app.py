import os


import weather


from flask import Flask
from flask import request
from flask import jsonify


from bot import send_message


app = Flask(__name__)


TOKEN = os.environ.get('TOKEN')


@app.route('/', methods=['POST', 'GET'])
def index():
    return '<h1>Bot is currently working.</h1>'


@app.route(f'/{TOKEN}', methods=['POST', 'GET'])
def bot():
    if request.method == 'POST':
        process_request(request)
        return '<H1>POST</H1>'
    return '<h1>GET</h1>'


def process_request(request):
    response = request.get_json()
    chat_id = response['message']['chat']['id']

    try:
        text = response['message']['text']
    except KeyError:
        send_message(chat_id, 'Input is incorrect!')
    
    if text == '/start':
        send_message(chat_id, "This bot can send you weather data from any City.\nType '/help' to see how-to.")
    elif text == '/help':
        send_message(chat_id, 'none')
    elif text == '/weather':
        send_message(chat_id, 'Type name of the city:')
    else:
        city = text.split()[0].capitalize()
        data = weather.get_weather_data(city)
        if data != None:
            send_message(
                chat_id,
                f"""
                City: {city}
{data['weather']}, {data['temp']} °C, feels like {data["feels_like"]} °C
Wind speed: {data["wind_sp"]} m/s
                """
            )
        else:
            send_message(chat_id, 'Incorrect input, please try again.')
