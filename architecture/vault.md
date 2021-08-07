# Vault

## Overview

![Vault architecture](../_meta/images/architecture_vault.png)

### Storage Backend
- Responsible for durable storage of encrypted data
- Untrusted, outside security barrier

### Secrets Engine
- Secrets manager

### Barrier
- Responsible for: 1) ensuring only encrypted data goes out, 2) verifying/decrypting data coming in
- All data between Vault and storage backend passes through the barrier
- Barrier must be "unsealed" before inside contents can be accessed

## How it works

1. When started, Vault is in a *sealed* state.
1. Vault must be unsealed before any operations can be performed.
   - Provide unseal keys
   - When Vault is initialized, it generates an encryption key to protect all data. This data key is protected by a master key.
   - Vault uses Shamir's Secret Sharing (SSS)
