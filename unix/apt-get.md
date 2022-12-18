# apt-get

If hit the following types of error messages from `apt-get update`
```go
The following signatures couldn't be verified
because the public key is not available: NO_PUBKEY <KEY>
```
or
```go
E: Repository 'http://security.debian.org/debian-security buster/updates InRelease'
changed its 'Suite' value from 'stable' to 'oldstable'
```

A fix is:
```sh
apt-get update --allow-releaseinfo-change
```

TODO: Add explanations, how apt-get works more fundamentally
