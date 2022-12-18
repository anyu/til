# PGP

- Pretty Good Privacy (PGP)
- based on a web of trust rather than certificate authorities (CA)
- allows users to choose who they trust
- PGP is “owned” by Symantec, but OpenPGP, an e-mail encryption standard, is implemented by multiple software.
- Uses asymmetric crypotography for key generation, symmetrical encryption for message encryption

## How it works
- You have a public key and a private key 
- Make public key public – ppl encrypt sensitive messages to you with it 
- Use your private key to decrypt it
- Using a PGP software, PGP creates a one-off session key. This session key is used to encrypt plaintext with symmetric-key cryptography. The session key is then encrypted using the journalist’s public key.
- Digital signatures can be used alongside PGP’s message encryption or separately
- Trust is through web of trust:	
  - If both of you meet one new PGP user each and digitally sign their certificates to verify their identities, you start to build a small network, where the four of you can trust the links between the public keys and identities, based on the trust each person has in others that they are linked to.

## Considerations
PGP encryption does not encrypt the subject line of an e-mail. Never put any sensitive information in the subject line.

## Compared to PKI
PGP certificates can be signed by anyone, while an X.509 certificate must be signed by what is known as a certificate authority.

