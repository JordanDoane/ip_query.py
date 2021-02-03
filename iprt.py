
class Iprt:
    from file_tool import FileTools
    import time
    from ip_query import ExternalIpQuery
    
    log_file = "/home/drako/Projects/ip_query_tool/iprt.log"
    config_file = "/home/drako/Projects/ip_query_tool/iprt.conf"
    config = {}
    
    #Retriving values from config file
    read_config = FileTools(config_file)
    config = read_config.read_config_file()

    log_f = FileTools(log_file)

    print(config.get("api"))

    ip_tool = ExternalIpQuery(config.get("api"))
    ip = ip_tool.request_ip()
    log_f.write_log_file(f"!Start ip: {ip}", True)

    def __init__(self):
        self.api = self.config.get("api")
        self.mqtt_broker = self.config.get("mqtt_broker")
        self.ip = self.ip_tool.request_ip()

      
    def run(self):
        
        print("running!")
        times_failed = 0
        while True:
    
            is_connection = self.ip_tool.is_connected()

            if is_connection == False and times_failed == 0:
                print(f"Connection failed : {times_failed}")
                self.log_f.write_log_file(f"!Connetion failed", True)
                times_failed += 1
                self.time.sleep(60)
                continue

            elif is_connection == False and times_failed >= 1:
                print(f"Connection failed : {times_failed}")
                times_failed += 1
                self.time.sleep(60)
                continue
                

            else:
                if times_failed > 0:
                    print("!Connection reestablished")
                    self.log_f.write_log_file(f"!Connection reestablished", True)
                    times_failed = 0
                
                if self.ip == self.ip_tool.request_ip():
                    print(self.ip)
                    self.time.sleep(60)
                    continue
                else:
                    self.ip = self.ip_tool.request_ip()
                    self.log_f.write_log_file( self.ip, True)
                    #send new ip to mqtt_broker
                    continue

                
                
            
               
          
                

def main():
    app = Iprt()
    app.run()


if __name__ == "__main__": main()