# Docker Debugging

Keep container running without getting terminated
```
ENTRYPOINT ["tail", "-f", "/dev/null"]
```

Connect to the container to debug

```sh
docker container ls
```

```sh
docker exec -it $CONTAINER_ID /bin/bash
```
