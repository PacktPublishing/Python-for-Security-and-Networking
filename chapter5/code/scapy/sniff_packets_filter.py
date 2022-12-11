from scapy.all import *
 
if __name__ == '__main__':
	sniff(iface="wlo1",filter="tcp and (port 443 or port 80)",
	prn=lambda x:x.sprintf("%.time% %-15s,IP.src% -> %-15s,IP.dst% %IP.chksum% %03xr,IP.proto% %r,TCP.flags%"))
