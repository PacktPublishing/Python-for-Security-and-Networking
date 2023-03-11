import urllib.request, json, sys, textwrap
import argparse

def cveSearch(cve):
    with urllib.request.urlopen('http://cve.circl.lu/api/cve/'+cve) as url:
        data = json.loads(url.read().decode())
        try:
            if data['cvss']:
                print("{} | CVSS {}".format(cve,data['cvss']))
            if data['summary']:
                print('+-- Summary '+'-'*68+"\n")
                print('\n'.join(textwrap.wrap(data['summary'],80)))
            if data['exploit-db']:
                print('+-- ExploitDB '+'-'*66)
                for d in data['exploit-db']:
                    print("| Title | {}".format(d['title']))
                    print("|   URL | {}".format(d['source']))
                    print("+-------+"+"-"*71)
        except (TypeError, KeyError) as e:
            pass

def gitHubSearch(cve):
    with urllib.request.urlopen('https://api.github.com/search/repositories?q='+cve) as url:
        data = json.loads(url.read().decode())
        try:
            print('GitHub Repositories:')
            for i in data['items']:
                print("|  Repository | {}".format(i['full_name']))
                print("|  Description | {}".format(i['description']))
                print("|   URL | {}".format(i['html_url']))
                print("---------------------------------------------")
        except (TypeError, KeyError) as e:
            pass
 
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Tool to search CVE information")
	parser.add_argument("--cve", help="CVE ID",default="")
	args = parser.parse_args()
	cveSearch(args.cve)
	gitHubSearch(args.cve)

