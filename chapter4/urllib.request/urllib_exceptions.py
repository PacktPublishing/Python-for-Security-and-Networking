#!/usr/bin/env python3

import urllib.error

from urllib.request import urlopen

try:
	urlopen('https://www.ietf.org/rfc/rfc0.txt')
	
except urllib.error.HTTPError as exception:
	print('Exception:', exception)
	print('Status:', exception.code)
	print('Reason', exception.reason)
	print('Url', exception.url)
