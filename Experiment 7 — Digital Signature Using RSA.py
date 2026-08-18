import hashlib

# RSA parameters
p = 61
q = 53

n = p * q
phi = (p - 1) * (q - 1)

# Public exponent
e = 17

# Private exponent
d = pow(e, -1, phi)

# Display keys
print("Public Key :", (e, n))
print("Private Key:", (d, n))

# Get message
message = input("\nEnter the message: ")

# Generate SHA-256 hash
hash_hex = hashlib.sha256(message.encode()).hexdigest()

# Convert hash into an integer
hash_value = int(hash_hex, 16)

# For this simple lab demonstration, reduce hash modulo n
hash_value = hash_value % n

# Generate digital signature using private key
signature = pow(hash_value, d, n)

print("\nSHA-256 Hash:", hash_hex)
print("Digital Signature:", signature)

# Verification
verify_message = input("\nEnter message for verification: ")

# Generate hash of received message
verify_hash_hex = hashlib.sha256(
    verify_message.encode()
).hexdigest()

verify_hash = int(verify_hash_hex, 16) % n

# Verify signature using public key
recovered_hash = pow(signature, e, n)

print("\nVerification Hash:", verify_hash)
print("Recovered Hash   :", recovered_hash)

if verify_hash == recovered_hash:
    print("\nDigital Signature is VALID")
    print("Message is authentic and unchanged.")
else:
    print("\nDigital Signature is INVALID")
    print("Message may have been modified.")
