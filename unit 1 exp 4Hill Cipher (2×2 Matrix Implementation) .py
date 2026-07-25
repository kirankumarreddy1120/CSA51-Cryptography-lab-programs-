# Q4: Hill Cipher (2×2 Matrix Implementation)

# Function to find modular inverse
def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


# Matrix multiplication (2x2)
def matrix_multiply(matrix, pair):
    return [
        (matrix[0][0] * pair[0] + matrix[0][1] * pair[1]) % 26,
        (matrix[1][0] * pair[0] + matrix[1][1] * pair[1]) % 26
    ]


# Encryption
def encrypt(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")

    if len(plaintext) % 2 != 0:
        plaintext += "X"

    ciphertext = ""

    for i in range(0, len(plaintext), 2):
        pair = [
            ord(plaintext[i]) - ord('A'),
            ord(plaintext[i + 1]) - ord('A')
        ]

        encrypted = matrix_multiply(key, pair)

        ciphertext += chr(encrypted[0] + ord('A'))
        ciphertext += chr(encrypted[1] + ord('A'))

    return ciphertext


# Decryption
def decrypt(ciphertext, key):

    det = (key[0][0] * key[1][1] - key[0][1] * key[1][0]) % 26

    inv_det = mod_inverse(det, 26)

    if inv_det is None:
        print("Key matrix is not invertible.")
        return ""

    inverse = [
        [( key[1][1] * inv_det) % 26,
         (-key[0][1] * inv_det) % 26],

        [(-key[1][0] * inv_det) % 26,
         ( key[0][0] * inv_det) % 26]
    ]

    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        pair = [
            ord(ciphertext[i]) - ord('A'),
            ord(ciphertext[i + 1]) - ord('A')
        ]

        decrypted = matrix_multiply(inverse, pair)

        plaintext += chr(decrypted[0] + ord('A'))
        plaintext += chr(decrypted[1] + ord('A'))

    return plaintext


# ---------------- Main Program ----------------

print("Enter 2×2 Key Matrix:")

key = []
for i in range(2):
    row = list(map(int, input().split()))
    key.append(row)

det = (key[0][0] * key[1][1] - key[0][1] * key[1][0]) % 26

if mod_inverse(det, 26) is None:
    print("\nInvalid Key Matrix")
    print("Determinant =", det)
    print("Determinant is NOT relatively prime to 26.")
else:
    print("\nValid Key Matrix")
    print("Determinant =", det)

    plaintext = input("\nEnter Plaintext: ")

    cipher = encrypt(plaintext, key)

    recovered = decrypt(cipher, key)

    print("\n========== Hill Cipher ==========")
    print("Plaintext :", plaintext.upper())
    print("Ciphertext:", cipher)
    print("Decrypted :", recovered)
