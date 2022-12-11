#!/usr/bin/python

import pcapy
import datetime

interfaces = pcapy.findalldevs()
     
print("Available interfaces are:")
for interface in interfaces:
	print(interface)
     
interface = input("Enter interface name to sniff: ")
print("Sniffing interface " + interface)

#  device, # of byte to capture per packet, promiscuous mode, timeout (ms)
cap = pcapy.open_live(interface, 65536 , 1 , 0)

while True:
    (header, payload) = cap.next()
    print ('%s: captured %d bytes' %(datetime.datetime.now(), header.getlen()))
