# Datetime

## SQLAlchemy datetime types

`DateTime`
- same as Postgres' `timestamp without time zone`
- with this option, if we want to always ensure timestamps have tz=UTC, can use such a decorator:
https://docs.sqlalchemy.org/en/14/core/custom_types.html#store-timezone-aware-timestamps-as-timezone-naive-utc


`DateTime(timezone=True)`
- same as Postgres' `timestamp with time zone`

