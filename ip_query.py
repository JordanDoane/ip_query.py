
import time
from requests import get


class ExternalIpQuery():
    def __init__(self, api):
        self.api = api

    def request_ip(self):
        try:
            ip = get(self.api).text
        except ConnectionError:
            print("error")
            time.sleep(30)
        return ip




api = "https://api.ipify.org"




