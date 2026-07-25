from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad
import binascii

# Plaintext
plaintext = "NETWORKSECURITY"

# Blowfish Key
key = b"SecretKey123"

# Create Blowfish Cipher
cipher = Blowfish.new(key, Blowfish.MODE_ECB)

# Pad plaintext
data = pad(plaintext.encode(), Blowfish.block_size)

# Encrypt
ciphertext = cipher.encrypt(data)

print("========== Blowfish Encryption ==========")
print("Plaintext :", plaintext)
print("Key       :", key.decode())

# Display Ciphertext in Hexadecimal
print("Ciphertext (Hex):")
print(binascii.hexlify(ciphertext).decode())
