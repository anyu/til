# JA3

**TLDR**
- A form of TLS fingerprinting that looks at TLS Client Hello attributes.
- Combines attributes into **JA3 hash**, a 32 char hexadecimal string
- Developed by Salesforce in 2017

**JA3** is a method used to create a unique fingerprint for TLS clients based on the way they negotiate their connection with a server. It captures specific details of how a client establishes a secure connection, which can be used to uniquely identify traffic even if the client tries to hide its identity using techniques like changing the **User-Agent (UA)** or other forms of obfuscation.

## What is JA3?

- **JA3** generates a fingerprint by examining parameters in the **TLS handshake** (specifically the [TLS Client Hello](https://tls12.xargs.org/#client-hello) packet) These parameters include:
  - Cipher suites (used for encryption)
  - Extensions (such as supported protocols and encryption methods)
  - The order of the extensions
  - Supported elliptic curve groups
  - Supported elliptic curve point formats
- These elements are combined into a hash (the **JA3 hash**), resulting in a 32-character hexadecimal string that uniquely identifies the fingerprint of a TLS client.

## Why look for JA3 Instead of just UA?

1. **UA Strings Can Be Easily Spoofed**:
   - The **User-Agent** string is used to identify the browser or client making the request (eg. "Mozilla/5.0"). However, this string can be easily modified or spoofed, making UA unreliable as a unique identifier. Many malicious actors or tools can modify the UA to appear as a different browser or device.

2. **JA3 is Harder to Spoof**:
   - JA3 is harder to modify because it relies on low-level cryptographic parameters during the TLS handshake. To change the JA3 fingerprint, an attacker would have to modify how the client negotiates the TLS connection, which is more complex than modifying a simple string like UA.

3. **JA3 is More Persistent**:
   - JA3 fingerprints persist across sessions. Even if a client changes its IP address, browser version, or other identifiers, the JA3 fingerprint might remain the same as long as the cryptographic parameters in the TLS handshake remain unchanged.
   - UA strings can change between requests, browsers, and sessions, making them less reliable for tracking.

4. **Detecting Malicious Traffic**:
   - Since JA3 fingerprints are difficult to spoof, they can be used to detect **bot traffic**, **malicious actors**, or **anomalies** in a way that’s more resilient than relying on easily manipulated identifiers like User-Agent strings.
   - JA3 can also identify traffic from **known attack tools** like **malware**, **penetration testing frameworks**, or **automated scanners**, which tend to have distinct JA3 fingerprints.

5. **Effective for TLS Traffic**:
   - JA3 is especially useful in environments where **encrypted traffic** (such as HTTPS or other TLS-based protocols) is prevalent. As more web traffic becomes encrypted, relying on visible headers like the UA (which may not be present in encrypted traffic) becomes less effective.
   - JA3 can be used to track and fingerprint traffic even when it’s encrypted.

## Use Cases for JA3

- **Malware Detection**: JA3 fingerprints can be used to detect malicious traffic by recognizing signatures of malware communication or tools like **Cobalt Strike**, which have distinctive JA3 fingerprints.
- **Bot Detection**: Bots often have predictable JA3 fingerprints, which can be identified and blocked.
- **Threat Intelligence**: By collecting and analyzing JA3 fingerprints, defenders can correlate new attack patterns, detect **Command & Control (C2)** communication, and detect the use of **exploit kits**.
- **Network Traffic Analysis**: JA3 can be used as a method for **anomaly detection** in network traffic. If a sudden surge in traffic from a new or uncommon JA3 fingerprint is detected, it could indicate new or suspicious activity.

## Pros

- low computational footprint
- compatible with wide range of network configurations
- straightforward implementation
- OSS

## Limitations
- core weakness = lack of granularity and uniqueness, due to the limited client attributes from a ClientHello packet
- likely for different clients to have identical fingerprints
- lack of a single authoritative fingerprint DB creates fragmentation
    - different JA3 tools can produce slightly different JA3 fingerprints
- can still be spoofed via tools ike [curl-impersonate](https://github.com/lwthiker/curl-impersonate)

## Future

JA4+
- https://blog.foxio.io/ja4%2B-network-fingerprinting (2023)
- https://blog.foxio.io/ja4t-tcp-fingerprinting (2024)

### Resources
- https://github.com/salesforce/ja3
- https://engineering.salesforce.com/tls-fingerprinting-with-ja3-and-ja3s-247362855967/
- [Fastly TLS Fingerprinting](https://www.fastly.com/blog/the-state-of-tls-fingerprinting-whats-working-what-isnt-and-whats-next)