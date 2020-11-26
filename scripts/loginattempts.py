import pwn, Util

class exploit(object):
    def __init__(self):
        self.Name = "SSHLoginAttempts"
        self.Description = "Multiple SSH login attempts with wrong admin credentials"
        self.Author = "Rens van der Linden"
        self.Version = "0.2"
        self.POC = ""
        self.Type = Util.Type.Remote
        self.Platform = Util.Platform.Linux

        self.HOST = None
        self.PORT = None


    def exploit(self):
        l = listen()
        for _ in range(3):
            try: 
                s = pwn.ssh(host=self.HOST, user='admin', password='P@ssw0rd')
                s.connect_remote(s.host, l.lport)
            except:
                pass


    def _validate(self):
        if(self.HOST == None):
            print(f"[{self.Name}] No valid parameters.")
            exit(1)


    def run(self):
        self._validate()
        self.exploit()
