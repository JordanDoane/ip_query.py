
from requests import get

class ExternalIpQuery():
    def __init__(self, api):
        self.api = api

    def request_ip(self):
        ip = get(api).text
        return ip




api = "https://api.ipify.org"




