# kubectl cheatsheet

### Contexts

```shell
$ kubectl config get-contexts

$ kubectl config use-context CONTEXT
```

### Namespaces

```shell
$ kubectl get ns
```

### Pods

```shell
$ kubectl get pods -n NAMESPACE

$ kubectl get pods --all-namespaces

$ kubectl get pods -l app=LABEL

$ kubectl describe pod POD_NAME -n NAMESPACE

$ kubectl logs POD_NAME -n NAMESPACE -c CONTAINER

```

### Events

```shell
kubectl get events
```

### Deployments

```shell
kubectl get deployments

kubectl apply -f deployment.yaml
```

### Services

```shell
kubectl get svc
```

### Secrets
```shell
kubectl get secrets

kubectl describe secret SECRET_NAME -n NAMESPACE

# Get value of secret
kubectl get secrets/SECRET_NAME -n NAMESPACE -o json

# Check cert
openssl x509 -in <(kubectl -n NAMESPACE get secret \
  SECRET_NAME -o jsonpath='{.data.tls\.crt}' | base64 -d) \
  -text -noout
```

```
kubectl get Certificate --all-namespaces -oyaml
```



### Volumes

```shell
kubectl exec POD_NAME -n NAMESPACE -c CONTAINER_NAME -- /bin/cat /path/to/shared/volume/file
```

### Proxy to hit kube-api directly

Creates a proxy server (an application-level gateway) between localhost and k8s api server
- incoming traffic enters one port and gets forwarded to the remote k8s api port

```shell
kubectl proxy --port=3000
```

### Apply a k8s config

```shell
cat <<EOF | kubectl apply -f -
kind: Namespace
apiVersion: v1
metadata:
name: my-cool-ns
EOF
```

---

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

### List K8S api endpoints

```sh
✗  kubectl api-resources
NAME                              SHORTNAMES   APIVERSION                             NAMESPACED   KIND
bindings                                       v1                                     true         Binding
componentstatuses                 cs           v1                                     false        ComponentStatus
configmaps                        cm           v1                                     true         ConfigMap
endpoints                         ep           v1                                     true         Endpoints
...
```

### Misc Debugging

SSH into pod
```shell
kubectl exec -it POD_NAME -n NAMESPACE -c CONTAINER_NAME -- /bin/bash
```

```shell
$ kubectl cluster-info dump
```
