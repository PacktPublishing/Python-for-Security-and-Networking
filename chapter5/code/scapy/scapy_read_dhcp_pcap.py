from scapy.all import *
from collections import Counter
from prettytable import PrettyTable

packets = rdpcap('packets_DHCP.cap')
srcIP=[]
for packet in packets:
	if IP in packet:
		try:
			srcIP.append(packet[IP].src)
		except:
			pass
counter=Counter()
for ip in srcIP:
	counter[ip] += 1
table= PrettyTable(["IP", "Count"])
for ip, count in counter.most_common():
   table.add_row([ip, count])
print(table)
