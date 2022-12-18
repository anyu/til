# jq

### Convert UNIX timestamp to date format
```shell
$ date +%s | jq "todate" // date +%s = current time in UNIX
"2022-04-11T14:30:44Z"

$ echo 1649687307 | jq "todate"
"2022-04-11T14:28:27Z"
```
