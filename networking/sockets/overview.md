# Sockets

There are 3 commonly used sockets: 
- **stream**: provides bidirectional, reliable, sequenced data flow (eg. TCP)
  - socket type = `SOCK_STREAM`
- **datagram**: provides bidirectional data flow, w/o order guarantee (eg. UDP)
  - socket type = `SOCK_DGRAM`
- **raw**: used by applications that need to interact directly w/ IP (eg. ping, RIP, OSPF)
  - socket type = `SOCK_RAW`