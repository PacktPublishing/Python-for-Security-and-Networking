from scapy.all import *

host = "45.33.32.156"

for i in range(1, 20):
    packet = IP(dst=host, ttl=i) / UDP(dport=33434)
    # Send the packet and get a reply
    reply = sr1(packet, verbose=0,timeout=1)
    if reply is None:
        pass
    elif reply.type == 3:
        # We've reached our destination
        print("Done!", reply.src)
        break
    else:
        # We're in the middle somewhere
        print("%d hops away: " % i , reply.src)
