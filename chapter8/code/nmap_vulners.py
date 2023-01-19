import subprocess

p = subprocess.Popen(["nmap", "-sV", "--script", "vulners", "scanme.nmap.org", "-p22,80,3306"], stdout=subprocess.PIPE)
(output, err) = p.communicate()
output = output.decode('utf-8').strip()
print(output)
