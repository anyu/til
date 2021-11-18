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

---

```shell
kubectl describe gateway/knative-ingress-gateway -n knative-serving
```

By default, Knative ships with a single ingress gateway.
- However, some installations (such as Google Cloud Run on GKE) ships with two separate gateways: one for internal traffic, one for external traffic.
- In Google Cloud Run on GKE, these gateways are deployed as Kubernetes Services in gke-system namespace named:
  - internal: cluster-local-gateway.gke-system.svc.cluster.local (type: ClusterIP)
  - external: istio-ingress.gke-system.svc.cluster.local (type: LoadBalancer, public)

By default, Knative uses Istio as the ingress gateway (load balancer).

This gateway is exposed externally to the world on a TCP/IP (Layer 3/4) load balancer created via Kubernetes Service (of type: LoadBalancer).

Knative requires an LB that understands L7 protocols (eg HTTP, gRPC)
- all traffic to KN services go through this LB (even pod to pod requests)
- this LB routes traffic to the right KN service via domain names, splits traffic based on revision, load balances betwen pods


https://www.triggermesh.com/blog/installing-knative-on-amazon-web-services-eks
https://events.istio.io/istiocon-2021/slides/b7p-PerformanceTuningKnative-GongZhang-YuZhuang.pdf

Installing Knative Serving and Knative Build

istio-system for the Istio components and the Ingress gateway that will receive Internet traffic
knative-serving for the Serving controller and autoscale
knative-build for the Build controller


## knative-serving components

When knative-serving is deployed, these are the components deployed:
```
$ kubectl get pods -n knative-serving
NAME                                     READY   STATUS    RESTARTS   AGE
activator-dfc4f7578-62c9f                2/2     Running   0          4m37s
autoscaler-756797655b-tz4c8              2/2     Running   0          2m31s
controller-7bccdf6fdb-kx5gj              2/2     Running   0          2m53s
domain-mapping-65fd554865-94kkg          2/2     Running   0          2m3s
domainmapping-webhook-7ff8f59965-ljqb6   2/2     Running   0          88s
webhook-568c4d697-hzh55                  2/2     Running   0          53s
```

Deploy the knative-istio-controller to integrate Istio and Knative:

Knative's net-istio controller creats a shared ingress Gateway called `knative-ingress-gateway` in the `knative-serving` namespace to service all incoming traffic to Knative.

The `net-istio` controller integrates with the default Istio gateway `istio-ingressgateway` in the `istio-system` namespace as its underlying gateway.

It adds the `net-istio-` components:
```
$ kubectl get pods -n knative-serving

NAME                                     READY   STATUS    RESTARTS   AGE
activator-dfc4f7578-62c9f                2/2     Running   0          7m32s
autoscaler-756797655b-tz4c8              2/2     Running   0          5m26s
controller-7bccdf6fdb-kx5gj              2/2     Running   0          5m48s
domain-mapping-65fd554865-94kkg          2/2     Running   0          4m58s
domainmapping-webhook-7ff8f59965-ljqb6   2/2     Running   0          4m23s
net-istio-controller-799fb59fbf-xtmwh    1/1     Running   0          59s
net-istio-webhook-5d97d48d5b-g7n6p       2/2     Running   0          59s
webhook-568c4d697-hzh55                  2/2     Running   0          3m48s
```

```
$ kubectl describe pod net-istio-webhook-5d97d48d5b-mwkgv -n knative-serving
```
