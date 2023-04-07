import pyminizip

input = "files/file.txt"
output = "output.zip"
password = "my_password"
compresion_level = 5
 
pyminizip.compress(input, None, output,password, compresion_level)
