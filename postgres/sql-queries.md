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