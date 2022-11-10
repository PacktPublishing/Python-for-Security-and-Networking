import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('ftp.debian.org', 80))
cmd = 'GET http://ftp.debian.org/debian/README.mirrors.txt HTTP/1.0\r\n\r\n'.encode()
sock.send(cmd)

while True:
    data = sock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

sock.close()
