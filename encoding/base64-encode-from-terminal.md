# base64-encode/decode from terminal

### Encode
```sh
$ base64 <<< msg_to_encode
aGV5Cg==
```
From file
```sh
$ base64 -i <file>
aGV5Cg==
```

### Decode
```sh
$ base64 -d <<< aGV5Cg==
msg_to_encode
```
From file
```sh
$ base64 -d -i <file>
msg_to_encode
```