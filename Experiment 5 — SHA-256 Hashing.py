import hashlib

# Get message from user
message = input("Enter the message: ")

# Convert message into bytes
data = message.encode()

# Generate SHA-256 hash
hash_value = hashlib.sha256(data).hexdigest()

print("\nOriginal Message:", message)
print("SHA-256 Hash:", hash_value)

# Verify the message
verify_message = input("\nEnter message again for verification: ")

verify_hash = hashlib.sha256(verify_message.encode()).hexdigest()

print("Verification Hash:", verify_hash)

if hash_value == verify_hash:
    print("Message Integrity Verified!")
else:
    print("Message has been modified!")
