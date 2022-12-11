from scapy.all import *

def count_dns_request(packet):
	if DNSQR in packet:
		print(packet.summary())
		print(packet.show())
		
sniff(filter="udp and port 53",prn=count_dns_request,count=100)

