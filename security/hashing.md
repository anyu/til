# Hashing

## Overview

Transforms plaintext into a fixed-length output (aka. hash/digest*) with the following attributes:
 - Same input always outputs same hash (the hash is usually shorter than input)
 - Different inputs should not produce the same hash (collision)
 - Should be irreversible (shouldn’t be able to get the original input from hash)
 - Slight change in input should produce a different hash

**checksum is loosely the umbrella term*

**Use cases**
- The most suitable way to store passwords securely
- Useful for comparing values for avoiding duplication
- Useful for finding specific data in large database
- Used in digital certificates

## Cryptographic vs non-cryptographic hash functions

Cryptographic hashes guarantees certain security properties:
- preimage resistance (given a hash `h`, it must be difficult to find a message that yields `h` when hashed)
- strong collision resistence (difficult to find two messages with the same hash)
- eg. SHA-2, HMAC, BLAKE, Whirlpool

Non-cryptographic hashes have weaker collision guarantees but are generally much faster.
- eg. MurmurHash, FNV-1, xxHash

NOTE: Different language implementations of these algorithms, particularly the less common ones, may result in varying hashes between them.

**MurmurHash3 Resources**
- JS tool: https://cimi.io/murmurhash3js-revisited
- Reason why Scala's implementation may [differ from others](https://stackoverflow.com/questions/39176052/scala-murmurhash3-library-not-matching-python-mmh3-library/46472986#46472986)


## Password storage concepts

### Salting

- A salt is a unique, random string added to each password during hashing
- Unique to every user
- Protects against attacks with pre-computed hashes using rainbow tables
- Protects against revealing if 2 users have the same password. Different salts result in different hashes even if passwords are the same.

### Peppering

- A pepper can be added on top of salting for an extra layer of protection
- Prevents attacker from cracking any hashes if they only have access to the DB

### Work Factors

- The # of iterations of hashing performed for each password
- Need to balance security (higher WF makes calculating hash more computationally expensive for attackers) and performance (but makes login slower)
- Work factor is typically stored in the hash output

## Password hashing algorithms

- Designed to be slow; work factor can be configured
- Safe to disclose publicly: https://pulse.michalspacek.cz/passwords/storages

### Recommended

- Argon2 - won 2015 Password Hashing Competition
  - Argon2id variant is most recommended
- bcrypt - automatically salts; supposedly has an offline cracking vulnerability
  - Has max input length limit of 72 bytes for most implementations
  - [Avoid combining bcrypt with other hash functions!](https://blog.ircmaxell.com/2015/03/security-issue-combining-bcrypt-with.html) (eg. pre-hashing)
- scrypt - can increase amount of memory needed to compute the hash (a “memory-hard” algorithm)

## Misc

For  “fast” use cases (TLS, blockchain)
- SHA-2 (Secure Hashing Algorithm 2) - includes SHA-256
- MD5 (message digest) - no longer recommended

### Compared with MACS

- MAC (message authentication code): A method of combining a shared secret key with a message, so the recipient can verify integrity + authenticity. Does not encrypt.
- HMAC (hash-based message authentication code): Applies hash function multiple times to some combination of the shared secret + message
