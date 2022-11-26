import urllib.request, urllib.parse, urllib.error

file_gz = urllib.request.urlopen('http://ftp.debian.org/debian/dists/stable/contrib/Contents-all.gz').read()
file = open('Contents-all.gz', 'wb')
file.write(file_gz)
file.close()
