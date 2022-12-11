#!/usr/bin/python
from scapy.all import *
packet=IP(dst='www.python.org')/ICMP()
packet.show()
sendp(packet)

