import os
file_count = 0 
for currentdir, dirnames, filenames in os.walk('.'): 
	file_count += len(filenames) 
print("The number of files in current directory are:",file_count) 
