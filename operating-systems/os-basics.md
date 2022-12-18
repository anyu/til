# OS Basics

- A program that manages the computer hardware. Hides the hardware complexity.
Intermediary between computer user/applications and computer hardware (CPU, memory, peripheral devices-input/output/storage devices)
- There's not really one definition of an OS
- Usually defined as the kernel - the one program running at all times on the computer
eg. Microsoft sued for including too much functionality in its OS (they had included browser as part of OS) and preventing third party competition.

## What happens when you turn on a computer (at least Linux)
1. Power button pressed.
2. Motherboard sends a signal to power supply device.
3. Power supply provides the proper amount of electricity to the computer.
4. Once the motherboard receives the power good signal, it tries to start the CPU.
5. CPU resets all leftover data in its registers and sets up predefined values for each of them.
6. [some other things happen]
7. BIOS starts; after initializing and checking the hardware, the BIOS needs to find a bootable device. 
8. A boot order is stored in the BIOS configuration, controlling which devices the BIOS attempts to boot from. When attempting to boot from a hard drive, the BIOS tries to find a boot sector.
9. Bootloader loads kernel into memory