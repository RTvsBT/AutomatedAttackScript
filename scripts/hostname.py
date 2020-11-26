import socket
import Util

class Exploit(object):
    def __init__(self):
        self.Name = "GetHostname"
        self.Description = "This function gets the hostname"
        self.Author = "René van Vliet"
        self.Version = "0.1"
        self.Platform = Util.Platform.Any
        self.Type = Util.Type.Local
        self.POC = ""

        
        self.HOST = None
        self.PORT = None

    def _validate(self):
        pass

    def run(self):
        self._validate()
        print(f"[{self.Name}] " + socket.gethostname())