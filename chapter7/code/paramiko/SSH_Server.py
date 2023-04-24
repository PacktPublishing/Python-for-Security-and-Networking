import socket, paramiko, threading, sys 
import getpass
if len(sys.argv) != 3: 
    print("usage SSH_Server.py <interface> <port>") 
    exit() 
    
class SSH_Server (paramiko.ServerInterface): 
   def check_channel_request(self, kind, chanid): 
       if kind == 'session': 
           return paramiko.OPEN_SUCCEEDED 
       return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED 
   def check_auth_password(self, username, password): 
       if (username == 'linux') and (password == 'linux'): 
           return paramiko.AUTH_SUCCESSFUL 
       return paramiko.AUTH_FAILED 
 
try: 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    sock.bind((sys.argv[1], int(sys.argv[2]))) 
    sock.listen(100) 
    print('[+] Listening on port ',str(sys.argv[2])) 
    client, addr = sock.accept() 
    print("Input connection")
    transport = paramiko.Transport(client) 
    transport.load_server_moduli() 
    server_key = paramiko.RSAKey(filename='/home/linux/.ssh/id_rsa') 
    key_password = getpass.getpass(prompt='Enter password for RSA key file: ')
    server_key.from_private_key_file('/home/linux/.ssh/id_rsa', password=key_password)
    transport.add_server_key(server_key)
    server = SSH_Server() 
    transport.start_server(server=server) 
    channel = transport.accept(20) 
    print((channel.recv(1024).decode())) 
    channel.send('SSH Connection Established!') 
    while True: 
        command= input(">: ").strip('n') 
        if command.lower() == 'exit': 
            print("Closing connection...") 
            channel.send('exit') 
            break 
        channel.send(command) 
        print((channel.recv(1024).decode()))
except Exception as exception: 
    print(('[-] Excepción: ' + str(exception))) 
