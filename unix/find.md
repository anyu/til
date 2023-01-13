# find

### Find files in directory with most # of lines - top 10

```sh
find . -type f -print0 | xargs -0 wc -l | sort -n | tail -10
```

eg. excluding particular folders/filenames + including particular file types:

```sh
find . -not -ipath "*./folder_to_exclude/*" -not -name "*test*" -name ".py" -type f -print0 | xargs -0 wc -l | sort -n | tail -10
```