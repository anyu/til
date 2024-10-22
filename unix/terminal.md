# Terminal

## Date - get current timestamp in UNIX

```shell
$ date +%s
1649687726
```

## Check what process is running on a port

```
$ lsof -i :8000

COMMAND     PID USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
com.docke 10055 anyu   49u  IPv6 0xff714f4171cf93e1      0t0  TCP *:irdmi (LISTEN)
```

## Redirecting output

```
          || visible in terminal ||   visible in file   ||

  Syntax  ||  StdOut  |  StdErr  ||  StdOut  |  StdErr  || existing file
==========++==========+==========++==========+==========++===========
    >     ||    no    |   yes    ||   yes    |    no    || overwrite
    >>    ||    no    |   yes    ||   yes    |    no    ||  append
          ||          |          ||          |          ||
   2>     ||   yes    |    no    ||    no    |   yes    || overwrite
   2>>    ||   yes    |    no    ||    no    |   yes    ||  append
          ||          |          ||          |          ||
   &>     ||    no    |    no    ||   yes    |   yes    || overwrite
   &>>    ||    no    |    no    ||   yes    |   yes    ||  append
          ||          |          ||          |          ||
 | tee    ||   yes    |   yes    ||   yes    |    no    || overwrite
 | tee -a ||   yes    |   yes    ||   yes    |    no    ||  append
          ||          |          ||          |          ||
 n.e. (*) ||   yes    |   yes    ||    no    |   yes    || overwrite
 n.e. (*) ||   yes    |   yes    ||    no    |   yes    ||  append
          ||          |          ||          |          ||
|& tee    ||   yes    |   yes    ||   yes    |   yes    || overwrite
|& tee -a ||   yes    |   yes    ||   yes    |   yes    ||  append
```

(source: https://askubuntu.com/a/731237)

## Fold

```
fold long_text.txt
```

Print contents broken up into lines <80 columns.
