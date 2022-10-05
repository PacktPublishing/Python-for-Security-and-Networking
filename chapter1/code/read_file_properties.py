#!/usr/bin/python3

file_descryptor = open("read_file_properties.py", "r+") 
print("Content: "+file_descryptor.read())
print("Name: "+file_descryptor.name)
print("Mode: "+file_descryptor.mode)
print("Encoding: "+str(file_descryptor.encoding))
file_descryptor.close() 
