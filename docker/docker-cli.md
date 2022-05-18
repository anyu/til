# Docker CLI

### View docker container logs

```
docker logs CONTAINER_NAME
```

### View Docker processes

```
docker ps -l
```

### Docker port already bound error

If it's a Docker process:

```shell
$ docker container ls

$ docker kill CONTAINER_ID
```

If not, check what process is running on that port

```
$ lsof -i :8000

COMMAND     PID USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
com.docke 10055 anyu   49u  IPv6 0xff714f4171cf93e1      0t0  TCP *:irdmi (LISTEN)
```
