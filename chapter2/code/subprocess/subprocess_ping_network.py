#!/usr/bin/env python
from subprocess import Popen, PIPE
import sys

print("Operating system:",sys.platform)

if sys.platform.startswith("linux"):
    command_ping ='/bin/ping'
elif sys.platform == "darwin":
    command_ping ='/sbin/ping'
elif os.name == "nt":
	command_ping ='ping'
	
for ip in range(1,4):
	ipAddress = '192.168.18.'+str(ip)
	print("Scanning %s " %(ipAddress))
	subprocess = Popen([command_ping, '-c 1',ipAddress], stdin=PIPE, stdout=PIPE, stderr=PIPE)
	stdout, stderr= subprocess.communicate(input=None)
	print(stdout)
	if b"bytes from " in stdout:
		print("The Ip Address %s has responded with a ECHO_REPLY!" %(stdout.split()[1]))
