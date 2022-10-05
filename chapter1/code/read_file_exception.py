#!/usr/bin/python3

try:
    file_handle = open("myfile.txt", "r")
except IOError as exception:
    print("Exception IOError: Unable to read from myfile ", exception)
except Exception as exception:
    print("Exception: ", exception)
else:
    print("File read successfully")
    file_handle.close()
