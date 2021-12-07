# Wasm-based Envoy filter

## Proxy-Wasm
- Proxy-Wasm is a "proxy-agnostic application binary interface (ABI) standard" that specifies how proxies (host) and Wasm modules interact
   - These interactions are in the form of functions and callbacks
   - It's proxy-agnostic so can be used with other proxies, not just Envoy
- The Proxy-Wasm plugin gets distributed as a Wasm module (.wasm file)
- At runtime, the proxy loads every Wasm module (all .wasm files) into a unique, sandbox VM that's isolated from the host environment
- The proxy creates a separate replica of the Wasm VM for every thread on which the plugin will be executed

## Wasm-based Envoy filters with Proxy-Wasm
- Envoy uses a subset of a V8 VM for the module sandbox VMs
- Envoy uses a multi-threaded model: 1 main thread handles config updates + global tasks, worker threads proxy individual TCP connections/HTTP requests. Worker threads are independent from each other.
- All interactions between the Wasm filter and the host (Envoy Proxy) happens via callback functions provided by the Envoy Proxy Wasm SDK.

### Using the Envoy Proxy Wasm SDK

This includes 3 steps:
- Build code (which implements and uses the ABI)
- Compile code to Wasm
- Deploy the Wasm code to an Envoy proxy

### Wasm-based Envoy Filter Lifecycle

## Envoy Proxy Wasm Filter Lifecycle

All interactions between the Wasm module (aka. filter, plugin, extension) and the host (Envoy Proxy) happen via **callback functions** provided by the Proxy Wasm SDK (available in various languages, eg. [Rust](https://github.com/proxy-wasm/proxy-wasm-rust-sdk)), which implements the [Proxy-Wasm ABI specs](https://github.com/proxy-wasm/spec/tree/master/abi-versions/vNEXT#proxy_on_configure).

The following diagram illustrates the relationship between a Wasm module and its Envoy Proxy host:
![](assets/wasm-based-envoy-filter-lifeycle.png)
([source](https://docs.eupraxia.io/docs/how-to-guides/deploy-rust-based-envoy-filter/))

## Initialization

When the host loads the Wasm plugin, it invokes the [_start()](https://github.com/proxy-wasm/spec/blob/master/abi-versions/vNEXT/README.md#_start) function. `_start()` is a good spot for initializing state, such as setting logging levels. It's also where we register a Context (usually a RootContext).

## Contexts and Request Lifecycle

The `Context` base class of the [Proxy Wasm SDK](https://github.com/proxy-wasm/proxy-wasm-rust-sdk/blob/master/src/traits.rs) provides hooks/callbacks (eg. `onXXX(...)`) that are invoked as the Envoy Proxy goes through the filter chain.

Depending on the level of the filter chain your filter is inserted into, different callbacks are invoked.

Each callback returns a status that you can use to tell Envoy Proxy whether or not to pass the processing to the next filter.

There are two types of contexts available for [HTTP-level filter chains](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/http/http_filters):
- RootContext
- HTTPContext

(TCP/UDP-level filter chains have [StreamContexts](https://github.com/proxy-wasm/proxy-wasm-rust-sdk/blob/375a3664dfa5a1e65f8a0bd24041e1cf8c5425f4/src/traits.rs#L249-L299))

**RootContext**

The [RootContext](https://github.com/proxy-wasm/proxy-wasm-rust-sdk/blob/375a3664dfa5a1e65f8a0bd24041e1cf8c5425f4/src/traits.rs#L209-L247) is a singleton and has the same lifetime as the sandbox VM it's executed in (exists for the whole lifetime of the filter)

It's used for:
- initial setup configuration between the plugin and Envoy host
- interactions that outlive a single request

The RootContext has methods such as:
- `on_configure`: invoked when the plugin is loaded, used to pass in VM/plugin configs
- `on_vm_start`: invoked when the host starts the Wasm VM
- `on_tick`: a timer called on every tick period

**HTTPContext**

Over the life of a filter, there will likely be many HTTP request/ response exchanges -- each of those exchanges gets its own [HTTPContext](https://github.com/proxy-wasm/proxy-wasm-rust-sdk/blob/375a3664dfa5a1e65f8a0bd24041e1cf8c5425f4/src/traits.rs#L301-L528). An HTTPContext is active for as long as one of those HTTP exchanges lasts and is destroyed afterwards.

The HTTPContext has methods such as:
- `on_http_request_headers`: invoked when HTTP request headers are received
- `get_http_request_headers`: gets HTTP request headers
- `set_http_request_headers`: sets HTTP request headers


> Check out the [HelloWorld filter](https://github.com/proxy-wasm/proxy-wasm-rust-sdk/blob/master/examples/hello_world.rs) for a baseline example.


## Resources

- [Proxy Wasm ABI spec](https://github.com/proxy-wasm/spec/tree/master/abi-versions/vNEXT)
- [Proxy Wasm SDK - Rust](https://github.com/proxy-wasm/proxy-wasm-rust-sdk/blob/master/src/traits.rs)
- [How to write Wasm filters for Envoy](https://banzaicloud.com/blog/envoy-wasm-filter/)
- [Tetrate-Episode 07: Developing Envoy Wasm Extensions](https://youtu.be/JIq8wujlG9s?t=1137)
- [Envoy Wasm Filters in Rust](https://martin.baillie.id/wrote/envoy-wasm-filters-in-rust/)
