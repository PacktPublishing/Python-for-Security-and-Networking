#!/usr/bin/env python

import socket

host = "domain/ip_address"
port = 80

try:
    mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print(mysocket)
    mysocket.settimeout(5)
except socket.error as error:
	print("socket create error: %s" %error)

try:
    mysocket.connect((host,port))
    print(mysocket)
except socket.timeout as error:
	print("Timeout %s" %error)
except socket.gaierror as error:
	print("connection error to the server:%s" %error)
except socket.error as error:
	print("Connection error: %s" %error)

