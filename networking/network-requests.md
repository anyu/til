# Network requests

## Network timeouts

- Assume network to be unreliable
- Lots of request libraries don't set default timeouts
- Keep in mind users who may have worse connection speeds (eg. worse upload speeds)
- Set specific timeouts for each API call

### Connect timeouts

- How long client will wait for connection with a server to be established 
- The time for a client who began the TCP handshake and sent a `SYN` packet, to receive a `SYN/ACK` back
- Connect timeouts should be kept short

### Write timeouts

- How long to wait while client tries to send data
- Harder to decide timeout. For background tasks, can consider higher timeouts. For more immediate tasks, probably shorter timeouts. Think of how long to expect users to wait.

### Read timeouts

- How long to wait for client to receive response back from server
- Harder to decide timeout. For background tasks, can consider higher timeouts. For more immediate tasks, probably shorter timeouts. Think of how long to expect users to wait.

### Other timeouts

- first byte

---

TODO

- blocking vs non blocking operations