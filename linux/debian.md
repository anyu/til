# Debian

### Handy apt commands

Shows available versions for installation
```sh
$ apt list meson -a

Listing... Done
meson/oldstable,now 0.56.2-1 all [installed]
meson/oldstable 0.56.1-1~bpo10+1 all
```

Shows available versions for installation - more details
```
$ apt-cache policy SOME_LIB

meson:
  Installed: 0.56.2-1
  Candidate: 0.56.2-1
  Version table:
 *** 0.56.2-1 500
        500 http://raspbian.raspberrypi.org/raspbian bullseye/main armhf Packages
        100 /var/lib/dpkg/status
     0.56.1-1~bpo10+1 500
        500 http://archive.raspberrypi.org/debian buster/main armhf Packages
```

Check out sources list
```
$ sudo vi /etc/apt/sources.list
```
