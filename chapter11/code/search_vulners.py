import vulners

vulners_api = vulners.Vulners(api_key="API_KEY")

openssl = vulners_api.find_all(query="openssl", limit=5)
for i, val in enumerate(openssl):
	for key,value in val.items():
		print(key,":",value)


#Get information about document by identifier
CVE_2023_001 = vulners_api.document("CVE-2023-0001")
for key,value in CVE_2023_001.items():
	print(key,":",value)


#Get references for the vulnerability
references = vulners_api.get_bulletin_references("CVE-2023-0001")
for key,value in references.items():
	for key,val in enumerate(value):
		for key,value in val.items():
			print(key,":",value)


	
