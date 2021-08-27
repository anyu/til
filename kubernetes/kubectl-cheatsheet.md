# kubectl cheatsheet

### Contexts

```shell
$ kubectl config get-contexts

$ kubectl config use-context <CONTEXT>
```

### Namespaces

```shell
$ kubectl get ns
```

### Pods

```shell
$ kubectl get pods -n <NAMESPACE>

$ kubectl get pods --all-namespaces

$ kubectl get pods -l app=<LABEL>

$ kubectl describe pod <POD NAME> -n <NAMESPACE>
```

### Deployments

```shell
kubectl get deployments
```

### Services

```shell
kubectl get svc
```

### Secrets
```shell
$ kubectl get secrets
```

### Quick resource docs

```shell
$ kubectl explain deployment

KIND:     Deployment
VERSION:  apps/v1

DESCRIPTION:
     Deployment enables declarative updates for Pods and ReplicaSets.

FIELDS:
   apiVersion	<string>
     APIVersion defines the versioned schema of this representation of an
     object. Servers should convert recognized schemas to the latest internal
     value, and may reject unrecognized values. More info:
     https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources

   kind	<string>
     Kind is a string value representing the REST resource this object
     represents. Servers may infer this from the endpoint the client submits
     requests to. Cannot be updated. In CamelCase. More info:
     https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
   ...

```

```shell
$ kubectl explain pod.spec.containers.livenessProbe.httpGet.httpHeaders

KIND:     Pod
VERSION:  v1

RESOURCE: httpHeaders <[]Object>

DESCRIPTION:
     Custom headers to set in the request. HTTP allows repeated headers.

     HTTPHeader describes a custom header to be used in HTTP probes

FIELDS:
   name	<string> -required-
     The header field name

   value	<string> -required-
     The header field value
```

### Misc Debugging

```shell
$ kubectl cluster-info dump
```
