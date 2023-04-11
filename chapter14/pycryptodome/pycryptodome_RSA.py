from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import sys

bit_size = int(sys.argv[1])
key_format = sys.argv[2]
message = sys.argv[3]

key = RSA.generate(bit_size)

print("Generating Public Key....")
publicKey = key.publickey().exportKey(key_format)

print("Generating Private Key....")
privateKey = key.exportKey(key_format)

message = str.encode(message)

RSApublicKey = RSA.importKey(publicKey)
OAEP_cipher = PKCS1_OAEP.new(RSApublicKey)
encryptedMsg = OAEP_cipher.encrypt(message)

print('Encrypted text:', encryptedMsg)

RSAprivateKey = RSA.importKey(privateKey)
OAEP_cipher = PKCS1_OAEP.new(RSAprivateKey)
decryptedMsg = OAEP_cipher.decrypt(encryptedMsg)

print('The original text:', decryptedMsg.decode())


