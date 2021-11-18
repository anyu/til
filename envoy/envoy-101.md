# Envoy

[Envoy](https://www.envoyproxy.io/) is an opensource edge and service proxy.

It's a programmable L4 and L7 proxy that uses a sidecar pattern (runs alongside every application) to abstract away the network component.

## Compared to NGINX, HAProxy

Envoy is often compared with NGINX, HAProxy. Some notes on each:

- NGINX's business model results in some tension between its commercial product and its OSS offering
- HAProxy is an older offering and has less forward community/velocity
- Envoy (released in 2016) was designed from the start for microservices

## Programming Envoy
- Envoy exposes APIs to dynamically configure the proxy (vs. using static files)
- **Listeners** can be configured to enable traffic flow through proxy
- **Filters** can enhance the data flow

<pre>
               ┌─────────────────────────────────────────────────┐
               │                                                 │
┌──────────┐   │  ┌──────────┐    ┌──────────┐    ┌──────────┐   │   ┌──────────┐
│ Listener │◀──┼─▶│  Filter  │◀──▶│  Filter  │◀──▶│  Filter  │◀──┼──▶│ Service  │
└──────────┘   │  └──────────┘    └──────────┘    └──────────┘   │   └──────────┘
               │                                                 │
               └──────────────────Filter chain───────────────────┘

</pre>

## Types of filters

- **Listener Filters**: access raw data, manipulate *metadata* of L4 connections during initial pre-connection phase.
- **Network Filters**: access and manipulate raw data on L4 connections, eg. TCP packets.
- **HTTP Filters**: operate at L7; access and manipulate HTTP requests/responses

## Creating filters

If the pre-built filters aren't sufficient, you can write your own.

#### Options:
- Native C++
- **Lua-based filter**: Use the existing HTTP Lua filter to add an inline Lua script (suited for less complex filters)
- **Wasm-based filter**: Create a filter as separate Wasm module, have Envoy dynamically load it during runtime. The options are:
  - a. Load Wasm module by pointing it to a local .wasm file accessible by the proxy
  - b. Use remote fetch and have Envoy download the .wasm file for you

### Resources
- [Why Ambassador Chose Envoy](https://blog.getambassador.io/envoy-vs-nginx-vs-haproxy-why-the-open-source-ambassador-api-gateway-chose-envoy-23826aed79ef)
- [How to Write Envoy Filters](https://blog.envoyproxy.io/how-to-write-envoy-filters-like-a-ninja-part-1-d166e5abec09)
- [Envoy: Life of a Request](https://www.envoyproxy.io/docs/envoy/latest/intro/life_of_a_request#overview)
