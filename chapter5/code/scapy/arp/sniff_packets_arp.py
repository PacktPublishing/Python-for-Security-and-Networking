from scapy.all import *

def arpDisplay(packet):
	if packet.haslayer(ARP):
		if packet[ARP].op == 1: #request
			print("Request: {} is asking about {} ".format(packet[ARP].psrc,packet[ARP].pdst))
		if packet[ARP].op == 2: #response
			print("Response: {} has MAC address {}".format(packet[ARP].hwsrc,packet[ARP].psrc))

sniff(iface="wlo1",prn=arpDisplay, filter="arp", store=0, count=10)
