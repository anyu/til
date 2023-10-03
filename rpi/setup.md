# RPI Setup

## Requirements

- power supply
- ethernet
- mac SD card adapter

## Flash rpi OS to SD card

### Use [Etcher](https://etcher.balena.io/) (easiest)

1. Download Raspbian or other OS from RPI official site
1. Follow etcher UI

### Manual
1. Download Raspbian or other OS from RPI official site
1. Tar unzip it: `tar -xvf raspbian-os.zip`
1. List mounted devices / space: `df -h`
1. Unmount sd card: `sudo diskutil unmount /dev/disk2s1`
1. Copy OS to SD card (name output ‘rdisk#’, don’t add remaining numbers)
`sudo dd bs=1m if=~/Downloads/raspbian-os.img of=/dev/rdisk2`
1. Wait until copy is done. Can use CTRL+T to check on status.

## Enable SSH to rpi

1. Touch empty ssh file in the `/boot` directory of the SD card to enable SSH
2. Edit `wpa_supplicant` file with Wifi info (or create if doesn’t exist):
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
  Note: If you create a `wpa_supplicant.conf` file in `/boot`, it will be copied to the main partition's `/etc/wpa_supplicant` location at boot time,replacing whatever is there. It will then be deleted from `/boot`, so you won't see it there if you go looking.

3. List connected devices: `diskutil list`
4. Safely eject SD card: `sudo diskutil eject /dev/rdisk2`

## SSHing into rpi
1. Insert SD card
1. Connect ethernet to laptop (that’s connected to WiFi)
  - Laptop might need to enable Internet Sharing in settings
1. Connect power to RPI last (give it 1 min to boot)
1. Scan for rpi on network (should be raspberrypi.local): `arp-a   // or ifconfig`
1. SSH: `ssh pi@raspberrypi.local // ѕѕh pi@192.168.2.2`
1. If needed, download lxsession/Vim/Chromium
1. SSH with -X and lxsession for GUI: `ѕѕh -X pi@192.168.2.2 lxѕеѕѕіоn`
1. Test for internet access: `ping www.google.com`

## Connecting via Wifi

1. `sudo raspi-config` > `System Options` > `Wireless LAN` > enter wifi info