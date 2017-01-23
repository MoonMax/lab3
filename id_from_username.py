from base_client import BaseClient
import requests, json

class IDFromUsername(BaseClient):
    BASE_URL = 'https://api.vk.com/method/users.get'
    http_method = 'GET'

    def get_params(self):
        return {
            'user_ids': self.name
        }

    def __init__(self, name):
        self.name = name


    def response_handler(self, response):
        parsed = json.loads(response.text)
        try:
            return parsed.get('response')[0].get('uid')
        except:
            return -1
