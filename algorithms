# Crypto Algorithms

## TODO: category

### Shamir's Secret Sharing (SSS) scheme

- Algorithm that allows secrets to be distributed securely amongst an untrusted network.
- Makes it possible for multiple parties who don't know each other to store secrets.
- Allows secret to be split into many parts and only requires a minimum number (aka. the threshold) of parts to reconstruct original the secret
- Flexible and extensible: Secret owner can add/remove parts any time without modifying secret

#### How it works
- Uses polynomial interpolation (basically a way to estimate unknown values in a gap between two known data points)
- TLDR: SSS encodes a secret into a polynomial -> splits it into pieces -> distributes.

#### Real life applications
- Used by Vault to split unseal keys