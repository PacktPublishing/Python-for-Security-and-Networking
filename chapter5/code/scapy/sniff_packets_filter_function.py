from scapy.all import *

def sniffPackets(packet):
	if packet.haslayer(IP):
		ip_layer = packet.getlayer(IP)
		packet_src=ip_layer.src
		packet_dst=ip_layer.dst
		print("[+] New Packet: {src} -> {dst}".format(src=packet_src, dst=packet_dst))

if __name__ == '__main__':
	sniff(iface="wlo1",filter="tcp and (port 443 or port 80)",prn=sniffPackets)


