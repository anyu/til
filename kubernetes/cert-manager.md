# cert-manager

[cert-manager](https://github.com/jetstack/cert-manager) is a k8s add-on to manage and issue TLS certificates.

Ensures certs are valid and renews them periodically.

Certificate steps:

Manually or automatically obtain a certificate
1. Create a k8s secret to hold the TLS cert `cert.pem`, and the private key `key.pem`
