# Double Transposition Cipher

def encrypt(text, key):
    cols = len(key)

    while len(text) % cols != 0:
        text += "X"

    rows = len(text) // cols

    # Create matrix
    matrix = []
    k = 0
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(text[k])
            k += 1
        matrix.append(row)

    # Column order
    order = sorted(range(cols), key=lambda i: key[i])

    # Read column-wise
    cipher = ""
    for c in order:
        for r in range(rows):
            cipher += matrix[r][c]

    return cipher


def decrypt(cipher, key):
    cols = len(key)
    rows = len(cipher) // cols

    order = sorted(range(cols), key=lambda i: key[i])

    matrix = [['' for j in range(cols)] for i in range(rows)]

    k = 0
    for c in order:
        for r in range(rows):
            matrix[r][c] = cipher[k]
            k += 1

    text = ""
    for i in range(rows):
        for j in range(cols):
            text += matrix[i][j]

    return text.rstrip('X')


# Main Program
text = input("Enter Plaintext: ").replace(" ", "")
key1 = input("Enter First Key: ").upper()
key2 = input("Enter Second Key: ").upper()

# First Transposition
c1 = encrypt(text, key1)
print("After First Transposition :", c1)

# Second Transposition
c2 = encrypt(c1, key2)
print("After Second Transposition:", c2)

# Decryption
d1 = decrypt(c2, key2)
print("After First Decryption    :", d1)

d2 = decrypt(d1, key1)
print("Original Text             :", d2)
