import pwn, Util

class exploit(object):
    def __init__(self):
        self.Name = "NIDS_Mock2"
        self.Description = "Fake the first nids alert"
        self.Author = "René van Vliet"
        self.Version = "0.1"
        self.POC = ""
        self.Type = Util.Type.Remote
        self.Platform = Util.Platform.Linux

        self.HOST = None
        self.PORT = 8000


    def exploit(self):
        remote = pwn.remote(self.HOST, self.PORT)
        remote.sendline("Mock2")
        remote.close()


    def _validate(self):
        if(self.HOST == None):
            print(f"[{self.Name}] No valid parameters.")
            exit(1)


    def run(self):
        self._validate()
        self.exploit()