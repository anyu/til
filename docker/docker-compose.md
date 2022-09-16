# Docker Compose

By default, `docker-compose up` does not rebuild the Dockerfile image if it changed.
It'll use a cached version.

To rebuild the image:
```sh
docker-compose up --build
```

To recreate the container:
```sh
docker-compose up --force-recreate
```
