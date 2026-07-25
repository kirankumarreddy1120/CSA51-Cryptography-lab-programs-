# Q9: Double Transposition Cipher with Security Comparison

import math
import time


# ---------- Key Ranking ----------
def get_key_order(keyword):
    keyword = keyword.upper()
    sorted_key = sorted(list(enumerate(keyword)), key=lambda x: (x[1], x[0]))
    order = [0] * len(keyword)

    for rank, (index, _) in enumerate(sorted_key):
        order[index] = rank

    return order


# ---------- Single Columnar Encryption ----------
def columnar_encrypt(text, keyword):

    cols = len(keyword)
    rows = math.ceil(len(text) / cols)

    while len(text) < rows * cols:
        text += 'X'

    matrix = []
    k = 0

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(text[k])
            k += 1
        matrix.append(row)

    order = get_key_order(keyword)

    cipher = ""

    for n in range(cols):
        col = order.index(n)
        for row in range(rows):
            cipher += matrix[row][col]

    return cipher


# ---------- Single Columnar Decryption ----------
def columnar_decrypt(cipher, keyword):

    cols = len(keyword)
    rows = math.ceil(len(cipher) / cols)

    matrix = [['' for _ in range(cols)] for _ in range(rows)]

    order = get_key_order(keyword)

    k = 0

    for n in range(cols):
        col = order.index(n)
        for row in range(rows):
            matrix[row][col] = cipher[k]
            k += 1

    text = ""

    for row in matrix:
        text += "".join(row)

    return text.rstrip('X')


# ---------- Main ----------

plaintext = input("Enter Plaintext: ").replace(" ", "").upper()

key1 = input("Enter First Keyword : ")
key2 = input("Enter Second Keyword: ")

# Single Transposition
start = time.perf_counter()
single_cipher = columnar_encrypt(plaintext, key1)
single_time = time.perf_counter() - start

# Double Transposition
start = time.perf_counter()
first = columnar_encrypt(plaintext, key1)
double_cipher = columnar_encrypt(first, key2)
double_time = time.perf_counter() - start

# Decryption
step1 = columnar_decrypt(double_cipher, key2)
original = columnar_decrypt(step1, key1)

print("\n=========== Double Transposition Cipher ===========")

print("\nPlaintext           :", plaintext)
print("First Keyword       :", key1.upper())
print("Second Keyword      :", key2.upper())

print("\nAfter 1st Transposition :", first)
print("After 2nd Transposition :", double_cipher)

print("\nRecovered Plaintext :", original)

print("\n=========== Security Comparison ===========")

print("{:<25}{:.8f} sec".format("Single Transposition", single_time))
print("{:<25}{:.8f} sec".format("Double Transposition", double_time))

print("\nObservation:")
print("- Double Transposition produces stronger ciphertext.")
print("- It is harder to break than Single Transposition.")
print("- Execution time is slightly higher due to two encryptions.")
