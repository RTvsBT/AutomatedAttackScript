import pwn, Util, random, nmap3

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
        r = pwn.remote(self.host, 22)
        r.recv()
        r.sendline("get_banner")


    def _validate(self):
        if(self.HOST == None):
            print(f"[{self.Name}] No valid parameters.")
            exit(1)


    def run(self):
        self._validate()
        self.exploit()
