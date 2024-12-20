# Misc

Apply values of Column A (starting from row 2 to row 10) to another column, prefixed by link:
```
=ARRAYFORMULA("https://some_link.com?q=" & A2:A10)
```