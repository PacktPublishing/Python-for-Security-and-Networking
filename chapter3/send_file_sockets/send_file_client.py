import os
import socket
import struct

def send_file(sock: socket.socket, filename):
    filesize = os.path.getsize(filename)
    sock.sendall(struct.pack("<Q", filesize))
    with open(filename, "rb") as f:
        while read_bytes := f.read(1024):
            sock.sendall(read_bytes)

with socket.create_connection(("localhost", 9999)) as connection:
    print("Connecting with the server...")
    print("Sending file...")
    send_file(connection, "send_file_client.py")
    print("File sended")

