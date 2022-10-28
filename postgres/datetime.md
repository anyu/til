# Datetime


Postgres has the following two data types for timestamps:

- `timestamp without time zone` (aka. `timestamp`)
- `timestamp with time zone` (aka. `timestamptz`)

Both data types are stored using only 64-bit integers. Neither *technically* store any time zone information; the latter is misleadingly named.

### Timestamp without time zone

This type is an absolute value time offset. It does not store time zone information.
It is essentially always assumed to be in UTC.

### Timestamp with time zone

This type is also an absolute value time offset with no time zone metadata set, but it displays timestamps and performs operations in the *session* time zone.

An input that has timezone information or an offset is converted to UTC using the offset for that time zone.

An input that does not have timezone information is assumed to be in the current PostgreSQL session’s time zone and is converted to UTC using the offset for that time zone.

For example, if the input is: `2018-08-28T12:30:00+05:30`, the value stored by Postgres will be: `2018-08-28T7:00:00:00`.

## psql time-related commands

Get session timezone

```sh
show timezone;
```

or

```sh
SELECT current_setting('TIMEZONE');
```