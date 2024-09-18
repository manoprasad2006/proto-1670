from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import os

def encrypt_aes_key(aes_key, public_key_path):
    with open(public_key_path, 'rb') as f:
        public_key = RSA.import_key(f.read())
    
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_key = cipher.encrypt(aes_key)
    
    with open('your_aes_key.bin', 'wb') as f:
        f.write(encrypted_key)

# Generate AES key
aes_key = os.urandom(16)  # 16 bytes for AES-128

# Replace 'public.pem' with the path to your RSA public key file
encrypt_aes_key(aes_key, 'public.pem')
