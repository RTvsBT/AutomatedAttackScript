import socket


class exploit(object):
    def __init__(self):
        self.Name = "GetHostname"
        self.Description = "This function gets the hostname"
        self.Author = "René van Vliet"
        self.Version = "0.1"
        self.POC = ""

        
        self.HOST = None
        self.PORT = None

    def _validate(self):
        pass

    def run(self):
        self._validate()
        print(f"[{self.Name}] " + socket.gethostname())