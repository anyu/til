# Fastai on RPI

Installation steps from: https://qengineering.eu/install-pytorch-on-raspberry-pi-4.html (good as of Oct 2023)

## Requirements
- 64 bit OS
- `arch64-linux-gnu version` C++ compiler
- Bullseye required for PyTorch 2.0

## Check requirements

1. Check 32 or 64bit OS: `getconf LONG_BIT`
1. Check C++ compiler version: `uname -a`
1. Check gcc version: `gcc -v`
1. Check zram swap size: `free -m`; shouldn't be more than 3g? Less isn't a problem if you don't build PyTorch from scratch.

## Install PyTorch 2.0 by wheel

Check [repo](https://github.com/Qengineering/PyTorch-Raspberry-Pi-64-OS) for new wheels as Python versions upgrade over time.

```sh
# get a fresh start
$ sudo apt-get update
$ sudo apt-get upgrade

# install the dependencies (if not already onboard)
$ sudo apt-get install python3-pip libjpeg-dev libopenblas-dev libopenmpi-dev libomp-dev

# above 58.3.0 you get version issues
$ sudo -H pip3 install setuptools==58.3.0
$ sudo -H pip3 install Cython

# install gdown to download from Google drive
$ sudo -H pip3 install gdown

# Only for Bullseye
# download the wheel
$ gdown https://drive.google.com/uc?id=1mPlhwM47Ub3SwQyufgFj3JJ9oB_wrU5D

# install PyTorch 2.0
$ sudo -H pip3 install torch-2.0.0a0+gite9ebda2-cp39-cp39-linux_aarch64.whl

# clean up
$ rm torch-2.0.0a0+gite9ebda2-cp39-cp39-linux_aarch64.whl
```

### Test PyTorch installation
```sh
$ python3
Python 3.9.2 (default, Feb 28 2021, 17:03:44)
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> torch.__version__
'2.0.1'
>>> z=torch.ones((3,3), dtype=torch.float32)
>>> print(z.exp())
tensor([[2.7183, 2.7183, 2.7183],
        [2.7183, 2.7183, 2.7183],
        [2.7183, 2.7183, 2.7183]])
```

## Install fastai

```sh
pip3 install fastai --no-deps
```

### Test fastai installation

```sh
$ python3.9
>>> import torch
>>> import torchvision
>>> import fastai
from fastai.vision import *
```