# jq

### Convert UNIX timestamp to date format
```shell
$ date +%s | jq "todate" // date +%s = current time in UNIX
"2022-04-11T14:30:44Z"

$ echo 1649687307 | jq "todate"
"2022-04-11T14:28:27Z"
```

### Manipulate files

Given a json file with such contents:

```json
[
  {
    "name": "some-name",
    "email": "email@domain.com",
    "target_field": "value1"
  },
  {
    "name": "some-name2",
    "email": "email2@domain.com",
    "target_field": "value2"
  }
]
```

Get length of json file array

```shell
jq 'length' input.json
```

Extract `target_field` and keep in JSON:

```shell
jq '[.[] | {target_field: .target_field}]' input.json > output.json
```

Output
```json
[
  {"target_field": "value1"},
  {"target_field": "value2"}
]
```

Extract `target_field`'s values only:

```shell
jq -r '.[].target_field' input.json > output.txt
```

Output
```
value1
value2
```
