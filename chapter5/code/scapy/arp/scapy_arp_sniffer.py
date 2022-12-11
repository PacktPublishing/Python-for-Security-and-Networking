import scapy.all as scapy
 
 # Implementing ARP Spoof Attack Detection Using Scapy
  
def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def get_mac_address(ip_address):
	broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_request = ARP(pdst=ip_address)
	arp_request_broadcast = broadcast / arp_request
	answered_list = srp(arp_request_broadcast,timeout=1,verbose=False)
	return answered_list[0][0][1].hwsrc
  
def process_sniffed_packet(packet):
	if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
		originalmac = get_mac_address(packet[scapy.ARP].psrc)
		responsemac = packet[scapy.ARP].hwsrc
		if originalmac != responsemac:
			print("[*] ALERT!!! You are under attack, ARP table is being poisoned.!")
			
if __name__ == '__main__':
	sniff("wlo1")
