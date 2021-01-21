#

class FileTools():
    def __init__(self,file_path):
       self.file_path = file_path

    def read_past_address(self):
        with open(self.file_path, 'r') as reader:
            past_addresses = reader.readlines()
            last_address = past_addresses[-1]
            return last_address

    def read_past_addresses(self):
        with open(self.file_path, 'r') as reader:
            past_addresses = reader.readlines()
            return past_addresses

    def WriteNewLine(self, line, time_date = None):
        import time
        with open(self.file_path, 'a') as writer:
            if time_date:
                time_stamp = time.asctime(time.localtime())
                line = f"{time_stamp} {line}\n"
                writer.write(line)
            else:
                line = f"{line} \n"
                writer.write(line)

    def Read_file(self):
        conf = {}
        with open(self.file_path, 'r') as reader:
            for line in reader.readlines():
                if line == '#\n' or line == '\n':
                    continue
                else:
                    arguments = line.split(" ")
                    conf.update({arguments[0]:arguments[1].strip('\n')})
        return conf
            