# Postgres Commands

## Setup
```
brew install postgres
brew services start postgresql
# enter pysql interactive
psql postgres
```

## Roles

The `postgres` role may not have been created, verify via:

```
$psql postgres

postgres-# \du
                                   List of roles
 Role name |                         Attributes                         | Member of
-----------+------------------------------------------------------------+-----------
 postgres  | Superuser, Create role, Create DB                          | {}
```

If it's not there, use the `createuser` utility that comes with Postgres:

```
createuser postgres -s
```

Log in w/ a particular role
```
psql -U postgres
```

If already in postgres, switch role
```
set role ROLE
```

### Create DB

```
CREATE database DB_NAME;
```

### List DBs
```
\list
```

### Connect to DB
```
\c DB_NAME
```

### Create table

```
CREATE TABLE TABLE_NAME (
  id SERIAL NOT NULL PRIMARY KEY,
  name TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
);
```

### List tables
```
\d
```

### Describe table

```
\d TABLE_NAME
```

### Drop table

```
DROP TABLE TABLE_NAME
```
