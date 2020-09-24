import requests
import os


TOKEN = os.environ.get('TOKEN')


URL_BASE = f'https://api.telegram.org/bot{TOKEN}/'


def send_message(chat_id, text='No message were recieved'):
    url = URL_BASE + f'sendmessage?chat_id={chat_id}&text={text}'
    print(url)
    requests.get(url)
