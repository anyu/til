# Bash

## Basic loops
```shell
for i in {1..10}; do echo $i; done
```

```shell
for i in `seq 1 10`; do echo $i; done
```

## Making parallel requests

```shell
# -I, replace occurrence of string with standard input
# -P, run up to P processes at a time

xargs -I % -P 5 curl http://localhost:8000 < <(printf '%s\n' {1..10})
```
