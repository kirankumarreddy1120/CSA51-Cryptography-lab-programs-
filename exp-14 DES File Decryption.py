from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad

# DES key (same key used during encryption)
key = b'A1B2C3D4'

# Create DES cipher in ECB mode
cipher = DES.new(key, DES.MODE_ECB)

# Read encrypted file
with open("encrypted.des", "rb") as file:
    ciphertext = file.read()

# Decrypt the data
decrypted_data = cipher.decrypt(ciphertext)

# Remove padding
plaintext = unpad(decrypted_data, DES.block_size)

# Save decrypted text
with open("decrypted.txt", "wb") as file:
    file.write(plaintext)

print("========== DES File Decryption ==========")
print("Encrypted File : encrypted.des")
print("Output File    : decrypted.txt")
print("Decryption Successful!")

# Display decrypted content
print("\nRecovered Plaintext:\n")
print(plaintext.decode())
