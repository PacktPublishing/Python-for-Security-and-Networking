#!/usr/bin/python

import socket

try:
	hostname = socket.gethostname()
	print("gethostname:",hostname)
	ip_address = socket.gethostbyname(hostname)
	print("Local IP address: %s" %ip_address)
	print("gethostbyname:",socket.gethostbyname('www.python.org'))
	print("gethostbyname_ex:",socket.gethostbyname_ex('www.python.org'))
	print("gethostbyaddr:",socket.gethostbyaddr('8.8.8.8'))
	print("getfqdn:",socket.getfqdn('www.google.com'))
	print("getaddrinfo:",socket.getaddrinfo("www.google.com",None,0,socket.SOCK_STREAM))

except socket.error as error:
   print (str(error))
   print ("Connection error")
   
