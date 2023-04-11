from cryptography.fernet import Fernet
import os 

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(file, key):
    i = Fernet(key)
    with open(file, "rb") as myfile:
    	file_data = myfile.read()
    	data = i.encrypt(file_data)
    	print("Data encrypted:",data.decode())
    with open("file_encrypted.txt", "wb") as file:
    	file.write(data)

def decrypt_file(file_encrypted, key):
    i = Fernet(key)
    with open(file_encrypted, "rb") as myfile:
    	file_data = myfile.read()
    	data = i.decrypt(file_data)
    	print("Data decrypted:",data.decode())
    	           
if __name__ == '__main__':
	file = 'file.txt'
	file_encrypted = 'file_encrypted.txt'
	key = load_key()
	encrypt_file(file, key)
	decrypt_file(file_encrypted, key)
  
