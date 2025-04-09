# Prometheus 101

## Components
- **Prometheus server**: periodically collects metrics ("scrapes") from targets (server, pod, endpoints, etc) via pull model
    - looks for metrics at `/metrics` path of target
    - expects data in specific text format

- **Prometheus exporters**: agents that run on the targets; converts metrics to Prometheus expected format and exposes them at `/metrics`
x
### Service Discovery
Prometheus uses 2 methods to scrape metrics from targets:
1. **static configs**: When targets have a static IP or DNS endpoint.
2. **service discovery**: When targets don't have a static endpoint (as in distributed/autoscaling systems - eg. k8s); prom has to discover them and add the targets to the config.

### Prometheus Pushgateway
- A standalone component used for scenarios where metrics need to be **pushed** to Prometheus
- Batch jobs can push metrics to the pushgateway via HTTP API
- Pushgateway exposes those metrics also at `/metrics`

### Prometheus Clients
- Instrumentation libraries to expose metrics for Prom server to pull (they don't send metrics anywhere)