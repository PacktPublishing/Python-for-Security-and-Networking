#!/usr/bin/python3

protocolList = ["FTP", "HTTP", "SNMP", "SSH"]
element_to_find = "SSH"
for i in range(len(protocolList)):
    if element_to_find in protocolList[i]:
    	print("Element found at index", i)
    	break
