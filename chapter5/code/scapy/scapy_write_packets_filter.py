from scapy.all import *

def sniffPackets(packet):
	if packet.haslayer(IP):
		ip_layer = packet.getlayer(IP)
		packet_src=ip_layer.src
		packet_dst=ip_layer.dst
		print("[+] New Packet: {src} -> {dst}".format(src=packet_src, dst=packet_dst))

if __name__ == '__main__':
	interfaces = get_if_list()
	print(interfaces)
	for interface in interfaces:
		print(interface)
	interface = input("Enter interface name to sniff: ")
	print("Sniffing interface " + interface)
	packets = sniff(iface=interface,filter="tcp and (port 443 or port 80)",prn=sniffPackets,count=100)
	wrpcap('packets.pcap',packets) 


