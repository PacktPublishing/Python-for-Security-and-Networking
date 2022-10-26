import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import time

url_list = ["http://www.python.org","http://www.google.com","http://www.packtpub.com","http://www.goooooooogle.com"]

def request_url(url):
    html = requests.get(url, stream=True)
    return url + "-->" + str(html.status_code)

process_list = []
with ThreadPoolExecutor(max_workers=10) as executor:
    for url in url_list:
        process_list.append(executor.submit(request_url, url))

for task in as_completed(process_list):
    print(task.result())
