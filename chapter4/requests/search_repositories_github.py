#!/usr/bin/env python

# python search_repositories_github.py --author packt --search_for book

SEARCH_URL_BASE = 'https://api.github.com/users'

import argparse
import requests
import json

def search_repository(author, search_for='homepage'):
    url = "%s/%s/repos" %(SEARCH_URL_BASE, author)
    print("Searching Repo URL: %s" %url)
    result = requests.get(url)
    results=[]
    if(result.ok):
        repo_info = json.loads(result.text or result.content)
        result = "No result found!"
        for repo in repo_info:
        	for key,value in repo.items():
        		if  search_for in str(value):
        			results.append(value)
        return results
            

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Github search')
    parser.add_argument('--author', action="store", dest="author", required=True)
    parser.add_argument('--search_for', action="store", dest="search_for", required=True)
    
    given_args = parser.parse_args() 
    results = search_repository(given_args.author, given_args.search_for)
    if isinstance(results, list):
        print("Got result for '%s'..." %(given_args.search_for))
        for value in results:
            print("%s" %(value))
    else:
        print("Got result for %s: %s" %(given_args.search_for, result))

