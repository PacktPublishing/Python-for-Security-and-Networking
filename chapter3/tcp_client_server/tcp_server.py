#!/usr/bin/python

import socket

SERVER_IP   = "127.0.0.1"
SERVER_PORT = 9999

#  family = Internet, type = stream socket means TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_IP,SERVER_PORT))
server.listen(5)
print("[*] Server Listening on %s:%d" % (SERVER_IP,SERVER_PORT))
client,addr = server.accept()
client.send("I am the server accepting connections on port 999...".encode())
print("[*] Accepted connection from: %s:%d" % (addr[0],addr[1]))

while True:
	request = client.recv(1024).decode()
	print("[*] Received request :%s" % (request))
	if request!="quit":
		client.send(bytes("ACK","utf-8"))
	else:
		break
    
client.close()
server.close()
