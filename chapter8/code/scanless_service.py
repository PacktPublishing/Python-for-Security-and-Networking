import scanless
import json
sl = scanless.Scanless()

print("1.hackertarget")
print("2.ipfingerprints")
print("3.spiderip")
print("4.standingtech")
print("5.viewdns")
print("6.yougetsignal")
option=int(input("Enter service option:"))

service=''
if option==1:
	service="hackertarget"
elif option==2: 
	service="ipfingerprints" 
elif option==3: 
	service="spiderip"     
elif option==4: 
	service="standingtech"     
elif option==5: 
	service="viewdns"    
elif option==6: 
	service="yougetsignal" 
	
output = sl.scan('scanme.nmap.org',scanner=service)
print(output['parsed'])
json_output= json.dumps(output,indent=2)
print(json_output)
