#!/usr/bin/python3

try:
    countlines = countchars = 0
    file = open('count_lines_chars.py', 'r')
    lines = file.readlines()
    for line in lines:
        countlines += 1
        for char in line:
            countchars += 1
    file.close()
    print("Characters in file:", countchars)
    print("Lines in file:", countlines)
except IOError as error:
    print("I/O error occurred:", str(error))
