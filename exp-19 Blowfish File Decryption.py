from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import unpad

# Blowfish Key (Same key used during encryption)
key = b"SecretKey123"

# Create Blowfish Cipher (ECB Mode)
cipher = Blowfish.new(key, Blowfish.MODE_ECB)

# Read encrypted file
with open("encrypted.bf", "rb") as file:
    ciphertext = file.read()

# Decrypt the data
decrypted_data = cipher.decrypt(ciphertext)

# Remove padding
plaintext = unpad(decrypted_data, Blowfish.block_size)

# Save decrypted data
with open("decrypted.txt", "wb") as file:
    file.write(plaintext)

print("========== Blowfish File Decryption ==========")
print("Encrypted File : encrypted.bf")
print("Output File    : decrypted.txt")
print("Decryption Successful!")

print("\nRecovered Plaintext:\n")
print(plaintext.decode())
