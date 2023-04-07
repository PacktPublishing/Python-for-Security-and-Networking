import zipfile

filename = 'output.zip'
password = 'my_password'

my_file = zipfile.ZipFile(filename)
try:
	my_file.extractall(pwd=bytes(password,'utf-8'))
	print(my_file)
except Exception as exception:
	print("Exception",exception)
