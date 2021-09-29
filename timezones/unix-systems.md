# Timezones in Unix systems

## Get date and timezone
```shell
$ date

Wed Sep 29 11:09:22 EDT 2021
```

## Get system timezone
```
$ sudo systemsetup -gettimezone

Time Zone: America/New_York
```

## Timezone files

`/etc/timezone` (only on some systems) - a text-based representation of the system's timezone.

`/etc/localtime` - a binary representation of the exact rules (daylight savings, leap days, etc) for calculating time relative to UNIX time (the kernal's representation).
May contain a symlink to the system's timezone.
- Applications read this when they first need timezone info
- used by `date` command

```shell
$ ls -l /etc/localtime

lrwxr-xr-x 42 root 19 Sep 19:21 /etc/localtime -> /var/db/timezone/zoneinfo/America/New_York
```

(`/usr/sharezoneinfo/...` in linux)
- `/etc/localtime` is essentially a symlink of `/usr/share/zoneinfo/$(cat /etc/timezone)`


## Changing system timezones

#### via systemsetup

```
sudo systemsetup -settimezone TIMEZONE
```

with `TIMEZONE` being a valid zone from:

```
sudo systemsetup -listtimezones
```

#### via /etc/localtime

```
rm /etc/localtime
```

```
ln -s TIMEZONE_PATH /etc/localtime
```

with TIMEZONE_PATH being a valid path from:
```
ls /var/db/timezone/zoneinfo
```
