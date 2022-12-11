from scapy.all import *

target = sys.argv[1]
port = int(sys.argv[2])

ans,unans = sr(IP(dst=target)/TCP(dport=port,flags="S"))
ans.summary()	
