from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

key = os.urandom(16)  # 16 bytes key for AES-128
iv = os.urandom(16)   # 16 bytes IV for AES

def encrypt_tflite_model(file_path, encrypted_file_path):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    with open(file_path, 'rb') as file:
        model_data = file.read()
        ciphertext = cipher.encrypt(pad(model_data, AES.block_size))
    
    with open(encrypted_file_path, 'wb') as file:
        file.write(iv + ciphertext)
        
# Replace 'model.tflite' with your TFLite model file and 'model_encrypted.tflite' with the desired output file
encrypt_tflite_model('tflite_model.tflite', 'model_encrypted.tflite')
