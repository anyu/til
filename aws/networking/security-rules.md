# Security Rules

Security groups vs NACLs vs WAFs

## Security Groups
- considered "stateful firewalls" that are attached to instances or LBs
  - stateful meaning it tracks outbound connections and allows return traffic through
- automatically creates temporary rules to allow return traffic from a TCP connection

## NACLs (network ACL)
- stateless firewall attached to subnets; must separately create rules to allow return traffic
- can only allow/block packets based on IP and port
- applied to traffic going in/out of a subnet
- tricky to use, try to avoid?

## WAFs (web application firewall)
- blocks HTTP traffic to/from a web app; inspects HTTP traffic
- differs from a regular firewall in that a WAF can filter the content of specific web applications while normal firewalls are between servers.

## Comparisons
- inside a subnet: only the security group can have an effect
- between subnets: route table specifies how traffic flows; NACL would specify what packets are allowed to flow
- order of events: NACL may be the first line of defense where an outside packet reaches first -> once allowed inside, route table is checked -> if it proceeds, security group rules are checked
