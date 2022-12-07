# SQL Queries


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