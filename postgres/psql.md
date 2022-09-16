# Postgres Commands

## Setup
```sh
brew install postgres
brew services start postgresql
# enter pysql interactive
psql postgres
```

## Roles

The `postgres` role may not have been created, verify via:

```sh
$psql postgres

postgres-# \du
                                   List of roles
 Role name |                         Attributes                         | Member of
-----------+------------------------------------------------------------+-----------
 postgres  | Superuser, Create role, Create DB                          | {}
```

If it's not there, use the `createuser` utility that comes with Postgres:

```sh
createuser postgres -s
```

Log in w/ a particular role
```sh
psql -U postgres
```

If already in postgres, switch role
```
set role $ROLE
```

### Create DB

```sql
CREATE database $DB_NAME;
```

### List DBs
```
\list
```

### Connect to DB
```
\c $DB_NAME
```

### Create table

```sql
CREATE TABLE IF NOT EXISTS $TABLE_NAME (
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
\d $TABLE_NAME;
```

### Drop table

```sql
DROP TABLE IF EXISTS $TABLE_NAME;
```

### View indexes

`\d $TABLE_NAME` should show indexes, but if not:

```sql
SELECT * FROM pg_indexes WHERE tablename NOT LIKE 'pg%';
```

## Troubleshooting

### Common errors

- Column doesn't exist when inserting into table
  - make sure values aren't double quoted (Postgres interprets them as delimited identifiers, eg. column in a table), but single quoted


## Resources

- [DB fiddle - postgres](https://dbfiddle.uk/?rdbms=postgres_14)
  - generate UUID type value
    ```sql
    select gen_random_uuid()
    ```
