import requests
import random
import sys

target = input("Enter target URL: ")
payloads = 'payloads.txt'

user_agent = ['Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991',
'Mozilla/5.0 (Linux; U; Android 4.2.2; en-us; A1-810 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30',
'Mozilla/5.0 (Windows NT 5.1; rv:52.0) Gecko/20100101 Firefox/52.0',
'Mozilla/5.0 (PLAYSTATION 3 4.81) AppleWebKit/531.22.8 (KHTML, like Gecko)',
'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.52',
'Mozilla/5.0 (SMART-TV; X11; Linux armv7l) AppleWebKit/537.42 (KHTML, like Gecko) Chromium/25.0.1349.2 Chrome/25.0.1349.2 Safari/537.42',
'Mozilla/5.0 (Windows NT 6.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/601.2.7 (KHTML, like Gecko)',
'Mozilla/5.0 (PlayStation 4 5.01) AppleWebKit/601.2 (KHTML, like Gecko)']

header = {'User-Agent': random.choice(user_agent)}

def test_open_redirect():
	print('Loading Payloads: ' + payloads)
	f = open(payloads,'r')
	for line in f.readlines():
		payload = line.strip('\n')
		try:
			final = target+"/"+payload
			print(final)
			response = requests.get(final,headers=header)
			for resp in response.history:
				print(resp.status_code)
				if resp.status_code == 302 or resp.status_code == 301:
					print(resp.status_code, resp.url + " [!] Vulnerable to Open Redirect")
				else:
					print(resp.url  + '[-]Not Vulnerable')
		except Exception as e:
			print ("Invalid URL:"+str(e))
			sys.exit()
		except IOError:
			print(IOError)
		
test_open_redirect()
