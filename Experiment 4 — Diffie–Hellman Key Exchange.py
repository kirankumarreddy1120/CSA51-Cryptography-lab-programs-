# Diffie-Hellman Key Exchange

# Public values
p = 23
g = 5

# Private keys
a = 6
b = 15

# Alice calculates her public key
A = pow(g, a, p)

# Bob calculates his public key
B = pow(g, b, p)

# Alice calculates shared secret
secret_A = pow(B, a, p)

# Bob calculates shared secret
secret_B = pow(A, b, p)

print("Public Prime (p):", p)
print("Public Base (g):", g)

print("\nAlice's Private Key:", a)
print("Alice's Public Key :", A)

print("\nBob's Private Key:", b)
print("Bob's Public Key :", B)

print("\nShared Secret calculated by Alice:", secret_A)
print("Shared Secret calculated by Bob  :", secret_B)

if secret_A == secret_B:
    print("\nKey Exchange Successful!")
    print("Shared Secret Key:", secret_A)
else:
    print("\nKey Exchange Failed!")
