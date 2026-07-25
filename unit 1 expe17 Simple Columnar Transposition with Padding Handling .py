# Q7: Simple Columnar Transposition with Padding Handling

import math

# ---------------- Encryption ----------------
def encrypt(plaintext, key_length, pad_char):

    plaintext = plaintext.replace(" ", "").upper()

    rows = math.ceil(len(plaintext) / key_length)

    # Padding
    while len(plaintext) < rows * key_length:
        plaintext += pad_char

    # Create Matrix
    matrix = []

    index = 0
    for i in range(rows):
        row = []
        for j in range(key_length):
            row.append(plaintext[index])
            index += 1
        matrix.append(row)

    print("\nRow-wise Matrix:")
    for row in matrix:
        print(" ".join(row))

    # Read Column-wise
    ciphertext = ""

    for col in range(key_length):
        for row in range(rows):
            ciphertext += matrix[row][col]

    return ciphertext


# ---------------- Decryption ----------------
def decrypt(ciphertext, key_length, pad_char):

    rows = math.ceil(len(ciphertext) / key_length)

    matrix = [['' for _ in range(key_length)] for _ in range(rows)]

    index = 0

    # Fill Column-wise
    for col in range(key_length):
        for row in range(rows):
            matrix[row][col] = ciphertext[index]
            index += 1

    print("\nDecryption Matrix:")
    for row in matrix:
        print(" ".join(row))

    # Read Row-wise
    plaintext = ""

    for row in matrix:
        plaintext += "".join(row)

    # Remove Padding
    plaintext = plaintext.rstrip(pad_char)

    return plaintext


# ---------------- Main ----------------

plaintext = input("Enter Plaintext: ")
key_length = int(input("Enter Numeric Key Length: "))
pad_char = input("Enter Padding Character: ")

cipher = encrypt(plaintext, key_length, pad_char)

plain = decrypt(cipher, key_length, pad_char)

print("\n========== Simple Columnar Transposition ==========")
print("Plaintext :", plaintext.upper())
print("Ciphertext:", cipher)
print("Decrypted :", plain)
