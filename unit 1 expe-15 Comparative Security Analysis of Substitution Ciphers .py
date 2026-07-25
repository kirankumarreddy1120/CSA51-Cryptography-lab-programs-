# Q5: Comparative Security Analysis of Substitution Ciphers

import random
import string
import time

# ---------------- Caesar Cipher ----------------
def caesar_encrypt(text, key):
    result = ""
    for ch in text.upper():
        if ch.isalpha():
            result += chr((ord(ch) - 65 + key) % 26 + 65)
        else:
            result += ch
    return result


# ---------------- Monoalphabetic Cipher ----------------
alphabet = string.ascii_uppercase
shuffled = list(alphabet)
random.shuffle(shuffled)

mono_key = dict(zip(alphabet, shuffled))

def mono_encrypt(text):
    result = ""
    for ch in text.upper():
        if ch.isalpha():
            result += mono_key[ch]
        else:
            result += ch
    return result


# ---------------- Vigenere Cipher ----------------
def vigenere_encrypt(text, key):
    text = text.upper()
    key = key.upper()

    result = ""
    j = 0

    for ch in text:
        if ch.isalpha():
            shift = ord(key[j % len(key)]) - 65
            result += chr((ord(ch) - 65 + shift) % 26 + 65)
            j += 1
        else:
            result += ch

    return result


# ---------------- Hill Cipher ----------------
hill_key = [[3, 3],
            [2, 5]]

def hill_encrypt(text):

    text = text.upper().replace(" ", "")

    if len(text) % 2 != 0:
        text += "X"

    cipher = ""

    for i in range(0, len(text), 2):

        p1 = ord(text[i]) - 65
        p2 = ord(text[i + 1]) - 65

        c1 = (hill_key[0][0] * p1 + hill_key[0][1] * p2) % 26
        c2 = (hill_key[1][0] * p1 + hill_key[1][1] * p2) % 26

        cipher += chr(c1 + 65)
        cipher += chr(c2 + 65)

    return cipher


# ---------------- Frequency Analysis ----------------
def frequency(text):
    freq = {}

    for ch in text:
        if ch.isalpha():
            freq[ch] = freq.get(ch, 0) + 1

    return freq


# ---------------- Main ----------------
plaintext = input("Enter Plaintext: ")

print("\n================ Comparative Security Analysis ================\n")

# Caesar
start = time.perf_counter()
caesar = caesar_encrypt(plaintext, 3)
caesar_time = time.perf_counter() - start

# Monoalphabetic
start = time.perf_counter()
mono = mono_encrypt(plaintext)
mono_time = time.perf_counter() - start

# Vigenere
start = time.perf_counter()
vigenere = vigenere_encrypt(plaintext, "KEY")
vigenere_time = time.perf_counter() - start

# Hill
start = time.perf_counter()
hill = hill_encrypt(plaintext)
hill_time = time.perf_counter() - start

print("{:<18} {:<25} {:<12}".format("Cipher", "Ciphertext", "Time (sec)"))
print("-" * 60)

print("{:<18} {:<25} {:.8f}".format("Caesar", caesar, caesar_time))
print("{:<18} {:<25} {:.8f}".format("Monoalphabetic", mono, mono_time))
print("{:<18} {:<25} {:.8f}".format("Vigenere", vigenere, vigenere_time))
print("{:<18} {:<25} {:.8f}".format("Hill", hill, hill_time))

print("\n================ Frequency Distribution ================\n")

print("Caesar        :", frequency(caesar))
print("Monoalphabetic:", frequency(mono))
print("Vigenere      :", frequency(vigenere))
print("Hill          :", frequency(hill))

print("\n================ Security Observation ================\n")

print("1. Caesar Cipher       : Weak (Fixed Shift)")
print("2. Monoalphabetic      : Better than Caesar")
print("3. Vigenere Cipher     : Strong against frequency analysis")
print("4. Hill Cipher         : Strongest among these (Matrix-based)")
