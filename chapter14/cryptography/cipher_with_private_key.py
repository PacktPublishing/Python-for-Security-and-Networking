from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

plaintext = b'a secret message'
padding_config = padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None)

with open('private_key.pem', 'rb') as private_key:
	private_key = serialization.load_pem_private_key(private_key.read(),password=None,backend=default_backend())

with open('public_key.pem', 'rb') as public_key:
	public_key = serialization.load_pem_public_key(public_key.read(),backend=default_backend())

ciphertext_with_public_key = public_key.encrypt(plaintext=plaintext,padding=padding_config)
decrypted_with_private_key = private_key.decrypt(ciphertext=ciphertext_with_public_key,padding=padding_config)

print("Encrypted message:",ciphertext_with_public_key)
print("Decrypted message:",decrypted_with_private_key)
print("Plain text:",plaintext.decode())
print(decrypted_with_private_key == plaintext)
