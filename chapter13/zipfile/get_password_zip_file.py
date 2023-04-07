import zipfile

filename = 'output.zip'
dictionary = 'password_list.txt'

my_file = zipfile.ZipFile(filename)
with open(dictionary, 'r') as f:
	for line in f.readlines():
		password = line.strip('\n')
		try:
			my_file.extractall(pwd=bytes(password,'utf-8'))
			print('Password found: %s' % password)
		except Exception as exception:
			print("Trying password:%s Exception:%s" % (password,exception))
