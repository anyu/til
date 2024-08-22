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

### Convert JSON to CSV

Given input JSON, convert to CSV with specific field values extracted (`id`, `name`, `tags`):

```json
{
  "message": "ok",
  "data": {
    "items": [
      {
        "id": 1,
        "ref_id": 22,
        "name": "some_name",
        "tags": []
      },
      {
        "id": 2,
        "ref_id": 33,
        "name": "some_name",
        "tags": []
      }
    ],
    "count": 2
  }
}
```

```sh
jq -r '.data.items[] | [.id, .name, (.tags | join(";"))] | @csv' input.json > output.csv
```

Do the same but with column headers:
```sh
jq -r '
  ["id", "name", "tags"],
  (.data.items[] | [
    .id, .name, (.tags | join(","))
  ])
  | @csv
' input.json > output.csv
```