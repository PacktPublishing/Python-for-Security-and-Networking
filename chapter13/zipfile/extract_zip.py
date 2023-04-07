import zipfile 
zipfilename = "zipfile.zip" 
password = None 
zf = zipfile.ZipFile(zipfilename, "r") 
try:
	zf.extractall(pwd=password)
except Excception as exception:
	print('Exception', exception) 
zf.close() 
