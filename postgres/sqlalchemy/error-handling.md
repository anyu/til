# Error handling

There may be a more elegant way to do this, but solutions out there didn't work for me.
Being able to differentiate more specific/underlying error types from asyncpg:


```python
from sqlalchemy import exc
from asyncpg.exceptions import UniqueViolationError
  
try:
  result = await self.some_query_db_method()
except exc.IntegrityError as e:
  if e.orig.__cause__.__class__ == UniqueViolationError:
    raise SomeCustomError("Duplicate record exists" )
  raise SomeGeneralError("Some other integrity error that's not unique violation")
except exc.SQLAlchemyError as e:
  raise SomeGeneralError(f"Some general error: {e}")
...
```