import requests
import re
import sys

def get_cve_info(query):
    nvd_url = f"https://nvd.nist.gov/vuln/search/results?form_type=Advanced&results_type=overview&query={query}&search_type=all"
    response = requests.get(nvd_url)
    
    if response.status_code == 200:
        html_content = response.text
        cve_ids = re.findall(r'href="/vuln/detail/CVE-(.*?)"', html_content)
        if cve_ids:
            cve_ids.sort()
            print("\nCVEs found for", query, ":")
            for cve_id in cve_ids:
                cve_url = f"https://www.cvedetails.com/cve/CVE-{cve_id}"
                cve_response = requests.get(cve_url)
                if cve_response.status_code == 200:
                    cve_html_content = cve_response.text
                    cve_summary = re.search(r'<div class="cvedetailssummary">(.*?)</div>', cve_html_content, re.DOTALL).group(1)
                    print("\n", cve_id, ":", cve_summary)

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '-h':
        print("\n" 'Usage mode: python cve_search_nvd_database.py <term_search>')
        print('Example: python3 cve_search_nvd_database.py "vsFTPd 2.3.4"\n')
        sys.exit()
    elif len(sys.argv) != 2:
        print("\n" 'Usage mode: python cve_search_nvd_database.py -h for help\n')
        sys.exit()

    query = sys.argv[1]
    get_cve_info(query)
