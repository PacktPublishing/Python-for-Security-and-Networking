import nmap 
import socket

print("-----------" * 6)
print('          Scanner with Nmap: ')
print("-----------" * 6)
domain = input ('Domain: ')
port_range = input ('Port range: ')

ip_address = socket.gethostbyname(domain)

print("-----------" * 6)
print("         Scanning the host with ip address: " + ip_address)
print("-----------" * 6)

nm = nmap.PortScanner()
nm.scan(ip_address, port_range)

for host in nm.all_hosts():
    print("     Host : %s (%s)" % (host,ip_address))
    print("     State : %s" % nm[host].state())

    for protocol in nm[host].all_protocols():
        print("-----------" * 6)
        print("     Protocols : %s" % protocol)

        lport = nm[host][protocol].keys()
        for port in lport:
            print("     Port : %s \t State : %s" %(port, nm[host][protocol][port]['state']))
     
