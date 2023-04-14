#!/usr/bin/python

import pcapy
from struct import *

interfaces = pcapy.findalldevs() 

print("Available interfaces are :") 

for interface in interfaces: 
	print(interface)	

interface = input("Enter interface name to sniff : ") 

cap = pcapy.open_live(interface, 65536, 1, 0)

while True:
    (header,payload) = cap.next()
    l2hdr = payload[:14]
    l2data = unpack("!6s6sH", l2hdr)
    srcmac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (l2hdr[0], l2hdr[1], l2hdr[2], l2hdr[3], l2hdr[4], l2hdr[5])
    dstmac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (l2hdr[6], l2hdr[7], l2hdr[8], l2hdr[9], l2hdr[10],l2hdr[11])
    print("Source MAC: ", srcmac, " Destination MAC: ", dstmac)

	# get IP header from bytes 14 to 34 in payload
    ipheader = unpack('!BBHHHBBH4s4s' , payload[14:34])
    timetolive = ipheader[5]
    protocol = ipheader[6]
    print("Protocol ", str(protocol), " Time To Live: ", str(timetolive))
