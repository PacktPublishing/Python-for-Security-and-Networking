import re
import requests 
import sys
import os
import argparse
import time
import optparse

def main():
	pars = optparse.OptionParser(description="[*] Discover hidden files and directories")
	pars.add_option('-u', '--url',action="store", dest="url", type="string", help=" URL of the Target",default=None)
	pars.add_option('-w', '--wordlist',action="store", type="string", dest="wordlist", help="Custom wordlist",default=None)

	opts, args = pars.parse_args()

	if not opts.url:
		print("usage : python myFuzzer.py -h")	
	if opts.wordlist:
		if not os.path.isfile(str(opts.wordlist)):
			print("[!] Please checkout your Custom wordlist path")			
			sys.exit(0)
	fuzz(opts.url,opts.wordlist)	

def ok_results(results):
	
	print("200 Ok results")
	print("---------------")
	for result in results:
		print("[+] -[200] -"+result)

def fuzz(url,CustomWordlist):
	results = []
	if CustomWordlist :
		words = [w.strip() for w in open(str(CustomWordlist), "rb").readlines()]
	else :
		words = [w.strip() for w in open(wordlists["dict"], "rb").readlines()]
	try:
		if not url.startswith('http://'):
			url ="http://"+url
		for paths in words:
			paths = paths.decode()
			if not paths.startswith('/'):
				paths ="/"+paths			
			fullPath = url+paths
			print(fullPath)
			response = requests.get(fullPath)
			code = str(response.status_code)
			print("[+] [{time}] - [{code}] - [{paths}] -> {fullPath}".format(time=time.strftime("%H:%M:%S"),code=code,paths=paths,fullPath=fullPath))  
			if code == "200":
				results.append(fullPath)
		ok_results(results)		
	except Exception as e:
		print("ERROR =>",e)

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt as err:
		sys.exit(0)
