import ssl
ciphers = ssl.SSLContext(ssl.PROTOCOL_SSLv23).get_ciphers()
for cipher in ciphers:
	print(cipher['name']+" "+cipher['protocol'])
