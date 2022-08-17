# Postgres with Python

## Connection Options
- popular ORM: SQLAlchemy
- direct SQL w/ a PostgreSQL driver/adapter
  - most common/widely supported: [psycopg](https://github.com/psycopg/psycopg)
    - used by SQLAlchemy under the hood
    - uses `libpq` (supports the same connection env vars as libpq: `PGDATABASE`, `PGUSER`, `PGHOST`, etc)
      - libpq requires `libpq-dev`, `python-dev` packages
  - no native dependendices/easy to distribute: pg8000
  - newer kid on the block: asyncpg
    - better performance

## Migration management tools
- [Alembic](https://alembic.sqlalchemy.org/en/latest/), used with SQLAlchemy (but doesn't need to?)
- [sqitch](https://sqitch.org)
- [flyway](https://flywaydb.org/)
  - rollback migrations is a paid feature
- [liquibase](https://www.liquibase.org/)
  - using env vars is a paid feature

### psycopg2

```sh
pip install psycopg2
```

#### DB cursors

How does an application handle large SQL query results?
It can either allocate a ton of memory, or use cursors to throttle data.

Cursors can paginate results from a query, move forward/backward across rows.

Two types of cursors

1. **client-side cursor** (the default): Fetches all available rows for a query. Client has to allocate memory for all results.
  - The cursor's `execute` method saves the query result in the cursor
  - The `fetchone`, `fetchmany`, `fetchall` cursor methods are for fetchin specific results
  - `query`, `name` cursor fields can be helpful for debugging (an unnamed cursor defaults to clientside)

1. **server-side cursor**: Used to throttle data. Clients can request X number of rows on the first request and further queries for more.


#### Basic setup

```py
import psycopg2

# connect to DB
conn = psycopg2.connect(
  host = "somehost",
  user = "someuser",
  password = "postgres",
  database="mydb"
)

sql_query = 'SELECT *  FROM actor WHERE first_name LIKE %s'
with connect(**config) as conn:
    with conn.cursor() as cur:
    # create a server-side cursor by passing in a name
    # with conn.cursor("actor") as cur:
        # If using server-side cursor, can limit result
        # max rows fetched in a batch; default is 2000
        # cur.itersize = 200
        cur.execute(sql_query, ["John%"])
        rows = cur.fetchall() // returns tuples (id, name)

        for r in rows:
          print(f"{r[0], r[1]}")
        
        cur.close()

# close connection
conn.close()        
```
