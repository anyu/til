# RPI Camera Module

Headless instructions

1. Turn off rpi
2. Connect camera module (pull up black cover, insert cam module with blue section facing USB ports, replace black cover)
3. Turn on rpi
4. SSH into RPI, run `sudo raspi-config` > `Interface Options` > `Camera` > `Enable`.
5. Take pic
  - newer rpi images (bullseye+): `libcamera-vid -t 0`
  - older rpi images: `raspistill -o test.jpg`

## Python camera library

Picamera2 lib: https://github.com/raspberrypi/picamera2
- Bullseye+