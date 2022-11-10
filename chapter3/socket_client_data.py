#!/usr/bin/python

import socket


host = input("Enter host name: ")
port = int(input("Enter port number: "))
try:
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
		socket_tcp.settimeout(10)
		if (socket_tcp.connect_ex((host,port)) == 0):
			print("Established connection to the server %s in the port %s" % (host, port))
			request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % host
			socket_tcp.send(request.encode())
			data = socket_tcp.recv(4096)
			print("Data:",repr(data))
			print("Length data:",len(data))
except socket.timeout as error:
	print("Timeout %s" %error)
except socket.gaierror as error:
	print("connection error to the server:%s" %error)
except socket.error as error:
	print("Connection error: %s" %error)
