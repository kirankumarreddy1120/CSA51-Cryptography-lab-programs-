# Simple Columnar Transposition Cipher

text = input("Enter Plaintext: ")
cols = int(input("Enter Key Length: "))
pad = input("Enter Padding Character: ")

# Add padding
while len(text) % cols != 0:
    text += pad

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

# Display matrix
print("\nMatrix:")
for row in matrix:
    print(row)

# Encryption (column-wise)
cipher = ""
for j in range(cols):
    for i in range(rows):
        cipher += matrix[i][j]

print("Ciphertext:", cipher)

# Decryption
k = 0
d = [['' for j in range(cols)] for i in range(rows)]

for j in range(cols):
    for i in range(rows):
        d[i][j] = cipher[k]
        k += 1

plain = ""
for i in range(rows):
    for j in range(cols):
        plain += d[i][j]

# Remove padding
while plain.endswith(pad):
    plain = plain[:-1]

print("Decrypted Text:", plain)
