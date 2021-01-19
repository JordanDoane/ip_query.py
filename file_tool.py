#
file_path ="ip_address.txt"

class FileTools():
    def __init__(self,file_path):
       self.file_path = file_path

    def read_past_address(self):
        with open(file_path, 'r') as reader:
            past_addresses = reader.readlines()
            last_address = past_addresses[-1]
            return last_address

    def read_past_addresses(self):
        with open(file_path, 'r') as reader:
            past_addresses = reader.readlines()
            return past_addresses

    def WriteNewLine(self, line, time_date = None):
        import time
        with open(file_path, 'a') as writer:
            if time_date:
                time_stamp = time.asctime(time.localtime())
                line = f"{time_stamp} {line}\n"
                writer.write(line)
            else:
                line = f"{line} \n"
                writer.write(line)
            
            
    


p1 = FileTools(file_path)

address = p1.read_past_address()
addresses = p1.read_past_addresses()

ip = "192.168.1.112"

p1.WriteNewLine(ip, True)
