# Apple Silicon Chip comps

To temporarily open a zsh shell using emulated x86/intel architecture:
```sh
arch -x86_64 zsh
```

Confirm
```sh
$ uname -m

x86_64
```

To always open w/ Rosetta:

`Terminal` -> Right click `Get Info` > check `Open using Rosetta` > Restart terminal