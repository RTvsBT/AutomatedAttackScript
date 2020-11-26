import pwn, Util

class exploit(object):
    def __init__(self):
        self.Name = "NIDS_Mock1"
        self.Description = "Fake the first nids alert"
        self.Author = "René van Vliet"
        self.Version = "0.1"
        self.POC = ""
        self.Type = Util.Type.Remote
        self.Platform = Util.Platform.Linux

        self.HOST = None
        self.PORT = None


    def exploit(self):
        remote = pwn.remote(self.HOST, self.PORT, typ="udp")
        remote.sendline("mock1")


    def _validate(self):
        if(self.HOST == None):
            print(f"[{self.Name}] No valid parameters.")
            exit(1)


    def run(self):
        self._validate()
        self.exploit()