from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import unpad
import binascii

# Blowfish Key
key = b"SecretKey123"

# Ciphertext generated in Experiment 6
cipher_hex = "5d9d7d81d9a81fb4c2eb2e85a5d0d87e"

# Convert Hex to Bytes
ciphertext = binascii.unhexlify(cipher_hex)

# Create Blowfish Cipher
cipher = Blowfish.new(key, Blowfish.MODE_ECB)

# Decrypt
decrypted = cipher.decrypt(ciphertext)

# Remove Padding
plaintext = unpad(decrypted, Blowfish.block_size)

print("========== Blowfish Decryption ==========")
print("Ciphertext (Hex):", cipher_hex)
print("Key             :", key.decode())
print("Recovered Plaintext:", plaintext.decode())
