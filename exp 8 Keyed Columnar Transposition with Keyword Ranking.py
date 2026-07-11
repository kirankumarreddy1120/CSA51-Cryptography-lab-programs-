# Keyed Columnar Transposition Cipher

text = input("Enter Plaintext: ").replace(" ", "")
key = input("Enter Keyword: ").upper()

cols = len(key)

# Padding with X
while len(text) % cols != 0:
    text += "X"

rows = len(text) // cols

# Create matrix row-wise
matrix = []
k = 0
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(text[k])
        k += 1
    matrix.append(row)

print("\nOriginal Matrix:")
for row in matrix:
    print(row)

# Generate ranking (handles duplicate letters)
rank = sorted(list(enumerate(key)), key=lambda x: (x[1], x[0]))

order = []
for i in rank:
    order.append(i[0])

print("Column Order:", order)

# Encryption
cipher = ""
for c in order:
    for r in range(rows):
        cipher += matrix[r][c]

print("Ciphertext:", cipher)

# Decryption
d = [['' for j in range(cols)] for i in range(rows)]

k = 0
for c in order:
    for r in range(rows):
        d[r][c] = cipher[k]
        k += 1

plain = ""
for i in range(rows):
    for j in range(cols):
        plain += d[i][j]

plain = plain.rstrip('X')

print("\nDecrypted Text:", plain)
