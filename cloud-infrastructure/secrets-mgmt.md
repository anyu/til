# Secrets Management

## Comparing solutions

### Roll your own
- TBD

### AWS services

#### AWS Systems Parameter Store (SSM Parameter Store)
- A managed generic key/value storage service (unencrypted or encrypted)
- Leverages KMS to encrypt data
- Lower cost

#### AWS Secrets Manager
- A managed key/value storage service for secrets
- Managed key/value store specifically (and only) for encrypted data
- Leverages KMS to encrypt data
- Handles key rotation

#### AWS Key Management Service (KMS)
- A managed encryption service ("Encryption as a service")
- Generates and manages cryptographic keys; uses them to encrypt/decrypt data
- Stores keys, not data
- Akin to Vault's Transit Secrets Engine

### GCP services

#### GCP Secret Manager
- A managed key/value storage service for secrets

#### Google Cloud Key Management Service (KMS)
- A managed encryption service ("Encryption as a service")
- Generates and manages cryptographic keys; uses them to encrypt/decrypt data
- Stores keys, not data
- Akin to Vault's Transit Secrets Engine

### Vault

- Self-hosted, full-fledged secrets management solution (secrets store, encryption service, and more)
- Vault's Secrets Engines = encryption service
  - Transit Engine
  - also supports AWS, Google KMS
