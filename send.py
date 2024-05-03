import requests as rq
import urllib.parse
import urllib.request
import os

class Send:
    def __init__(self, token):
        self.token = token

    def tg_send(self, chat_id, text):
        url = f'https://api.telegram.org/bot{self.token}/sendMessage'
        data = {
            'chat_id': chat_id,
            'text': text
        }
        rq.post(url, data=data)
        
class ServerSend:
    def __init__(self, sendkey):
        self.sendkey = sendkey

    def server_send(self, text, desp=''):
        postdata = urllib.parse.urlencode({'text': text, 'desp': desp}).encode('utf-8')
        # print(text, desp)
        url = f'https://sctapi.ftqq.com/{self.sendkey}.send'
        # print(url)
        req = urllib.request.Request(url, data=postdata, method='POST')
        with urllib.request.urlopen(req) as response:
            result = response.read().decode('utf-8')
        return result