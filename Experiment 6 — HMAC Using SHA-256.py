import hmac
import hashlib

# Get message and secret key
message = input("Enter the message: ")
key = input("Enter the secret key: ")

# Generate HMAC using SHA-256
hmac_value = hmac.new(
    key.encode(),
    message.encode(),
    hashlib.sha256
).hexdigest()

print("\nOriginal Message:", message)
print("HMAC-SHA256:", hmac_value)

# Verify the message
verify_message = input("\nEnter message for verification: ")

verify_hmac = hmac.new(
    key.encode(),
    verify_message.encode(),
    hashlib.sha256
).hexdigest()

print("Verification HMAC:", verify_hmac)

# Compare HMAC values securely
if hmac.compare_digest(hmac_value, verify_hmac):
    print("Message Authentication Successful!")
    print("Message Integrity Verified!")
else:
    print("Authentication Failed!")
    print("Message may have been modified.")
