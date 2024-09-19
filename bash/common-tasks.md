# Bash

## Basic loops
```sh
for i in {1..10}; do echo $i; done
```

```sh
for i in `seq 1 10`; do echo $i; done
```

## Making parallel requests

```sh
# -P, run up to P processes at a time

seq 1 5 | xargs -n1 -P 5 curl http://localhost:8000
```

## Remove header row from csv

```sh
tail -n +2 input.csv > output.csv
```


## Useful resources

- https://explainshell.com
- https://thevaluable.dev/guide-terminal-shell-console
