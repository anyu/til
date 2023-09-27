# Upgrading RPI OS in place

How to upgrade to the latest RPI OS from within RPI

```sh
# Update software repository list
sudo apt update

# Run full upgrade of installation
sudo apt dist-upgrade -y

# Update RPI firmware
sudo rpi-update 
# Reboot RPI when complete

# Open sources.list
sudo nano /etc/apt/sources.list

# Change `buster` to `bullseye` (or whatever new version)
deb http://raspbian.raspberrypi.org/raspbian/ buster main contrib non-free rpi
# CTRL+X, Y, Enter to save and exit

# Update Bullseye software repository list
sudo apt update

# Run another distribution upgrade to install the Bullseye software requirements.
sudo apt dist-upgrade

# If errors with "libc6-dev : Breaks: libgcc-8-dev...", then run command below & rerun dist-upgrade
# sudo apt install gcc-8-base 

# Clean up installation files
sudo apt autoclean

# Reboot RPI
sudo reboot
```

