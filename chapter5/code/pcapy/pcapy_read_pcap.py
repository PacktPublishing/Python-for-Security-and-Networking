#!/usr/bin/python

import pcapy
from struct import *

pcap_file = pcapy.open_offline("packets.pcap")
count = 1

while count<500:
	print("Packet #: ", count)
	count = count + 1
	(header,payload) = pcap_file.next()
	l2hdr = payload[:14]
	l2data = unpack("!6s6sH", l2hdr)
	srcmac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (l2hdr[0], l2hdr[1], l2hdr[2], l2hdr[3], l2hdr[4], l2hdr[5])
	dstmac = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (l2hdr[6], l2hdr[7], l2hdr[8], l2hdr[9], l2hdr[10],l2hdr[11])
	print("Source MAC: ", srcmac, " Destination MAC: ", dstmac)
	ipheader = unpack('!BBHHHBBH4s4s' , payload[14:34])
	timetolive = ipheader[5]
	protocol = ipheader[6]
	print("Protocol ", str(protocol), " Time To Live: ", str(timetolive))
	count = count + 1
