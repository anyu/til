# Security Rules

NACLs vs Security groups vs WAFs

## NACLs (network ACL)
- "firewall at subnet level"
- stateless firewall attached to subnets; must separately create rules to allow return traffic
- can only allow/block packets based on IP and port
- applied to traffic going in/out of a subnet
- tricky to use, try to avoid?

## Security Groups
- considered "stateful firewalls" that are attached to instances or LBs
  - stateful meaning it tracks outbound connections and allows return traffic through (in other words, they remember if a connection was initiated by the EC2 instance or from outside and temporarily allow traffic to respond without having to modify the inbound rules.)
- automatically creates temporary rules to allow return traffic from a TCP connection
- default config blocks all inbound traffic, allows all outbound

## WAFs (web application firewall)
- blocks HTTP traffic to/from a web app; inspects HTTP traffic
- differs from a regular firewall in that a WAF can filter the content of specific web applications while normal firewalls are between servers.

## Comparisons
- between subnets: route table specifies how traffic flows; NACL would specify what packets are allowed to flow
- inside a subnet: only the security group can have an effect
- order of events: NACL may be the first line of defense where an outside packet reaches first -> once allowed inside, route table is checked -> if it proceeds, security group rules are checked
