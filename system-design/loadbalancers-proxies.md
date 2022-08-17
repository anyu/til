# Network Load Balancers and Proxies

Generally interchangeable terms.

## Overview

### Load Balancer Functions
- Service discovery
- Healthchecks
- Load balancing
- Observability
- Security

### Benefits
- Abstracts naming of backends
- Fault tolerance
- Performance and cost benefits

## L4, L7 Load Balancing

These terms get muddled because they may overlap.

### L4 (TCP/UDP layer)
- simple, pervasive
- cons: not aware if client A is sending a ton of requests and client B isn't; backend selected for client A may be handling much more load than backend selected for client B

### L7 (application layer)
- can distribute load from same client for different HTTP calls

## Load Balancer Architectures

- **Middle proxy**: Client -> LB -> Backends
  - single point of failure
- **Edge proxy**: Client -> Internet -> LB -> Backends
  - like an API gateway
  - single point of failure
  - typically unavoidable for Internet-facing distributed systems
- **Embedded client library**: Service + client library -> Backend
  - LB is embedded directly into service via a library (eg. Finagle, Hystrix)
  - distributes LB functionality to each client
  - library upgrades can be painful
- **Sidecar proxy**: Service <-> sidecar proxy -> Backend
  - popularized as "service mesh" (eg. Envoy, NGINX, HAProxy, Linkerd)
  - get benefit of embedded library w/o language lock-in, at a slight latency cost

Most large distributed architectures use a two-tiered L4/L7 system for Internet traffic.

L7 LBs will likely replace L4 LBs for service-to-service communication, but L4s are still very relevant at the edge.

L4s are beneficial at the edge over L7 LBs because:
- L4 LBs are more performant/can handle more traffic due to less operations
- L7 LBs tend to be more actively developed, deployed more often -> more bugs


---

#### Resources

- https://blog.envoyproxy.io/introduction-to-modern-network-load-balancing-and-proxying-a57f6ff80236
