# Q10: Cryptanalysis Tool for Columnar Transposition Cipher
# Brute-force key lengths (2–8) and rank plaintexts using English frequency scoring

import itertools
import math

# ---------------- English Letter Frequency ----------------
english_freq = {
    'E': 12.7, 'T': 9.1, 'A': 8.2, 'O': 7.5, 'I': 7.0,
    'N': 6.7, 'S': 6.3, 'H': 6.1, 'R': 6.0, 'D': 4.3,
    'L': 4.0, 'C': 2.8, 'U': 2.8, 'M': 2.4, 'W': 2.4,
    'F': 2.2, 'G': 2.0, 'Y': 2.0, 'P': 1.9, 'B': 1.5,
    'V': 1.0, 'K': 0.8, 'J': 0.15, 'X': 0.15,
    'Q': 0.10, 'Z': 0.07
}


# ---------------- Score Plaintext ----------------
def score_text(text):
    score = 0
    for ch in text:
        if ch in english_freq:
            score += english_freq[ch]
    return score


# ---------------- Columnar Decryption ----------------
def decrypt(cipher, perm):

    cols = len(perm)
    rows = math.ceil(len(cipher) / cols)

    matrix = [['' for _ in range(cols)] for _ in range(rows)]

    index = 0

    for p in perm:
        for r in range(rows):
            if index < len(cipher):
                matrix[r][p] = cipher[index]
                index += 1

    plaintext = ""

    for r in matrix:
        plaintext += "".join(r)

    return plaintext.rstrip('X')


# ---------------- Main ----------------

ciphertext = input("Enter Ciphertext: ").replace(" ", "").upper()

results = []

for key_len in range(2, 9):

    print("\nTrying Key Length =", key_len)

    for perm in itertools.permutations(range(key_len)):

        try:
            plain = decrypt(ciphertext, perm)
            score = score_text(plain)
            results.append((score, key_len, perm, plain))
        except:
            pass


results.sort(reverse=True)

print("\n========== Top 5 Probable Plaintexts ==========\n")

for i in range(min(5, len(results))):
    score, key_len, perm, plain = results[i]

    print("Rank :", i + 1)
    print("Key Length :", key_len)
    print("Permutation:", perm)
    print("Score :", round(score, 2))
    print("Plaintext :", plain)
    print("-" * 50)
