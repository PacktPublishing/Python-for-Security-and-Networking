import ssl
address = ('python.org', 443)
certificate = ssl.get_server_certificate(address)
print(certificate)
