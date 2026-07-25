# Q2: Monoalphabetic Cipher with Frequency Analysis

import random
import string
from collections import Counter

# Generate random substitution key
alphabet = list(string.ascii_uppercase)
shuffled = alphabet.copy()
random.shuffle(shuffled)

encrypt_map = dict(zip(alphabet, shuffled))
decrypt_map = dict(zip(shuffled, alphabet))


# Encryption Function
def encrypt(text):
    result = ""
    for ch in text.upper():
        if ch.isalpha():
            result += encrypt_map[ch]
        else:
            result += ch
    return result


# Decryption Function
def decrypt(cipher):
    result = ""
    for ch in cipher:
        if ch.isalpha():
            result += decrypt_map[ch]
        else:
            result += ch
    return result


# Frequency Analysis
def frequency_analysis(cipher):
    letters = [c for c in cipher if c.isalpha()]
    freq = Counter(letters)

    print("\nLetter Frequency:")
    for letter, count in sorted(freq.items()):
        print(f"{letter} : {count}")

    print("\nTop 3 Most Frequent Letters:")
    top3 = freq.most_common(3)
    for letter, count in top3:
        print(f"{letter} -> {count}")


# Main Program
plaintext = input("Enter Plaintext: ")

ciphertext = encrypt(plaintext)
decrypted = decrypt(ciphertext)

print("\n========== Monoalphabetic Cipher ==========")

print("\nGenerated Key:")
for a, b in zip(alphabet, shuffled):
    print(f"{a} -> {b}")

print("\nPlaintext :", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted :", decrypted)

frequency_analysis(ciphertext)
