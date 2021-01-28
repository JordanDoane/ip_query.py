

from ip_query import ExternalIpQuery
from os import EX_CONFIG


class Iprt:
    from file_tool import FileTools
    import time
    from ip_query import ExternalIpQuery
    
    config_file = "/home/drako/Projects/ip_query_tool/iprt.conf"
    config = {}
    
    #Retriving values from config file
    read_config = FileTools(config_file)
    config = read_config.read_config_file()

    print(config.get("api"))

    ip_tool = ExternalIpQuery(config.get("api"))
    ip = ip_tool.request_ip()

    def __init__(self):
        self.api = self.config.get("api")
        self.mqtt_broker = self.config.get("mqtt_broker")
        self.ip = self.ip_tool.request_ip()

      
    def run(self):
        print("running!")
        while True:
            if self.ip_tool.request_ip() != self.ip:
                self.ip = self.ip_tool.request_ip()
            else:
                print(self.ip)
                self.time.sleep(10)
            
               
          
                

def main():
    app = Iprt()
    app.run()


if __name__ == "__main__": main()