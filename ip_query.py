
import time
import requests
import urllib3
import socket



class ExternalIpQuery():
    def __init__(self, api):
        self.api = api
        self.url = api
        
    def is_connected(self, timeout = 3):
        try:
            request = requests.head(self.url, timeout=timeout)
            return True
        except requests.ConnectionError as ex:
            print(ex)
            return False
    
    def request_ip(self, timeout = 3):
        ip = None
        try:
            ip = requests.get(self.api).text
        except socket.gaierror as socket_error:
            print(socket_error)
            print("socket error!")
        except urllib3.exceptions.NewConnectionError as urllib3_ex_new_conn_error:
            print(urllib3_ex_new_conn_error)
            print("new connection error!")
        except urllib3.exceptions.MaxRetryError as url_maxtry_error:
            print(url_maxtry_error)
            print("Max retries error!")
        except requests.exceptions.ConnectionError as req_ex_conn_error:
            print(req_ex_conn_error)
            print("connection error!")
        return ip
               
            
def main():
    api = "https://api.ipify.org"


    p1 = ExternalIpQuery(api)
    ip = p1.request_ip()
    print(ip)
    

   


if __name__ == "__main__": main()

