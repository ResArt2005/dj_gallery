from django.shortcuts import render
import requests
from .models import *

def send_message(message, who, file=None):
    telegram = Telegram.objects.filter(who=who).first()
    token = telegram.token
    url = telegram.url
    channel_id = telegram.chanel_id
    method = '{url}{token}/sendMessage'.format(url=url, token=token)
    r = requests.post(method, data={
        "chat_id": channel_id,
        "text": message
    })
    if file:
        with open(file, "rb") as filexlsx:
            files = {"document": filexlsx}
            title = "test.txt"
            method = '{url}{token}/sendDocument'.format(url=url, token=token)
            r = requests.post(method, data={
                "chat_id": channel_id,
                "caption": title
            }, files=files)
    if r.status_code != 200:
        result = {'status': 'error'}
    else:
        result = {'status': 'ok'}
    return result

