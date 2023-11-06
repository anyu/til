# TUN/TAP

### What's a network tunnel

A way to for transport data across a network using protocols that are not supported by that network.

It works by **encapsulating packets** (wrapping packets inside other packets).

Encapsulation use case examples: 
- encapsulate IPv6 packets inside IPv4 packets through a network that only supports IPv4
- encapsulate encrypted network packet inside an unencrypted packet so it can travel across networks

### What's a tun device?

TUN (short for network TUNnel) is a **virtual interface** that essentially implements a software version of a network by emulating physical devices (eg. Ethernet or WiFi interface cards)

It operates on **Layer 3** of the OSI model (network layer), so can handle IP packets.

It can be used to **route traffic** through a tunnel, so it's good for VPN functionality.

It lets applications read and write to this network inferface.

Note that no ethernet headers are added via TUN.

#### How to create a TUN interface

With `ip`

```sh
$ sudo ip tuntap add name tun0 mode tun user $USER
```

With `tunctl` (less common, less general purpose?)
```sh
$ sudo tunctl -t tun0
```

### What's TAP?

TAP is similar to TUN, but works at **Layer 2** (datalink layer), so carries Ethernet frames.

It's used to create virtual Ethernet devices that behave like physical network interfaces. These virtual devices can be bridged with physical network interfaces or other TAP devices, allowing them to communicate as if they were connected to the same physical network.

### Resources
- **TUN/TAP**:
  - https://www.gabriel.urdhr.fr/2021/05/08/tuntap/#tun-vs-tap
  - https://backreference.org/2010/03/26/tuntap-interface-tutorial/index.html