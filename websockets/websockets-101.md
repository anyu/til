# WebSockets

An API that enables bidirectional communication between a client and server.

Enables the connection between the client and server to stay open.

## History
- With HTTP/1, request response cycles are 1:1; connection closes after the request
- AJAX enabled clients to make a request and receive a response without a page reload, but doesn't let servers send data without a request to do so
- WebSockets build on top of TCP

## How it works

- WebSocket handshake = request contains an 'upgrade header' (a request for the server to switch to WebSocket protocol) -> server responds with 101 header to confirm the protocol switch -> WebSocket is opened
- Once connection is established, client and server can both send data whenever, unprompted by the other

## WebSockets vs HTTP/2
- HTTP/2 doesn't fully replace WebSockets
- TODO

### Resources
- [What I learned about WebSockets...](https://medium.com/@jamesbrown5292/what-i-learned-about-websockets-by-building-a-real-time-chat-application-using-socket-io-3d9e163e504)
- [WebSockets vs. HTTP/2 vs. SSE Compared](https://linuxhint.com/websockets-http-2-sse-compared/d)
