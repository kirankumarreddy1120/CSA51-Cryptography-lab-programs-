# Cryptanalysis of Columnar Transposition Cipher

cipher = input("Enter Ciphertext: ")

for cols in range(2, 9):
    if len(cipher) % cols != 0:
        continue

    rows = len(cipher) // cols

    # Create empty matrix
    matrix = [['' for j in range(cols)] for i in range(rows)]

    # Fill column-wise
    k = 0
    for j in range(cols):
        for i in range(rows):
            matrix[i][j] = cipher[k]
            k += 1

    # Read row-wise
    text = ""
    for i in range(rows):
        for j in range(cols):
            text += matrix[i][j]

    print("\nPossible Plaintext (Key Length =", cols, ")")
    print(text)
