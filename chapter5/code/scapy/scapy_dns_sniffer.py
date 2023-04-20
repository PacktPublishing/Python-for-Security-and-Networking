from scapy.all import sniff, DNSQR

number_dns_queries = 0
dns_domains = []
    
def count_dns_request(packet):
	global number_dns_queries
	if DNSQR in packet:
		number_dns_queries += 1
		if packet[DNSQR].qname not in dns_domains:
			dns_domains.append(packet[DNSQR].qname)

def main():
    print("[*] Executing DNS sniffer...")
    print("[*] Stop the program with Ctrl+C and view the results...") 
    try:
        a = sniff(filter="udp and port 53", prn=count_dns_request, count=500)
    except KeyboardInterrupt:
        pass

    print("[*] Sniffer stopped. Showing results")
    print("Number dns queries:",number_dns_queries)
	
    print("[+] Domains:")
    for domain in dns_domains:
    	print(domain.decode())

if __name__ == '__main__':
    main()

