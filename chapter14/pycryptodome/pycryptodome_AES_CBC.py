from Crypto.Cipher import AES 
import binascii,os
import random, string

key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
print('Key:',key)
encryptor = AES.new(key.encode("utf8"), AES.MODE_CBC, 'This is an IV-12'.encode("utf8"))
decryptor = AES.new(key.encode("utf8"), AES.MODE_CBC, 'This is an IV-12'.encode("utf8"))

def aes_encrypt(plaintext):
    ciphertext = encryptor.encrypt(plaintext)
    return ciphertext
    
def aes_decrypt(ciphertext):
    plaintext = decryptor.decrypt(ciphertext)
    return plaintext
    
encrypted = aes_encrypt('This is the secret message      '.encode("utf8"))
decrypted = aes_decrypt(encrypted)
print("Encrypted message :", encrypted)
print("Decrypted message :", decrypted.decode())
