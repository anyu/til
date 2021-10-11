# Kubernetes State

## Between containers in same pod

### Shared volumes

- Share data between containers on same pod:
    - can use a directory on the host that's shared w/ all containers in a pod
    - volumes enable data to survive container restarts, have same lifetime as a pod
    - if pod is deleted, shared volume is destroyed
- Standard use case:
    - 1 container writing to shared directory (eg. logs) so that other container can read it
- eg.
```yaml
volumes:
- name: html
  emptyDir: {} #initial empty volume created when Pod is assigned a node
containers:
- name: container-a
  image: nginx # nginx reads/serves files in the shared volume that container-b writes to
  volumeMounts:
  - name: html
    mountPath: /usr/share/nginx/html # shared volume mounted at this location for container-a
  - name: container-b
    image: debian
    volumeMounts:
    - name: html
      mountPath: /html # shared volume mounted at this location for container-b
    command: ["/bin/sh", "-c"]
    args:
      - while true; do
          date >> /html/index.html; # container writes to file in shared volume
            sleep 1;
          done
```
