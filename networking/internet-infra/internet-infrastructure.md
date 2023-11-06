# Internet Infrastructure

**Internet, the Definition**: A global network of voluntarily interconnected, independent networks.

A network of networks.

---

## Overview

**ELIF**

- The Internet is made of up a bunch of computers. ISPs, universities, companies own the bunches.
- A bunch that belongs to one organization = an Autonomous System (AS). Each AS is assigned an ASN.
- Computers within an AS communicate *with each other* via **interior gateway protocols** (eg. RIP, OSPF).
- Computers communicate *with external* ASes via **border gateway protocol** (BGP).

## Internet Service Providers (ISPs)

**Types of ISP interconnect agreements**
- **Peering**: mutual exchange of data between entities (no upstream access)
  - "settlement-free" = unpaid arrangement
- **Transit**: one entity pays the other for the right to transit to its upstream network (hierarchy exists)
- **Customer**: pays for access

### Tier 1 networks

- Tier 1 networks can reach every other network on the internet without paying.
- Peers for free
- They own enough of the physical network infrastructure to carry most traffic themselves, so can negotiate with other Tier 1 networks for free access.
- Examples:
  - AT&T
  - T-Mobile (formerly Sprint)
  - Lumen Technologies (formerly CenturyLink, Level 3)
  - Verizon
  - Deustche Telekom

### Tier 2 networks

- Tier 2 networks peer for free with some networks, but may pay for peering or transit for others.
- Typically, they're regional or national providers
- Examples:
  - Comcast
  - China Telecom

### Tier 3 networks

- Tier 3 networks solely purchase transit/peering from other networks.
- Last mile providers to customers
- Examples:
  - Spectrum
  - Optimum
  - Verizon

## Internet Exchange Points (IXPs)

- Common locations where ISPs exchange data via public peering
- Generally located in places with pre-existing connections to multiple distinct networks (eg. datacenters)
- Mostly non-profits of its constituent ISPs
- The alternative to IXPs = private peering (ISPS directly connect to each other)
- Benefits of an IXP to ISPs: 1) cheaper than sending traffic to an ISP's upstream provider, 2) reduces latency

Examples:
- DE-CIX

### How an IXP works

- Typically an IXP consists of 1+ network switches, which each of the ISPs connect to
- Traffic exchange is usually through mutual peering agreements
- Traffic exchange is facilitated by BGP

## AS

- Each AS gets a number of IP ranges

## BGP

- BGP lets ASes announce themselves to the rest of the internet
- Finds the best routes to send traffic to any computer on the internet
- Without BGP, ASes are essentially just local networks
