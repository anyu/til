# Dockerfiles

### Changing timezone

Set TZ env var in Dockerfile, update time files:
```shell
ENV TZ=America/New_York
RUN echo $TZ > /etc/timezone \
  && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime
```

or use `dpkg-reconfigure`, if tzdata is available:

```shell
ENV TZ=America/New_York
RUN echo $TZ | tee /etc/timezone \
  && dpkg-reconfigure --frontend noninteractive tzdata
```

#### at runtime
```shell
docker run -it -e TZ='America/New_York' ubuntu
```

#### via docker-compose
Mount host files to container files

```shell
# ro = read-only keyword
volumes:
  - "/etc/timezone:/etc/timezone:ro"
  - "/etc/localtime:/etc/localtime:ro"
```
