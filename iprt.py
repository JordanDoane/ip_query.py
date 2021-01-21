
from file_tool import FileTools
from ip_query import ExternalIpQuery
import time

config_file = "ipqt.conf"
config = {}

read_config = FileTools(config_file)
config = read_config.Read_file()

log_file = "ipqt.log"
log_write = FileTools(log_file)



ip = ExternalIpQuery(config.get("api"))
current_ip = ip.request_ip()
log_write.WriteNewLine(current_ip, True)

while True:

    if ip.request_ip() != current_ip:
        new_ip = ip.request_ip()
        log_write.WriteNewLine(new_ip)

    else:
        time.sleep(60)






