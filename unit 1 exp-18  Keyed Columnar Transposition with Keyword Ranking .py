# Q8: Keyed Columnar Transposition with Keyword Ranking

import math

# ---------------- Key Ranking ----------------
def get_key_order(keyword):
    key = list(keyword.upper())
    sorted_key = sorted([(char, i) for i, char in enumerate(key)])

    order = [0] * len(key)

    for rank, (_, index) in enumerate(sorted_key):
        order[index] = rank

    return order


# ---------------- Encryption ----------------
def encrypt(plaintext, keyword):

    plaintext = plaintext.replace(" ", "").upper()
    cols = len(keyword)
    rows = math.ceil(len(plaintext) / cols)

    # Padding
    while len(plaintext) < rows * cols:
        plaintext += 'X'

    # Create Matrix
    matrix = []

    index = 0
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(plaintext[index])
            index += 1
        matrix.append(row)

    print("\nOriginal Matrix:")
    for row in matrix:
        print(" ".join(row))

    order = get_key_order(keyword)

    print("\nKey Ranking:")
    for i in range(cols):
        print(keyword[i], "->", order[i])

    # Encrypt
    ciphertext = ""

    for num in range(cols):
        col = order.index(num)
        for row in range(rows):
            ciphertext += matrix[row][col]

    return ciphertext


# ---------------- Decryption ----------------
def decrypt(ciphertext, keyword):

    cols = len(keyword)
    rows = math.ceil(len(ciphertext) / cols)

    order = get_key_order(keyword)

    matrix = [['' for _ in range(cols)] for _ in range(rows)]

    index = 0

    for num in range(cols):
        col = order.index(num)
        for row in range(rows):
            matrix[row][col] = ciphertext[index]
            index += 1

    print("\nPermuted Matrix:")
    for row in matrix:
        print(" ".join(row))

    plaintext = ""

    for row in matrix:
        plaintext += "".join(row)

    return plaintext.rstrip('X')


# ---------------- Main ----------------

plaintext = input("Enter Plaintext: ")
keyword = input("Enter Keyword: ")

cipher = encrypt(plaintext, keyword)
plain = decrypt(cipher, keyword)

print("\n========== Keyed Columnar Transposition ==========")
print("Plaintext :", plaintext.upper())
print("Keyword   :", keyword.upper())
print("Ciphertext:", cipher)
print("Decrypted :", plain)
