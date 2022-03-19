# Debugging Kubernetes

- Containers in a pod are started in parallel, can't define that one starts before the other (though can consider [Init Containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/)

If creating Ingress resource fails
```
kubectl delete -A ValidatingWebhookConfiguration ingress-nginx-admission
```

### Init containers don't complete

Your pod has the following status: `Init:0/X`:
```
NAMESPACE            NAME                                   READY   STATUS            RESTARTS   AGE
cert-manager         pod-a-001                              1/1     Running           0          6d2h
default              pod-b-001                              0/3     Init:0/2          0          13m
default              pod-b-002                              0/3     Init:0/2          0          19m
```

This means two [init containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/) did not complete.

```shell
kubectl describe po POD_NAME
```

Look for the Init Containers section
```shell
...
Init Containers:
some-agent-init:
Container ID:  docker://some-id
...
```
Check out logs of the init container:
```shell
# CONTAINER_NAME = some-agent-init
kubectl logs POD_NAME -c CONTAINER_NAME
```

May see errors:
```shell
2022-03-17T21:48:11.322Z [ERROR] auth.handler: error authenticating:
error=
| Error making API request.
|
| Code: 400. Errors:
|
| * IAM Principal "arn:aws:sts::some-arn-string" does not belong to the role "some-role"
```
