Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
from math import gcd

... # Choose two prime numbers
... p = 61
... q = 53
... 
... # Calculate n
... n = p * q
... 
... # Calculate Euler's Totient
... phi = (p - 1) * (q - 1)
... 
... # Choose public exponent e
... e = 17
... 
... # Check e and phi are relatively prime
... if gcd(e, phi) != 1:
...     print("Invalid value of e")
...     exit()
... 
... # Calculate private exponent d
... d = pow(e, -1, phi)
... 
... print("Public Key  :", (e, n))
... print("Private Key :", (d, n))
... 
... # Message
... message = int(input("\nEnter a number to encrypt: "))
... 
... if message >= n:
...     print("Message must be smaller than", n)
...     exit()
... 
... # Encryption
... ciphertext = pow(message, e, n)
... 
... # Decryption
... decrypted = pow(ciphertext, d, n)
... 
... print("Original Message :", message)
... print("Encrypted Message:", ciphertext)
