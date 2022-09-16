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

If app container isn't able to connect to other service (eg. DB),
might have to connect via the DB's service name rather than localhost:
(error: `cannot assign requested address`)


```sh
postgresql://postgres-dev:[~secret~]@localhost:5432/dev
```

```sh
postgresql://postgres-dev:[~secret~]@db:5432/dev

```