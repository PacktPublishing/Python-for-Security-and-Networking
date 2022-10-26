import os

extensions = ['.jpeg','.jpg','.txt','.py']

for extension in extensions:
	print("Files with extension ",extension)
	for path,folder,files in os.walk("."):
		for file in files:
			if file.endswith(extension):
				print(os.path.join(path,file))
