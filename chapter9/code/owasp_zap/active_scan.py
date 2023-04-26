#!/usr/bin/env python
import time
from zapv2 import ZAPv2

apiKey='<YOUR_API_KEY>'

target = 'http://testphp.vulnweb.com/'
zap = ZAPv2(apikey=apiKey)

print('Accessing target {}'.format(target))
zap.urlopen(target)
time.sleep(2)

print('Active Scanning target {}'.format(target))
scanID = zap.ascan.scan(target)
while int(zap.ascan.status(scanID)) < 100:
    print('Scan progress %: {}'.format(zap.ascan.status(scanID)))
    time.sleep(5)

print('Active Scan completed')

with open("report.html", "w") as report_file:report_file.write(zap.core.htmlreport())

print('Hosts: {}'.format(', '.join(zap.core.hosts)))
print('Alerts: ')
print(zap.core.alerts(baseurl=target))

