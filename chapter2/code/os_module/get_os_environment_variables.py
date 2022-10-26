#!/usr/bin/python3
import os

print(os.getcwd())
print(os.getuid())
print(os.getenv("PATH"))
print(os.environ)
for environ in os.environ:
	print(environ)

for key, value in os.environ.items():
	print(key,value)




                   
            
    
