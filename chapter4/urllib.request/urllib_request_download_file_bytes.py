import urllib.request, urllib.parse, urllib.error

file_gz = urllib.request.urlopen('http://ftp.debian.org/debian/dists/stable/contrib/Contents-all.gz')
file = open('Contents-all.gz', 'wb')
file_size = 0
while True:
    bytes = file_gz.read(10000)
    if len(bytes) < 1:
    	break
    file_size = file_size + len(bytes)
    file.write(bytes)

print(file_size, 'bytes copied')
file.close()
