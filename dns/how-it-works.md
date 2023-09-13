# How DNS Works

## TLDR

You enter `google.com`:

1. Browser -> browser's DNS cache -> **DNS resolver** (aka. recursive nameserver) (ISP or 3rd party)
1. ISP DNS resolver -> own DNS cache -> DNS root name server, which returns the `.com` TDL nameserver address
1. ISP DNS resolver -> `.com` TLD name server, which returns the **authoritative** nameserver address that has a record for `google.com`.
1. ISP DNS resolver ->  authoritative nameserver, which returns the IP for the domain.
1. The browser finally makes an HTTP request to that IP address.

## The detailed explanation

You enter `google.com`:

1. The browser check its own browser cache to see if it already has the IP for this domain.
2. Next, the browser hands off responsbilitiy to the OS. Your OS checks the computer's hosts file, which is a local text file.

    `/private/etc/hosts`:

    ```
    ##
    # Host Database
    #
    # localhost is used to configure the loopback interface
    # when the system is booting.  Do not change this entry.
    ##
    127.0.0.1   localhost
    255.255.255.255 broadcasthost
    ::1             localhost

3. The OS queries the DNS resolver (aka. recursive nameserver) configured in your OS's network settings. This may be referred to the as the "browser DNS", but is usually by default just
the one in OS settings, which is likely the ISP DNS or a configured 3rd party DNS.

    `/private/etc/resolv.conf`
    
    ```
    nameserver 192.168.0.1
    ```

    TODO: Test changing DNS in settings and see if this file changes.

4. The ISP DNS resolver first checks its own cache. (TODO: Where is this located?)
5. The ISP DNS resolver starts the **DNS resolution process**. It queries one of 13[^1] main **root name servers** located wordwide, which provide information about the TLD name servers.
Most DNS servers are configured with a **root file** (or **root hint** file, `root.hits`) with the addresses of the root name servers.

    You can see the list via `dig . ns`.

    The 13 root name servers are named `A` to `M`, all have an IPv4 address, and most have an IPv6 address.
    ICANN manages these root servers, which are operated by different institutions.
    An info pages exists for each at `http://{letter}.root-servers.org` (eg. [a.root-server](https://a.root-servers.org/)

    Each root name server contains an identical copy of the **root zone file** (not to be confused with the `root.hints` file), which is updated very occasionally through an ICANN process.

5. The ISP DNS resolver queries the TLD name server, which returns the **authoritative** nameserver address that has an A record for `google.com`.
6. ISP DNS resolver queries that authoritative nameserver, which returns the IP for the domain.

## Terms in more detail


### Recursive nameservers
- A recursive name servers (aka DNS resolver) is like the middleman of DNS. It's involved in **every single DNS query**.
- It resolves DNS queries on behalf of clients and do not hold authoritative data themselves.
- They get answers from authoritative nameservers.

### Authoritative nameservers
- Authoritative nameservers hold the official DNS records for specific domains. The source of truth.

### Domain types

#### Apex domains

The `google` part = the apex domain.
https://vercel.com/docs/projects/domains#apex-domains

#### FQDN (fully qualified domain name)

The `google.com` part = the fully qualified domain name (FQDN)

`www` is actually a subdomain.

### Domain Records

#### CNAME = Canonical Name

- record that maps a hostname to another hostname

#### A record = authoritative record
- record that maps a hostname to an IP address

## Running Questions

- What happens when you have a domain with Namecheap, but want to have the domain point to your app hosted elsewhere? (eg. Vercel)
- Why are A records recommended over nameservers sometimes? eg. Vercel
- How do I use tools like dig, nmap, etc?
- When I try to access WiFi at a coffee shop, how do they make those little pop-ups come up where you have to take an action before being able to access the WiFi?
What's really happening under the hood?
- What is `broadcasthost`, `::1` entry in hosts file

### Misc interesting facts

DNS lookups to the root name servers are relatively infrequent. 
2003 - only 2% of root name server queries were legit.


- The IANA official root servers list: https://www.iana.org/domains/root/servers


