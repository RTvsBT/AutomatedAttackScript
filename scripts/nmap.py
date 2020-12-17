import Util, random, socket

class exploit(object):
    def __init__(self):
        self.Name = "NMAP"
        self.Description = "NMAP Alerts"
        self.Author = "René van Vliet"
        self.Version = "0.1"
        self.POC = ""
        self.Type = Util.Type.Remote
        self.Platform = Util.Platform.Linux

        self.HOST = None
        self.PORT = None


    def exploit(self):
        r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        r.connect((self.HOST,22))
        r.recv(2048)
        r.sendmsg("get_banner")
        r.close()

    def _validate(self):
        if(self.HOST == None):
            print(f"[{self.Name}] No valid parameters.")
            exit(1)


    def run(self):
        self._validate()
        self.exploit()
