# Q6: Rail Fence Cipher Implementation with Performance Analysis

import time

# ---------------- Encryption ----------------
def encrypt(text, rails):
    rail = [['\n' for _ in range(len(text))] for _ in range(rails)]

    direction_down = False
    row = 0
    col = 0

    for ch in text:
        if row == 0 or row == rails - 1:
            direction_down = not direction_down

        rail[row][col] = ch
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    print("\nRail Matrix:")
    for r in rail:
        print(" ".join(c if c != '\n' else '.' for c in r))

    cipher = ""
    for i in range(rails):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                cipher += rail[i][j]

    return cipher


# ---------------- Decryption ----------------
def decrypt(cipher, rails):

    rail = [['\n' for _ in range(len(cipher))] for _ in range(rails)]

    direction_down = None
    row = 0
    col = 0

    # Mark zigzag positions
    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == rails - 1:
            direction_down = False

        rail[row][col] = '*'
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    # Fill characters
    index = 0
    for i in range(rails):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    # Read zigzag
    result = ""
    row = 0
    col = 0

    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == rails - 1:
            direction_down = False

        result += rail[row][col]
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    return result


# ---------------- Main ----------------

plaintext = input("Enter Plaintext: ")
rails = int(input("Enter Number of Rails (2-10): "))

start = time.perf_counter()
cipher = encrypt(plaintext, rails)
enc_time = time.perf_counter() - start

start = time.perf_counter()
plain = decrypt(cipher, rails)
dec_time = time.perf_counter() - start

print("\n========== Rail Fence Cipher ==========")
print("Plaintext :", plaintext)
print("Ciphertext:", cipher)
print("Decrypted :", plain)

print("\nPerformance Analysis")
print("Encryption Time : {:.8f} sec".format(enc_time))
print("Decryption Time : {:.8f} sec".format(dec_time))
print("Time Complexity : O(n)")
