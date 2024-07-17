# CLI

```sh
docker exec -it $MYSQL_CONTAINER_ID /bin/bash 
```

```sh
docker exec -it $(docker ps -q --filter ancestor="$MYSQL_IMAGE_NAME") /bin/bash 
```

```sh
mysql -uroot -proot
```

```
mysq
```

```
SHOW DATABASES
```

```
USE $DB
```

```
SHOW TABLES 
```