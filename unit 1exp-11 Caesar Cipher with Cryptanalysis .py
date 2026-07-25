# Q1: Caesar Cipher with Cryptanalysis

def encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result


def decrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift - key) % 26 + shift)
        else:
            result += char
    return result


def brute_force(ciphertext):
    print("\n----- Brute Force Attack -----")
    for key in range(1, 26):
        print(f"Key {key:2}: {decrypt(ciphertext, key)}")


# Main Program
plaintext = input("Enter Plaintext: ")
key = int(input("Enter Key (1-25): "))

ciphertext = encrypt(plaintext, key)
decrypted = decrypt(ciphertext, key)

print("\n========== Caesar Cipher ==========")
print("Plaintext :", plaintext)
print("Key       :", key)
print("Ciphertext:", ciphertext)
print("Decrypted :", decrypted)

brute_force(ciphertext)
