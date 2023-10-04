# RPI Setup

## Requirements

- rpi power supply
- mac SD card adapter
- ethernet cable (optionally)

## Flash rpi OS to SD card

1. Download the [Raspberry Pi Imager](https://www.raspberrypi.com/software)
1. Set hostname, pw, wifi, SSH in Advanced Options before flashing.

## SSH into rpi
1. Insert SD card into rpi
2. Connect power to RPI (give it 1 min to boot)
3. Try `ping raspberrypi.local` (default hostname, but may conflict if other rpis are on network)
4. If hostname not found, scan for rpi IP on network

    a) Use arp: `arp -a`

    b) Use nmap:
      - Get own IP (`ipconfig getifaddr en0` if wireless, `ipconfig getifaddr en1` if wired)
      - `sudo nmap -sn $IP/$IP_RANGE` eg `sudo nmap -sn sudo nmap -sn 10.100.3.71/24`. Should see:
        ```
        ...
        MAC Address: DC:A6:32:0E:2D:DD (Raspberry Pi Trading)
        Nmap scan report for 10.100.3.121
        ...
        ```
      - Try pinging the ip
5. `ssh pi@raspberrypi.local` (or eg. `ѕѕh pi@192.168.2.2`)

## Change hostname (to avoid conflicts)
1. `hostname` outputs current hostname
1. `sudo vi /etc/hostname`
1. `sudo reboot`

If run into network issues, also update in `/etc/hosts`

## Useful things to install

- [fzf](https://github.com/junegunn/fzf) for better history search



# Archived (old methods)

## Flash rpi OS to SD card


1. Download Raspbian or other OS from RPI official site
1. Flash OS

    a) Use [Etcher](https://etcher.balena.io/) and follow UI
    b) Manual:
      1. Download Raspbian or other OS from RPI official site
      1. Tar unzip it: `tar -xvf raspbian-os.zip`
      1. List mounted devices / space: `df -h`
      1. Unmount sd card: `sudo diskutil unmount /dev/disk2s1`
      1. Copy OS to SD card (name output ‘rdisk#’, don’t add remaining numbers)`sudo dd bs=1m if=~/Downloads/raspbian-os.img of=/dev/rdisk2`
      1. Wait until copy is done. `CTRL+T` to check on status.

## Enable SSH to rpi

1. Create an empty file named `ssh` (must have no extension) in the `/boot` directory of the SD card to enable SSH.
2. List connected devices: `diskutil list`
3. Safely eject SD card: `sudo diskutil eject /dev/$DEVICE_NAME`

## Enable Wifi on rpi

1. Edit `wpa_supplicant` file with Wifi info (or create if doesn’t exist):
  `sudo vi /etc/wpa_supplicant/wpa_supplicant.conf`
    
    ```sh
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    country=US
      
    network={
      ssid="YOURSSID"
      psk="YOURPASSWORD"
      key_mgmt=WPA-PSK
      <!-- scan_ssid=1 -->
    }
    ```
    **Note**: If you create a `wpa_supplicant.conf` file in `/boot`, it will be copied to the main partition's `/etc/wpa_supplicant` location at boot time,replacing whatever is there. It will then be deleted from `/boot`, so you won't see it there if you go looking.
    
2. Shouldn't need this, but can also add: `sudo raspi-config` > `System Options` > `Wireless LAN` > enter wifi info