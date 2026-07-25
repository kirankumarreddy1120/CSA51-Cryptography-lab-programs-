from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

# DES key (8 bytes)
key = b'A1B2C3D4'

# Create DES cipher in ECB mode
cipher = DES.new(key, DES.MODE_ECB)

# Read plaintext from file
with open("input.txt", "rb") as file:
    plaintext = file.read()

# Pad the plaintext to make it a multiple of 8 bytes
padded_text = pad(plaintext, DES.block_size)

# Encrypt the data
ciphertext = cipher.encrypt(padded_text)

# Save encrypted data
with open("encrypted.des", "wb") as file:
    file.write(ciphertext)

print("========== DES File Encryption ==========")
print("Input File      : input.txt")
print("Encrypted File  : encrypted.des")
print("Encryption Successful!")
