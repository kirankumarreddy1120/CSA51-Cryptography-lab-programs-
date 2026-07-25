import os
import time
import psutil

from Crypto.Cipher import DES, Blowfish
from Crypto.Util.Padding import pad, unpad

# ---------------------------
# Keys
# ---------------------------
des_key = b"A1B2C3D4"
blowfish_key = b"SecretKey123"

# ---------------------------
# File Sizes
# ---------------------------
sizes = {
    "1 KB": 1024,
    "10 KB": 10 * 1024,
    "100 KB": 100 * 1024,
    "1 MB": 1024 * 1024
}

process = psutil.Process()

print("=" * 95)
print("{:<8} {:<12} {:<12} {:<12} {:<12} {:<12} {:<10}".format(
    "Size",
    "Algorithm",
    "Enc Time",
    "Dec Time",
    "Memory(KB)",
    "Cipher Size",
    "Status"
))
print("=" * 95)

for name, size in sizes.items():

    data = os.urandom(size)

    # ================= DES ===================
    des_cipher = DES.new(des_key, DES.MODE_ECB)

    padded = pad(data, DES.block_size)

    mem_before = process.memory_info().rss

    start = time.perf_counter()
    des_ciphertext = des_cipher.encrypt(padded)
    enc_time = time.perf_counter() - start

    start = time.perf_counter()
    decrypted = unpad(des_cipher.decrypt(des_ciphertext), DES.block_size)
    dec_time = time.perf_counter() - start

    mem_after = process.memory_info().rss

    print("{:<8} {:<12} {:<12.6f} {:<12.6f} {:<12.2f} {:<12} {}".format(
        name,
        "DES",
        enc_time,
        dec_time,
        (mem_after - mem_before) / 1024,
        len(des_ciphertext),
        "Success"
    ))

    # =============== Blowfish =================
    blow_cipher = Blowfish.new(blowfish_key, Blowfish.MODE_ECB)

    padded = pad(data, Blowfish.block_size)

    mem_before = process.memory_info().rss

    start = time.perf_counter()
    blow_ciphertext = blow_cipher.encrypt(padded)
    enc_time = time.perf_counter() - start

    start = time.perf_counter()
    decrypted = unpad(blow_cipher.decrypt(blow_ciphertext), Blowfish.block_size)
    dec_time = time.perf_counter() - start

    mem_after = process.memory_info().rss

    print("{:<8} {:<12} {:<12.6f} {:<12.6f} {:<12.2f} {:<12} {}".format(
        "",
        "Blowfish",
        enc_time,
        dec_time,
        (mem_after - mem_before) / 1024,
        len(blow_ciphertext),
        "Success"
    ))

    print("-" * 95)
