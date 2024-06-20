
# The Crypto library in Python provides various cryptographic functionalities
# such as encryption, decryption, hashing, and key generation.
# The getPrime function generates a prime number,
# while getRandomRange generates a random number within a specified range.
from Crypto.Util.number import getPrime, getRandomRange

# # Publickey: This submodule of the Crypto library contains classes
# and functions related to public key cryptography , ElGamal:
# This class represents the ElGamal encryption scheme
from Crypto.PublicKey import ElGamal

# Generate a 2048-bit large prime number
p = getPrime(2048)

# Generate a private key, random number 1 <= x <= p-1
x = getRandomRange(1, p-1)

# Generate a public key
# we use a fixed generator for simplicity,
# but a more secure method would use a randomly chosen generator.
g = 2

# g = primative root p , x = private key , p = large prime number
y = pow(g, x, p)

# we create an object that represents the ElGamal public key,
# which can then be used for encryption and verification purposes in the ElGamal.
public_key = ElGamal.construct((p, g, y))

#  by assigning (p, x) to private_key,
#  we are creating a representation of the private key in the ElGamal,
#  where p is the prime modulus and x is the private exponent.
#  This key pair can then be used for decryption and signature generation in ElGamal.
private_key = (p, x)

# Encrypt a message using the public key
# let the user enter the message and convert it to byte
message = input("Enter your message: ").encode()


# int.from_bytes(message, 'big') is a Python function that converts a sequence of bytes,
# represented by the message variable, into an integer.
# The second argument, 'big', specifies the byte order,
# indicating that the most significant byte is at the beginning of the byte string.
plaintext = int.from_bytes(message, 'big')

# Generate a random number k, 1<= k <= p-1 , and the k must be unique each time
k = getRandomRange(1, p-1)

# Compute the ciphertext
# c1 =  g ^ k % p
c1 = pow(g, k, p)
# c2 = ( message * y^k % p) % p
c2 = plaintext * pow(y, k, p) % p

# we use the c1, c2 to create the ciphertext
ciphertext = (c1, c2)
print("ciphertext: ",ciphertext)

# Decrypt the ciphertext using the private key
c1, c2 = ciphertext

# K = c1^x mod p
# Calculate K
K = pow(c1, x, p)
# Calculate the modular inverse of K
K_inverse = pow(K, -1, p)
# Calculate plaintext
# # plaintext = c2 * K^-1 mod p
plaintext = (c2 * K_inverse) % p

# Convert the plaintext back to bytes
message = plaintext.to_bytes((plaintext.bit_length() + 7) // 8, 'big')
print("decrypted message: ",message.decode())