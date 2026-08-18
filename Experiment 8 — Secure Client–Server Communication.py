from cryptography.fernet import Fernet
import hashlib

# Generate a shared secret key
key = Fernet.generate_key()
cipher = Fernet(key)

print("===== SECURE CLIENT-SERVER COMMUNICATION =====")

# ---------------- CLIENT ----------------

message = input("\nClient - Enter message: ")

# Generate SHA-256 hash
original_hash = hashlib.sha256(message.encode()).hexdigest()

# Encrypt message
encrypted_message = cipher.encrypt(message.encode())

print("\n--- CLIENT ---")
print("Original Message :", message)
print("SHA-256 Hash     :", original_hash)
print("Encrypted Message:", encrypted_message.decode())

# ---------------- SERVER ----------------

print("\n--- SERVER ---")

# Decrypt message
decrypted_message = cipher.decrypt(encrypted_message).decode()

# Generate hash of decrypted message
received_hash = hashlib.sha256(decrypted_message.encode()).hexdigest()

print("Decrypted Message:", decrypted_message)
print("Received Hash    :", received_hash)

# Verify integrity
if original_hash == received_hash:
    print("\nMessage Integrity: VERIFIED")
    print("Secure communication successful!")
else:
    print("\nMessage Integrity: FAILED")
    print("Message may have been modified.")
