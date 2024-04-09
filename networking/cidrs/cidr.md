# CIDR (Classless Inter-Domain Routing)

CIDR is an IP address allocation method.

An IP address has 2 parts:
- the **network address**: digits pointing to a network's unique ID
- the **host address**: digits pointing to the host/individual device on the network

An IPv4 address has 32 bits. Each set of numbers separated by the period has 8 bits, represented by 0-255.

## Classful IPv4 addresses

- **Class A**: has 8 network prefix bits (eg. `44.0.0.1` where `44` = network address, `0.0.1` = host address
  - supports 2^24 = 16,777,214 hosts (minus the first and last, which are reserved)
- **Class B**: has 16 network prefix bits (eg. `128.16.0.2`, where `128.16` = network address, `0.2` = host address)
 - supports 2^16 = 65,534 hosts
- **Class C**: has 24 network prefix bits (eg. `192.168.1.100`, where `192.168.1` = network address, `100` = host address)
 - supports 2^8 = 254 hosts

Cons:
- limited and inefficient flexibility in allocating IPs (if you need 300 IPs, you'll need to apply for Class B addresses, which leaves a lot of unused spaces)

## Classless IPv4 addresses

"Classless" or CIDR addresses use subnet masks to change the ratio between the network and host address bits in an IP.

A **subnet mask** returns the **network address** from the IP by turning the host part into zeroes.

Useful to break down an IP address space to subnets of various sizes.
- Each subnet can have a flexible host count + limited # of IP addresses
- The "suffix" indicates the "prefix" bits for the network address.
- eg `/24` means the subnet mask is `11111111.11111111.11111111.00000000` (ie. `255.255.255.0`), with 1 representing the network portion and 0 representing the host portion.
  - `192.168.1.0/24` = the first 24 bits (`192.168.1`) is the network address portion
  - Since there's 1 octet (8 bits) available for host addresses, this allows up to 2^8 (256) host addresses (`192.168.1.0` to `192.168.1.255`)
  - NOTE: In reality, only 254 of the 256 are assignable because the first (ie. `192.168.1.0`) is reserved to represent the network address, and the last address (ie. `192.168.1.255`) is reserved for broadcast.

### CIDR block

A CIDR block is collection of IP addresses that share the same network prefix and # of bits.

## Resources

- IPv4 CIDR table: https://www.catalyst2.com/knowledgebase/networking/ipv4-cidr-table/