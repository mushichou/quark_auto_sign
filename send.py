import requests as rq

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

    def server_send(self, text):
        url = f'https://sctapi.ftqq.com/{self.sendkey}.send?title=夸克网盘自动签到&desp={text}'
        rq.post(url)