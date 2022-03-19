# DNS

### Making DNS queries

Use nslookup or dig.

### Installing `nslookup` or `host`

Need to install via `dnsutils`
```shell
apt-get update
apt-get install dnsutils
```

### dig

#### dig with an specific DNS server to query
```shell
dig @8.8.8.8 example.com
```
#### find & dig against the authoritative name server

Let's say your DNS was in a bad state.

```shell
$ dig some-example-domain.com
...
;; ANSWER SECTION:
some-example-domain.com. 60	IN	CNAME	bad-state.dns.some-domain.net.
...
```

Check if the DNS resolves. If not, may not see Answer section, but would see Authority section:
```shell
$ dig bad-state.dns.some-domain.net

...
;; AUTHORITY SECTION:
dns.some-domain.net. 900	IN	SOA	ns.some-dns.net. some-hostmaster.com. ...
...
```

Could then dig straight against authoritative name server
```shell
$ dig @ns.some-dns.net. some-region.dns.some-domain.net
```
