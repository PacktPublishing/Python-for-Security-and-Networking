#!/usr/bin/env python3

from scapy.all import *

def queryDNS(dnsServer,dominio):
    packet_dns= IP(dst=dnsServer)/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname=dominio))
    response_packet = sr1(packet_dns,verbose=1)
    print(response_packet.show())
    return response_packet[DNS].summary()
    
if __name__ == "__main__":
    print (queryDNS("8.8.8.8","www.python.org"))
