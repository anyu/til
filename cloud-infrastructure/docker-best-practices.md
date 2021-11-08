# Docker best practices
- https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
- https://cloud.google.com/architecture/best-practices-for-building-containers

Rule of thumbs.

- 1 container = 1 app
  - if have multiple apps, they may be in different states. A container could be running but have an unresponsive core component.
- Optimize for the Docker build cache
  - Docker reuses a layer from previous build if it hasn't changed
  - Put build steps that change most often at bottom of Dockerfile
  - Since build layers may be re-used, if a build step relies on cache, the cache must be generated in the same step or it'll be out of date.
    eg.
    ```
    FROM debian:9

    RUN apt-get update && \
      apt-get install -y nginx
    ```
    instead of
    ```
    FROM debian:9

    RUN apt-get update
    RUN apt-get install -y nginx
    ```

- Remove unneeded tools to reduce attack surface area
- Build the smallest image possible
  - faster upload/download times (important for cold starts in k8s pods)
  - use the smallest base image possible
- Use [multi-stage builds](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#use-multi-stage-builds)
  - app is built in a "build" container, and result is used in another (shares same Dockerfile)
  - eg.
    ```
    FROM golang:1.10 as builder

    WORKDIR /tmp/go
    COPY hello.go ./
    RUN CGO_ENABLED=0 go build -a -ldflags '-s' -o hello

    # Results in a single layer image
    FROM scratch
    CMD [ "/hello" ]
    COPY --from=builder /tmp/go/hello /hello
    ```
  - Minimize the number of layers
    - Only `RUN`, `COPY`, `ADD` create layers. Other instructions create temporary intermediate images, that do not increase build size
  - Sort multi-line arguments for readability
  - Use a `WORKDIR` instead of proliferating `cd`'s; use absolute paths for `WORKDIR`
  - Avoid running processes as root inside containers

## Exemplary examples

- [go](https://hub.docker.com/_/golang/)
- [ruby](https://hub.docker.com/_/ruby/)

# Docker Tips

- Create/use Dockerfile without persisting it
  ```sh
  docker build -<<EOF
  FROM busybox
  RUN echo "hello world"
  EOF
  ```

- Use `ENV` to update `PATH` var to make container easier to use
  - `ENV PATH=/usr/local/nginx/bin:$PATH` so `CMD ["nginx"]` just works
