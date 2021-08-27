# comm

Built-in Unix file comparison tool.

Note: Both inputs must be sorted. If not, sort 'em.

---

Print 3 columns: lines only in file1, lines only in file2, lines in both:
```shell
$ comm FILE1 FILE2
```

Print only lines common to both files:
```shell
$ comm -12 FILE1 FILE2
```

Get only lines found in file1:
```shell
$ comm -23 FILE1 FILE2
```

Get only lines found in file1; pipe to some comand:
```shell
# {} = each line input
$ comm -23 FILE1 FILE2 | xargs -I {} echo ${}
```

Print only lines common to both files, once sorted:
```shell
$ comm -12 <(sort FILE1) <(sort FILE2)
```
