import zipfile 

zf = zipfile.ZipFile("zipfile.zip", "r") 
print(zf.namelist()) 
zf.close() 
