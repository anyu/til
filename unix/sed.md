# sed


### Replace all instances of keyword in a file

Escape special chars
```sh
sed 's/target\.com/target/g' input.txt > output.txt
```

### Execute multiple expressions with single command

`-e`: multiple exxpressions

- Replaces `target.com` with `target`
- Replaces `another_target` with empty string

```sh
sed -e 's/target\.com/target/g; s/another_target//g' input.txt > output.txt
```

### Format IP ranges

Given a file with a list of IP ranges in a line, eg:

input.txt:
```
16.128.0.0/12205.252.30.0/22183.62.249.0/22
```

Get each on new line

output.txt:
```
16.128.0.0/12
205.252.30.0/22
183.62.249.0/22
```

```sh
sed 's/\([0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\/[0-9]\{1,2\}\)/\n\1/g' input.txt > output.txt
```

With sort
```sh
sed 's/\([0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\/[0-9]\{1,2\}\)/\n\1/g' input.txt | sort > output.txt
```