from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

# Generate or load your AES key here
key = os.urandom(16)
iv = os.urandom(16)

def encrypt_tflite_model(file_path, encrypted_file_path):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    with open(file_path, 'rb') as file:
        model_data = file.read()
        ciphertext = cipher.encrypt(pad(model_data, AES.block_size))
    
    with open(encrypted_file_path, 'wb') as file:
        file.write(iv + ciphertext)
    
    # Save the AES key to a file
    with open('your_aes_key.bin', 'wb') as f:
        f.write(key)

# Replace 'model.tflite' with your TFLite model file and 'model_encrypted.tflite' with the desired output file
encrypt_tflite_model('model.tflite', 'model_encrypted.tflite')
