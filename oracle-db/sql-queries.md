# SQL queries

Show all tables
```sql
SELECT owner, table_name FROM ALL_TABLES;
```

Show table columns
```sql
DESCRIBE <TABLE>;
```

Filter by field
```sql
SELECT * FROM <TABLE> WHERE some_string_field='some-field-value';
```

Show entries since X time
```sql
SELECT * FROM <TABLE> WHERE some_time_field > TO_TIMESTAMP('02-04-20 00:00:00', 'dd-mm-yyy hh24:mi:ss')
```

Show entries since X time with AM/PM specified
```sql
SELECT * FROM <TABLE> WHERE some_time_field  > TO_TIMESTAMP('04-10-21 03:00:00 PM', 'dd-mm-yyy hh:mi:ss PM')
```

Get count from table
```sql
SELECT DISTINCT COUNT(*) FROM <TABLE> WHERE date_created >= '01-JAN-20'
```

Filter by keyword + timestamp
```sql
SELECT * FROM <TABLE> WHERE
(
some_string_field LIKE '%keyword1%'OR
some_string_field LIKE '%keyword2%'
)
AND some_date_field > to_timestamp('01-JAN-20')
ORDER BY some_date_field
```

Get last 10 rows from table
```sql
SELECT * FROM <TABLE> WHERE ROWNUM > 10;
```
