# SQL Queries

### Select rows with ID in list

```
SELECT * FROM $table_name
WHERE id in ('e8fa8f92', '4fe2a6a6');
```

### Delete rows with ID in list

```
DELETE FROM $table_name
WHERE id in ('e8fa8f92', '4fe2a6a6');
```

### Upserting a value when there's a conflict due to a constraint
```sql
INSERT INTO $table_name (column1, column2, column3)
VALUES ('some-valu1',  'some-value2', 'some-value3') 
ON CONFLICT ON CONSTRAINT $constraint_name DO UPDATE SET column3 = '$new_value';
```

or do nothing
```sql
INSERT INTO $table_name (column1, column2, column3)
VALUES ('some-valu1',  'some-value2', 'some-value3') 
ON CONFLICT ON CONSTRAINT DO NOTHING
```

### Get duplicate entries

- the columns selected by must also be in the group by

```sql
SELECT column1 from $table_name group by column1, column2
HAVING COUNT(*) > 1;
```

### Cascade deleting records in other tables

Use `ON DELETE CASCADE`

```sql
CREATE TABLE IF NOT EXISTS authors (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    name TEXT NOT NULL,
    active BOOLEAN NOT NULL DEFAULT FALSE,
);

CREATE TABLE IF NOT EXISTS books (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    name TEXT NOT NULL,
    author_id UUID NOT NULL,
    published_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW() NOT NULL,
    FOREIGN KEY (author_id) REFERENCES authors(id) ON DELETE CASCADE
);

```

### Auto-updating fields

Postgres does not have a built-in `ON UPDATE`, unlike MySQL, so this is generallly achieved via triggers ([nice article](https://aviyadav231.medium.com/automatically-updating-a-timestamp-column-in-postgresql-using-triggers-98766e3b47a0))

This will auto-update the `updated_at` field of `my_table` right before an `update` happens, even if the record values end up the same.

```sql
CREATE FUNCTION trigger_update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER update_timestamp
BEFORE UPDATE ON my_table
FOR EACH ROW
EXECUTE PROCEDURE trigger_update_timestamp();

```

If want to auto-update the field only if the record actually changed:

```sql
CREATE FUNCTION trigger_update_timestamp()
RETURNS TRIGGER AS $$
BEGIN
  IF (NEW != OLD) THEN -- only modify if record actually changed, not just that an update attempt happened
    NEW.updated_at = NOW();
    RETURN NEW;
  END IF;
  RETURN OLD;
END;
$$ LANGUAGE plpgsql;
```

NOTE: If using something like sqlalchemy in application code, see sqlalchemy note on using `server_onupdate` to delegate to the DB.


## Misc

Handy query to test against values instead of a table
```sql
SELECT
  DISTINCT(REGEXP_EXTRACT(emails,'@(.+)',1)) as domains
FROM 
(
  VALUES
  ('test@gmail.com'),
  ('test2@hotmail.com')
)
as emails(emails);
```
