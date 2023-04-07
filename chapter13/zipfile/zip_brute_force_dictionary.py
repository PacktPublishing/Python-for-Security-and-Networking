import zipfile
import optparse
from threading import Thread

def extract_file(zip_file, password):
	try:
		print(f'[+] Trying password: {password}')
		zip_file.extractall(pwd=password.encode('utf-8'))
		print(f'[+] Found password: {password}')
	except Exception as exception:
		pass

def main(zip_file, dictionary):
    zip_file = zipfile.ZipFile(zip_file)
    with open(dictionary) as passwords_file:
        for line in passwords_file.readlines():
            password = line.strip('\n')
            thread = Thread(target=extract_file, args=(zip_file, password))
            thread.start()

if __name__ == '__main__':
	parser = optparse.OptionParser(usage='zip_crack.py --zipfile <ZIP_FILE> --dictionary <DICTIONARY_FILE>')
	parser.add_option('--zipfile', dest='zipfile',help='zip file')
	parser.add_option('--dictionary', dest='dictionary',help='dictionary file with possible passwords')
	(options, args) = parser.parse_args()
	if (options.zipfile == None) | (options.dictionary == None):
		print(parser.usage)
	else:
		main(options.zipfile, options.dictionary)
