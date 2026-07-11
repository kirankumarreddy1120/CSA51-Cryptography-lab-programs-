# Rail Fence Cipher - Encryption and Decryption

def create_rail_matrix(text, rails):
    n = len(text)
    matrix = [[' ' for _ in range(n)] for _ in range(rails)]

    row = 0
    direction = 1

    for col in range(n):
        matrix[row][col] = text[col]

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    return matrix


def encrypt(text, rails):
    matrix = create_rail_matrix(text, rails)

    print("\nRail Matrix:")
    for r in matrix:
        print(' '.join(r))

    cipher = ""
    for r in matrix:
        for ch in r:
            if ch != ' ':
                cipher += ch

    return cipher


def decrypt(cipher, rails):
    n = len(cipher)

    # Create empty matrix
    matrix = [[' ' for _ in range(n)] for _ in range(rails)]

    # Mark zigzag positions
    row = 0
    direction = 1

    for col in range(n):
        matrix[row][col] = '*'

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    # Fill characters row-wise
    index = 0
    for i in range(rails):
        for j in range(n):
            if matrix[i][j] == '*' and index < n:
                matrix[i][j] = cipher[index]
                index += 1

    # Read in zigzag order
    text = ""
    row = 0
    direction = 1

    for col in range(n):
        text += matrix[row][col]

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    return text


# Main Program
plaintext = input("Enter Plaintext: ")
rails = int(input("Enter Number of Rails: "))

cipher = encrypt(plaintext, rails)
print("\nEncrypted Text:", cipher)

original = decrypt(cipher, rails)
print("Decrypted Text:", original)
