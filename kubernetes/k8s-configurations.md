# k8s configuration

Misc things on configuring k8s

## Healthcheck Probes

It's easy to shoot yourself in the foot if these aren't configured appropriately, eg.

- If a liveness probe timeout is too short, the container could be restarted repeatedly.

### Liveness Probe
- Is this container responsive?
- Tells k8s when to restart a container

**Recommendations**
- Avoid checking dependencies in liveness probes (should be very light w/ minimal latency fluctuations)
- Factor in container startup latency fluctuations over time (due to resource allocation, load increases, etc)
- Regularly restart containers to avoid surprises/changes in initialization

If a `livenessProbe` is NOT specified at all, the default behavior is that if the container is `Running`, it's considered "successful".

### Readiness Probe
- Is this container ready to accept traffic?
