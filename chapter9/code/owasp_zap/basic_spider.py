#!/usr/bin/env python
import time
from zapv2 import ZAPv2

apiKey='<YOUR_API_KEY>'

target = 'http://testphp.vulnweb.com/'
zap = ZAPv2(apikey=apiKey)

print('Spidering target {}'.format(target))
scanID = zap.spider.scan(target)
while int(zap.spider.status(scanID)) < 100:
    print('Spider progress %: {}'.format(zap.spider.status(scanID)))
    time.sleep(1)

print('Spider has completed!')
print('\n'.join(map(str, zap.spider.results(scanID))))
