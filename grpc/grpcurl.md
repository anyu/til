# grpcurl

Make curl-like requests to gRPC servers.

### Installation

```shell
brew install grpcurl
```

### Handy queries

List all services exposed by a gRPC server:

```shell
grpcurl -plaintext localhost:8000 list
```

List all methods attached to a service:

```shell
grpcurl -plaintext localhost:8000 list my.custom.server.Service
```

Describe a method:
```shell
$ grpcurl -plaintext localhost:8000 describe my.custom.server.Service/Method

my.custom.server.Service.Method is a message:
message Method {
string name = 1;
}
```

Describe a method and generate JSON message template:
```shell
$ grpcurl -plaintext -msg-template localhost:8000 describe my.custom.server.Service.Method

my.custom.server.Service.Method is a message:
message Method {
  string name = 1;
}

Message template:
{
  "name": ""
}
```

Send a request, inline:
```shell
grpcurl -d '{"name": "some_data"}' -plaintext localhost:8000 my.custom.server.Service.Method
```

Send a request, with message template:

`msg.json` (copied from `-msg-template` output above)
```shell
{
  "name": "some_data"
}
```

```shell
grpcurl -d @ -plaintext localhost:8000 my.custom.server.Service.Method <msg.json
```
