# Istio

Three ways to install Istio:
- Helm (no longer recommended)
- Istioctl
- Istio operator - manages lifecycle, but has some light security concerns

## Istio and Envoy

- Istio relies on Envoy for L7 traffic management.
- Istio itself is a control plane for a fleet of Envoy Proxies