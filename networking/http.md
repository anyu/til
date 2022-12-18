# HTTP

## A Simple HTTP Transaction

1. **DNS Lookup**: The client tries to resolve the domain name for the request.
Client sends DNS Query to local ISP DNS server.
DNS server responds with the IP address for hostname.com

2. **Connect**: Client establishes TCP connection with the IP address of hostname.com
Client sends SYN packet.
Web server sends SYN-ACK packet.
Client answers with ACK packet, concluding the three-way TCP connection establishment.

3. **Send**: Client sends the HTTP request to the web server.

4. **Wait**: Client waits for the server to respond to the request.
Web server processes the request, finds the resource, and sends the response to the Client. Client receives the first byte of the first packet from the web server, which contains the HTTP Response headers and content.

5. **Load**: Client loads the content of the response.
Web server sends second TCP segment with the PSH flag set.
Client sends ACK. (Client sends ACK every two segments it receives. from the host)
Web server sends third TCP segment with HTTP_Continue.

6. **Close**: Client sends a FIN packet to close the TCP connection.


