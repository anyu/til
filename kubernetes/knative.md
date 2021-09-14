Options for deployment in the Kubernetes ecosystem:
- vanilla k8s primitives
- Helm
- Knative

---

# Knative

Knative consists of 3 core components: Build, Serving, Eventing.

## Knative Build
- used to build images from source to containers efficiently
- implemented via CRDs

## Knative Serving
- builds on k8s and Istio to support deploying/serving containers
- features:
  - fast serverless container deployment
  - autoscaling
  - routing for Istio components
  - deployment snapshots
- defines CRD objects: Service, Route, Configuration, Revision

## Knative Eventing
- provides global event subscription/delivery/management capabilities
- event producers and event consumers are independent

---

Misc
- currently, Knative Serving does not support multiple containers (more than 1 port per Service) that can handle requests simultaneously
