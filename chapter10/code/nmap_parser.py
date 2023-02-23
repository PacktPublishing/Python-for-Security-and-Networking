from libnmap.parser import NmapParser
p = NmapParser.parse_fromfile("results.xml")
for host in p.hosts:
	for svc in host.services:
		for script in svc.scripts_results:
			output = script.get("output")
			print(output)
