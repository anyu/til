# SQLalchemy Query Functions

- `Query.first()`: Returns only the first result or None
- `Query.one()`: Returns only one result. Raises exception if none found.
- `CursurResult.fetchone()`: Returns 1 row or None. Can be used to iterate through more results.
- `CursurResult.first()`: Returns 1 row or None.
  - `Result.scalar()`: Returns 1 singular scalar value (eg. the first column of the first row)

### Create record and return it
```python
my_obj = MyTableModel(
    some_id="some-id",
    name="some-name"
)

session.add(my_obj)
return my_obj

# If using a session context manager, may need to refresh session objects, eg:
# try:
#   yield async_session
#   await async_session.commit()
#   # Refresh session objects to access newly created objects
#   # within session
#   for obj in async_session:
#       await async_session.refresh(obj)
```

### Update record and return result as model object

```python
values_dict = {
    "updated_by": updated_by,
    "updated_at": datetime.now(timezone.utc),
}

if True:  # some fake condition
  values_dict.update({"name": name})

conditions = [MyTableModel.id == some_id]
  update_query = (
      update(MyTableModel)
      .where(and_(*conditions))
      .values(values_dict)
      .returning(MyTableModel)
  )
  query = select(MyTableModel).from_statement(update_query)
  await session.execute(query)
```

### Delete record

```python
conditions = [MyTableModel.id == some_id]
query = delete(MyTableModel).where(and_(*conditions))
await session.execute(query)
```

### Joins

```python
from sqlalchemy import outerjoin

conditions = [
    MyTableModel_1.note_id == "some-note-id"
    MyTableModel_2.tag_id == "some-tag-id"
]

join_stmt = outerjoin(
    MyTableModel_1,
    MyTableModel_2,
    MyTableModel_1.note_id == MyTableModel_2.note_id
)

query = (
    select(MyTableModel_1)
    .select_from(join_stmt)
)
await session.execute(query)
```

### Select from subquery

```python

subquery = (
    select(MyTableModel.some_id)
    .where([MyTableModel.id == some_id])
)

subquery_conditions = [
    MyTableModel.some_id.in_(subquery.subquery().select())
]
query = select(MyTableModel).where(
    and_(*conditions),
    and_(True, *subquery_conditions),
)
await session.execute(query)
```

### Intersect
Return only data common in both statements

```python
from sqlalchemy import intersect

intersect_result = intersect(query1, query2)

# Result type from an `intersect` isn't a table model type

subquery_conditions = [
    MyTableModel.some_id.in_(intersect_result.subquery().select())
]
query = (
    select(MyTableModel)
    .where(and_(True, *subquery_conditions))
)
return await session.execute(query)
```

### Getting Row result with table/column names

```python
for row in results.mappings():
  if row.get("MyTableModel"):
  ...
```

### Complex query with everything

```python
from sqlalchemy.sql.expression import nulls_last

base_conditions = [
    MyTableModel.note_id = "some-note-id"
    MyTableModel.name == "some-name"
]

query = (
  select(MyTableModel)
  .select_from(join_stmt)
  .where(
      and_(*conditions),
      and_(True, *subquery_conditions),
      and_(True, *cursor_conditions),
      or_(
          and_(*base_conditions),
          or_(or_(*null_conditions)),
      ),
  )
  .order_by(
      nulls_last(asc(MyTableModel.date)),
      sort_direction(MyTableModel.name),
  )
  .limit(25)
  ```