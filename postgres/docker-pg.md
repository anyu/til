# Docker PG

Misc things about running Postgres in Docker

If app container isn't able to connect to other service (eg. DB),
might have to connect via the DB's service name rather than localhost:
(error: `cannot assign requested address`)


```sh
postgresql://postgres-dev:[~secret~]@localhost:5432/dev
```

```sh
postgresql://postgres-dev:[~secret~]@db:5432/dev

```