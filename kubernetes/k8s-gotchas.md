# Kubernetes Gotchas

- Containers in a pod are started in parallel, can't define that one starts before the other (though can consider [Init Containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/)
