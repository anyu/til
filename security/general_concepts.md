# General security concepts

## Core tenets of security

- **Confidentiality**: Keeping secrets secret
- **Integrity**: Ensuring message is not altered
- **Authenticity**: Verifying identity

## Encoding vs hashing vs encrypting
These three terms are often conflated/confused.
- **Encoding**: for data usability, can be reversed by same algorithm that encoded content (does not keep info secret, no key involved)
   - eg. base64, URL encoding, ASCII, unicode, UTF-8
- **Hashing (aka. one way encryption)**: for validating integrity of content
   - eg. MD5 , SHA-2, bcrypt
- **Encrypting**: for data confidentiality, requires secret key to retrieve original input
   - eg. AES, RSA, Blowfish
