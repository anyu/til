# DNS Lookup

[DNS Lookup: How a Domain Name is Translated to an IP Address](http://blog.catchpoint.com/2014/07/01/dns-lookup-domain-name-ip-address/)

1. Browser asks OS for IP address

2. OS stub resolver checks in cache
- OS has a DNS client (aka. stub resolver) – a simple resolver that handles all the DNS lookups for the OS. 
- DNS client looks in its cache – if it has the record it gives the information to the application. If it does not have it, it sends a DNS query (with recursive flag) to the recursive resolver 

3. OS Recursive Query to DNS Resolver
- The stub resolver sends DNS queries with the recursive flag to a specified recursive resolver (name server). (DNS server of your ISP).
  - For most users, their DNS resolver/DNS server is provided by their ISP, or they are using an OSS alternative such as Google DNS (8.8.8.8) or OpenDNS (208.67.222.222).
- Recursive query = the resolver must complete the recursion and the response must be either an IP address or an error.

4. DNS Resolver Iterative Query to the Root Server
- The resolver queries one of the root DNS servers for the IP of “www.google.com.”
- This query does not have the recursive flag and therefore is an “iterative query,” meaning its response must be an address, the location of an authoritative name server, or an error.

5. Root Server Response
- These root servers hold the locations of all of the top level domains (TLDs) such as .com, .de, .io, and newer generic TLDs such as .camera.
- It returns the location of the .com servers. The root responds with a list of the 13 locations of the .com gTLD servers, listed as NS or “name server” records.

6. DNS Resolver Iterative Query to the TLD Server
- Next the resolver queries one of the .com name servers for the location of google.com

7. TLD Server Response
- Each TLD server holds a list of all of the authoritative name servers for each domain in the TLD
- The .com gTLD server responds with a list of all of google.com’s NS records

8. DNS Resolver Iterative Query to the Google.com NS
- Finally, the DNS resolver queries one of Google’s name server for the IP of “www.google.com.”

9. Google.com NS Response
- This time the queried nameserver knows the IPs and responds with an A or AAAA address record (depending on the query type) for IPv4 and IPv6, respectively.

10. DNS Resolver Response to OS
- At this point the resolver has finished the recursion process and is able to respond to the end user’s OS with an IP address.

11. Browser Starts TCP Handshake
- OS provides the IP to the browser, which initiates the TCP connection to start loading the page. 

## Authoritative server vs. Recursive resolver
- Authoritative name servers store DNS record information – usually a DNS hosting provider or domain registrar. 
- Recursive name servers are the “middlemen” between authoritative servers and end-users because they have to recurse up the DNS tree to reach the name servers authoritative for storing the domain's records
