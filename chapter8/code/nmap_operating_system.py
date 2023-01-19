import nmap, sys

command="nmap_operating_system.py  <IP_address>"

if len(sys.argv) == 1:
    print(command)
    sys.exit()

host = sys.argv[1]
	
portScanner = nmap.PortScanner()
open_ports_dict =  portScanner.scan(host, arguments="-O -v")

if open_ports_dict is not None:
    open_ports_dict = open_ports_dict.get("scan").get(host).get("tcp")

    print("Open port-->Service")
    port_list = open_ports_dict.keys()
    for port in port_list:
        print(port, "-->",open_ports_dict.get(port)['name'])

    print("\n--------------Operating System details---------------------\n")
    print("Details about the scanned host are: \t", portScanner[host]['osmatch'][0]['osclass'][0]['cpe'])
    print("Operating system family is: \t\t", portScanner[host]['osmatch'][0]['osclass'][0]['osfamily'])
    print("Type of OS is: \t\t\t\t", portScanner[host]['osmatch'][0]['osclass'][0]['type']) 
    print("Generation of Operating System :\t", portScanner[host]['osmatch'][0]['osclass'][0]['osgen'])
    print("Operating System Vendor is:\t\t", portScanner[host]['osmatch'][0]['osclass'][0]['vendor'])
    print("Accuracy of detection is:\t\t", portScanner[host]['osmatch'][0]['osclass'][0]['accuracy'])
