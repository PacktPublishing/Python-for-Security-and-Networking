#!/usr/bin/python3

def contains(dictionary,item):
	for key,value in dictionary.items():
		if value == item:
			return True
	return False 

dictionary = {1:100,2:200,3:300}
print(contains(dictionary,200))
print(contains(dictionary,300))
print(contains(dictionary,350))
