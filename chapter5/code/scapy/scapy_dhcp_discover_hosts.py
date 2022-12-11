from scapy.all import *

pcap_path = "packets_DHCP.cap"
packets = rdpcap(pcap_path)

for packet in packets:
	try:
		packet.show()
		options = packet[DHCP].options
		#print(options)
		for option in options:
			if option[0] == 'client_id':
				client_id = option[1].decode()
			if option[0] == 'server_id':
				server_id = option[1]
				print('ServerID: {} | ClientID: {}'.format(server_id, client_id))
	except IndexError as error:
		print(error)

