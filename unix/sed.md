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