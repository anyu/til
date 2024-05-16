# AWS Load Balancers

## AWS Elastic Load Balancing (ELB)

- load balances for EC2
- can be integrated with EC2 auto scaling
- 3 main components:
	- **listeners**: what the client connects to. There can be many listeneres for a single LB.
	- **target groups**: the backend server to direct traffic to. Each target group needs a health check defined
	- **rules**: used to associate a target troup to a listener. Made up of a condition for the client (eg. client source IP) and a condition to decide which target group to send traffic to

### Application Load Balancer (ALB)

- for HTTP/HTTPS traffic
- routes traffic based on request data
- sends responses directly to client
- a security group needs to be configured to prevent traffic from reaching it
- has sticky sessions based on HTTP cookies
- can be used for authentication

### Network Load Balancer (NLB)

- for TCP/UDP/TLS
- supports static and elastic IPs
- handles millions of RPS (ALBs need to be scaled to reach this)
- preserves source IP address (whereas with ALB, the source IP is the ALB's IP)
- has sticky sessions based on client IP instead of cookie