import scanless
import json
sl = scanless.Scanless()

print("1.ipfingerprints")
print("2.spiderip")
print("3.standingtech")
print("4.viewdns")
print("5.yougetsignal")
option=int(input("Enter service option:"))

service=''
if option==1: 
	service="ipfingerprints" 
elif option==2: 
	service="spiderip"     
elif option==3: 
	service="standingtech"     
elif option==4: 
	service="viewdns"    
elif option==5: 
	service="yougetsignal" 
	
output = sl.scan('scanme.nmap.org',scanner=service)
print(output['parsed'])
json_output= json.dumps(output,indent=2)
print(json_output)
