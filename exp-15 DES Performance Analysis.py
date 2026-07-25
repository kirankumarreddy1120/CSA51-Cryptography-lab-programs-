import os
import time
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# DES Key (8 bytes)
key = b'A1B2C3D4'

# Create DES Cipher
cipher = DES.new(key, DES.MODE_ECB)

# File sizes to test
sizes = {
    "1 KB": 1024,
    "10 KB": 10 * 1024,
    "100 KB": 100 * 1024,
    "1 MB": 1024 * 1024
}

print("=" * 65)
print("{:<10} {:<20} {:<20}".format("File Size", "Encryption Time(s)", "Decryption Time(s)"))
print("=" * 65)

for name, size in sizes.items():

    # Generate random data
    data = os.urandom(size)

    # Padding
    padded_data = pad(data, DES.block_size)

    # Encryption Timing
    start = time.perf_counter()
    encrypted = cipher.encrypt(padded_data)
    encryption_time = time.perf_counter() - start

    # Decryption Timing
    start = time.perf_counter()
    decrypted = unpad(cipher.decrypt(encrypted), DES.block_size)
    decryption_time = time.perf_counter() - start

    print("{:<10} {:<20.6f} {:<20.6f}".format(
        name,
        encryption_time,
        decryption_time
    ))
