#!/usr/bin/env python3

import socket
from geoip import geolite2
import argparse
import json

# Setup commandline arguments
parser = argparse.ArgumentParser(description='Get IP Geolocation info')
parser.add_argument('--hostname', action="store", dest="hostname", required=True)

# Parse arguments
given_args = parser.parse_args()
hostname = given_args.hostname
ip_address = socket.gethostbyname(hostname)

print("IP address: {0}".format(ip_address))

geolocation = geolite2.lookup(ip_address)

if geolocation is not None:
	print('Country: ',geolocation.country)
	print('Time zone: ', geolocation.timezone)
	print('Location: ', geolocation.location)
