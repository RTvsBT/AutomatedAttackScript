import pwn, Util, random

class exploit(object):
    def __init__(self):
        self.Name = "HIDS_Mock1"
        self.Description = "Fake the HIDS alert"
        self.Author = "René van Vliet"
        self.Version = "0.1"
        self.POC = ""
        self.Type = Util.Type.Local
        self.Platform = Util.Platform.Linux

        self.HOST = None
        self.PORT = None


    def exploit(self):
        remote = pwn.ssh(host=self.HOST, user="student", password="student")
        remote(f"/bin/echo {str(random.randint(1,100))} >> /test/Mock1.log")
        remote.close()


    def _validate(self):
        if(self.HOST == None):
            print(f"[{self.Name}] No valid parameters.")
            exit(1)


    def run(self):
        self._validate()
        self.exploit()