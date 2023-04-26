#!/usr/bin/env python
import time
from pprint import pprint
from zapv2 import ZAPv2

apiKey='<YOUR_API_KEY>'

target = 'http://testphp.vulnweb.com/'
zap = ZAPv2(apikey=apiKey)

print('Accessing target {}'.format(target))
zap.urlopen(target)
time.sleep(2)

print('Spidering target {}'.format(target))
scanid = zap.spider.scan(target)
time.sleep(2)

while (int(zap.spider.status(scanid)) < 100):
    print('Spider progress %: {}'.format(zap.spider.status(scanid)))
    time.sleep(2)

while (int(zap.pscan.records_to_scan) > 0):
      print ('Records to passive scan : {}'.format(zap.pscan.records_to_scan))
      time.sleep(2)

with open("report.html", "w") as report_file:report_file.write(zap.core.htmlreport())
      
print('Passive Scan completed')
print('Hosts: {}'.format(', '.join(zap.core.hosts)))
print('Alerts: ')
print(zap.core.alerts())

