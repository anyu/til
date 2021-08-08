# Encryption

## Overview

Encryption generally involves: 1) scrambling information, 2) using a key to decrypt the scramble.

## States of encryption

### Encryption at rest

Protecting data when it’s stored
- Disk/filesystem-level encryption
- Encrypt data before it’s stored (in DB, on disk, etc)

### Encryption in-transit

Protecting data as it’s being transported
1. Encrypt data before transmission
1. Authenticate endpoints
1. Decrypt and verify data on arrival

### Encryption in use

Protecting data when it’s being accessed
- Homomorphic Encryption - form of encryption that allows users to perform computations on encrypted data without first decrypting it

## Two main types

### Symmetric encryption (aka. private key encryption)

- Uses a single key to encrypt/decrypt
- Mainly used to keep information private, particularly when performance matters or only single party involved (eg. password managers)
- More performant
- eg. AES (Advanced Encryption Standard), DES (Data Encryption Standard), Blowfish, RC4 (Rivest Cipher 4), ChaCha

### Asymmetric encryption (aka. public key encryption)

- Uses two different keys: a private and a public key
- Mainly used to authenticate a user/computer, verify if a message's authenticity, or to distribute symmetric keys
- More secure, but more computationally intensive/less performant
- eg. RSA (River Shamir Adleman), DSA (Digital Signature Algorithm), ECDSA (Elliptic Curve Digital Signature Algorithm), ECDH (Elliptic curve Diffie-Hellman), ED25519 (Edwards-curve Digital Signature Algorithm)

A hybrid model is sometimes used to take advantage of both (eg. TLS)

## Two methods of symmetric encryption

### Block ciphers

- Encrypt data in chunks (analogy: one page at a time)
- eg. AES (most widely used), DES, 3DES/IDEA, Blowfish

### Stream ciphers

- Encrypt data bit-by-bit (analogy: one letter at a time)
- eg. RC4 (most widely used, but recently proven insecure), Salsa20, ChaCha

## Block cipher spotlight: AES encryption

- Established as an encryption standard ~30 years ago; replaced DES (had 56-bit key limit)
- A variant of the Rjndael family of symmetric block cipher algorithms
- Used in TLS, file encryption, WiFi security, browser connection encryption, VPN implementations
- Why it's so popular: Fast and highly secure (good balance of trade-offs)
  - With a 256-bit encryption key, it’s virtually unbreakable

### How it works

- AES scrambles uses 4 scrambling operations per round
  - eg. perform operation -> repeat based off of previous round’s results X times
- AES has 3 key length options - affects number of rounds
  - 128-bit AES encryption key has 10 rounds
  - 192-bit AES encryption key has 12 rounds
  - 256-bit AES encryption key has 14 rounds
- Operations happen in binary

### 4 types of AES encryption operations

Plaintext data is divided into blocks (AES block size is 128-bits): 4x4 column of 16 bytes
1. **Key Expansion**: Uses initial key to come up with other keys for each round. New keys are derived via “Rijndael's key schedule”
1. **AddRoundKey**: Takes current data state and executes XOR against the current round’s subkey
1. **SubBytes** (substitute bytes): Substitutes each byte according to a table to another value
1. **ShiftRows**: Moves data positions with wrapping
1. **MixColumns**: Uses matrix multiplication and XOR to transform data

Then repeat/mix for # number of rounds.

### Block cipher modes of operation

- A block cipher (eg. AES) alone only encrypts one block
- Modes of operation describes how to repeatedly apply a single block cipher beyond the one block
- Most modes of operation require:
  - an initialization vector (aka. nonce, salt)
  - A random bit string with the same length as a block; adds randomness
  - If we encrypt the same plaintext twice with the same key, but different nonces, output will be different
  - Nonce is unique for every encryption but doesn’t need to be a secret
- Some use a padding algorithm - since a block cipher works on fixed size blocks, and messages can be in varying lengths, some modes require the final block be padded before encryption (eg. CBC)
- AE (Authenticated Encryption) mode - handles both encryption (confidentiality) and authentication (integrity)
- AEAD (Authenticated Encryption with Associated Data) mode - AE mode that also supports additional authenticated data

### Types of block cipher 'modes of operation'

**1. ECB (Electronic code book) mode**
- Each block is encrypted then appended to previous block.
- Simplest, very insecure

**2. CBC (Cipher block chaining) mode**
- Next cipher block is made by encrypting XOR output of previous cipher block + present plaintext block

**3. CFB (Cipher feedback) mode**
- Data is encrypted in form of units

**4. OFB (Output feedback) mode**
- Output of nonce encryption is used for next stage of encryption process

**5. CTR (Counter) mode**
- Uses number sequence as algorithm input
- **or block ciphers with 128-bit block size**

**essentially turns a block cipher into a stream cipher*

### GCM (Galois/Counter Mode)

- GCM combines Galois field multiplication with the counter mode operation
- Considered an authenticated encryption algorithm
  - Provides both data integrity/authenticity + confidentiality
- GMAC (Galois message authentication code): authentication-only variant of GCM
- Fast and efficient, highly recommended
- AES-GCM is a family of AEAD algorithms based on AES
- GCM is an authenticated encryption mode (more granularly, an AEAD mode) of operation for block ciphers

### Encryption configuration options
- Convergent encryption support - the same plaintext creates the same ciphertext (nonce is derived vs. randomly generated)
  - Enables server deduplication
    - If two users encrypt the same file, server can just store 1 copy
  - Uses original file to calculate a hash
  - Use hash as key to encrypt rest of file
  - Encrypt hash key an store securely
- Key derivation (KDF) function - functions to derive a key from other secret information
  - eg. HKDF, a KDF based on HMAC

## Appendix

### Encryption considerations

- How fast is encryption/decryption?
- How complicated is the implementation?
- Are there free implementations?
- Is it widely used?
- Can I parallelize it?
- How do I transmit the secret key?

### Glossary
- **plaintext**: the information before encryption or after decryption.
- **ciphertext**: the encrypted version of it, i.e. after encryption and before decryption
- **block cipher**: the algorithm used to encrypt a single block
- **mode**: the algorithm used to combine encrypted blocks
- **nonce/salt**: the not secret, random string used to introduce unique-ness

### Real life applications

- Uses 256-bit AES
  - Google Cloud data at rest
  - 1pass, LastPass (uses your master password to encrypt/decrypt)
  - TLS (uses many encryption algos, incl. AES)
- Zoom, until recently, was using 128-bit AES with ECB!

### Resources
- https://www.leozqin.me/aes-chain-block-cipher-vs-galoiscounter-modes-of-operation/
