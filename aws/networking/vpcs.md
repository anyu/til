# AWS VPC (Virtual Private Cloud)
A VPC is essentially an isolated virtual network (akin to a traditional local data center) that has a specified IP range.

VPCs are regional services (spans all AZs in a region)

- Each VPC can be given an IP range
- A VPC has a router that uses the route table, which controls where traffic is directed

## Availability Zone (AZ)
An AZ is essentially a discrete data center within a region.

## Subnet
A subnet is essentially a range of IP addresses.

IP addresses are assigned to resources within the VPC (eg. EC2 instances, NAT gateways, NLBs, etc)

- A subnet must live within a single AZ
- An AZ can have multiple subnets
- A subnet can only be assigned 1 route table, the set of rules that specify allowed routes for outbound traffic
- A subnet can be public, private, or VPN-only

### Public Subnet
- A public subnet is a subnet that can access the Internet.
- It has a route table entry that points to an internet gateway.
- Resoureces that need to receive Internet traffic would need to be added to a public subnet.

### Private Subnet
- A private subnet is a subnet that cannot access the Internet.
- It doesn't have a route table that points to an internet gateway.

### VPC only Subnet
- Traffic is routed to a site-to-site VPN connection through a virtual private gateway

### Subnet Security
- A security group can be assigned to a subnet to control the traffic for instances within a subnet.
- Network ACLs can also be used to control subnet traffic
- Using both provides more defense

## Gateway
A gateway connects a VPC to another network.

### Internet Gateway
- An internet gateway allows inbound and outbound access from a VPC to the internet.

### NAT Gateway (Network Address Translation)
**different from a NAT instance

A NAT gateway is an AWS managed service created in a specific AZ.

Both connectivity types of NAT gateways map the source private IP  > private IP of the NAT gateway. For public NAT gateway, the internet then maps the private IP of the public NAT gateway to the elastic IP associated with the NAT gateway.

#### NAT gateways with Public connectivity type
**the more common use case**

- (should be the same thing as a NAT gateway placed in a public subnet w/ a public IP)
- Enables private subnet resources to connect to the internet (but cannot receive unsolicited inbound internet traffic) or to other VPCs
- Translates private subnet private IPs into a public address that's used to connect to the internet
- To connect to other VPCs, you'd route traffic from the NAT gateway through a transit gateway or virtual private gateway
- This is generally configured in a route table entry as `0.0.0.0/0` destination with `ngw-########` target

#### NAT gateways with Private connectivity type
- Enables private subnet resources to connect to other VPCs
- You can route traffic from the NAT gateway through a transit gateway or virtual private gateway
- You can't associate an elastic IP with a private NAT gateway
- You can technically attach an internet gateway to a VPC with a private NAT gateway, but if you try to route traffic from the private NAT gateway to the internet gateway, the internet gateway drops the traffic

## VPC Peering
- VPC peering can route traffic between 2 private VPCs.

## Route Tables

Route tables are a set of rules (aka routes) that determine where to direct traffic from a subnet or gateway.

- a route table entry has a **destination* (the IP range for traffic to go, and a **target** (the gateway or connection through which to send the traffic))
- multiple routes can match, but the most specific route wins
- if a subnet does not have a route table associated with it, it implicitly uses its VPC's route table
- each subnet can only be associated with 1 route table.

### Default route
- The entry with `0.0.0.0/0` destination is the default route (target should be an internet gateway)
- Any traffic with a destination that doesn't match the other routes is sent to the default gateway, which forwards to the internet.

### Local route
- A `local` route is a type of route that enables communication **within** the VPC.
- By default, every VPC has at least the `local` route (can't be deleted)
- If the VPC has `172.16.0.0/16` range, the local route would be the same.

### NAT gateway route
- Generally configured as `0.0.0.0/0` destination with `ngw-########` target

### Common Patterns
- 1 route table for whole VPC:
  - for simple environments with only public subnets all pointing to 1 VPC internet gateway; no complex routing rules
- 1 route table per subnet:
  - each subnet has 1 route table assigned; 1:1 relationship between route tables and subnets within the VPC
- 2-tier routing tables (1 for public subnets, 1 for private subnets)
  - best practice for envs broken into public/private subnets
  - requires further separating route tables into AZs
- Routing between multiple VPCs (VPC peering)
  - VPC peering lets 1 VPC request a peering connectiong with another VPC (or within another AWS account); the other VPC must acept the request; then a new route needs to be added to each route table in each VPC
    - This is done by adding a route with the other VPC’s CIDR range as the Destination, and then the `pcx ID` of the peering connection as the Target
  - The subnets in each VPC can't overlap with each other

## NACL (Network Access Control Lists)

- A NACL is a subnet-level firewall controlling traffic in/out of subnets
- Perhaps more used to isolate different envs in 1 AWS account