#!/usr/bin/env python3

import urllib.request
from urllib.request import Request

def chrome_user_agent(domain, USER_AGENT):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', USER_AGENT)]
    urllib.request.install_opener(opener)
    response = urllib.request.urlopen(domain)
    print("Response headers")
    print("--------------------")
    for header,value in response.getheaders():
        print(header + ":" + value)

    request = Request(domain)
    request.add_header('User-agent', USER_AGENT)
    print("\nRequest headers")
    print("--------------------")
    for header,value in request.header_items():
	    print(header + ":" + value)

if __name__ == '__main__':
	domain = "http://python.org"
	USER_AGENT = 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36'
	chrome_user_agent(domain, USER_AGENT)
