import time
from zapv2 import ZAPv2

target = 'http://testphp.vulnweb.com/'

zap = ZAPv2()

print('Ajax Spider target {}'.format(target))
scanID = zap.ajaxSpider.scan(target)

timeout = time.time() + 60*2
while zap.ajaxSpider.status == 'running':
    if time.time() > timeout:
        break
    print('Ajax Spider status:' + zap.ajaxSpider.status)
    time.sleep(2)

print('Ajax Spider completed')
ajaxResults = zap.ajaxSpider.results(start=0, count=10)
print(ajaxResults)
