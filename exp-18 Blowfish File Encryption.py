from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad

# Blowfish Key
key = b"SecretKey123"

# Create Blowfish Cipher (ECB Mode)
cipher = Blowfish.new(key, Blowfish.MODE_ECB)

# Read plaintext from input file
with open("input.txt", "rb") as file:
    plaintext = file.read()

# Pad the plaintext
padded_data = pad(plaintext, Blowfish.block_size)

# Encrypt the data
ciphertext = cipher.encrypt(padded_data)

# Save encrypted data
with open("encrypted.bf", "wb") as file:
    file.write(ciphertext)

print("========== Blowfish File Encryption ==========")
print("Input File      : input.txt")
print("Encrypted File  : encrypted.bf")
print("Encryption Successful!")
