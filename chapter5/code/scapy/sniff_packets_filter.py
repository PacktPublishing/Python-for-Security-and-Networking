from scapy.all import *
 
if __name__ == '__main__':
	interfaces = get_if_list()
	print(interfaces)
	for interface in interfaces:
		print(interface)
	interface = input("Enter interface name to sniff: ")
	print("Sniffing interface " + interface)
	sniff(iface=interface,filter="tcp and (port 443 or port 80)",
	prn=lambda x:x.sprintf("%.time% %-15s,IP.src% -> %-15s,IP.dst% %IP.chksum% %03xr,IP.proto% %r,TCP.flags%"))
