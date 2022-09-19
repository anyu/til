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
# -P, run up to P processes at a time

seq 1 5 | xargs -n1 -P 5 curl http://localhost:8000
```
