# Open SSL

Print contents of a PEM-formatted cert
```shell
# in encoded form
openssl x509 -in <PEM FILE>.pem

# in plaintext (-noout additionally printing the encoded form)
openssl x509 -in  <PEM FILE>.pem -noout -text
```
Print start/expiry dates of a PEM-formatted cert
```shell
# expiry date (the `notAfter` date)
openssl x509 -in <PEM FILE>.pem -noout -enddate

# with both start + expiry dates (`notBefore`, `notAfter`)
openssl x509 -in <PEM FILE>.pem -noout -dates
```

Convert between formats
```shell
# PEM -> DER
openssl x509 -in <CERT>.pem -out <CERT>.der -outform DER

# DER -> PEM
openssl x509 -in <CERT>.der -out <CERT>.pem -outform PEM
```

Other useful flags
```shell
-startdate
-subject
-issuer
-pubkey
```
