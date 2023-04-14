#!/usr/bin/python
from scapy.all import *
packet=Ether()/IP(dst='www.python.org')/TCP(dport=80,flags="S")
packet.show()
srp1(packet,timeout = 10)

