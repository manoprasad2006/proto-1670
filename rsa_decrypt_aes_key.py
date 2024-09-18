from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

def decrypt_aes_key(encrypted_key_path, private_key_path):
    with open(private_key_path, 'rb') as f:
        private_key = RSA.import_key(f.read())
    
    cipher = PKCS1_OAEP.new(private_key)
    
    with open(encrypted_key_path, 'rb') as f:
        encrypted_key = f.read()
    
    aes_key = cipher.decrypt(encrypted_key)
    return aes_key

# Replace 'aes_key_encrypted.bin' with your encrypted AES key file and 'private.pem' with the path to your RSA private key file
aes_key = decrypt_aes_key('your_aes_key.bin', 'private.pem')
