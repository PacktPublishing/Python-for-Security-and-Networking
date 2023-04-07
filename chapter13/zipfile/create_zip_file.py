import os
import zipfile

zf = zipfile.ZipFile("zipfile.zip", "w")
for dirname, subdirs, files in os.walk('files', topdown=False):
    for filename in files:
    	print(filename)
    	zf.write(os.path.join(dirname, filename))
zf.close()
