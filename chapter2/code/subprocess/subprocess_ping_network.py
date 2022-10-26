#!/usr/bin/env python
from subprocess import Popen, PIPE

for ip in range(1,4):
	ipAddress = '192.168.18.'+str(ip)
	print("Scanning %s " %(ipAddress))
	subprocess = Popen(['/bin/ping', '-c 1',ipAddress], stdin=PIPE, stdout=PIPE, stderr=PIPE)
	stdout, stderr= subprocess.communicate(input=None)
	print(stdout)
	if b"bytes from " in stdout:
		print("The Ip Address %s has responded with a ECHO_REPLY!" %(stdout.split()[1]))
