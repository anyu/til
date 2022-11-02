# SQLalchemy Query Functions


- `Query.first()`: Returns only the first result or None
- `Query.one()`: Returns only one result. Raises exception if none found.
- `CursurResult.fetchone()`: Returns 1 row or None. Can be used to iterate through more results.
- `CursurResult.first()`: Returns 1 row or None.
  - `Result.scalar()`: Returns 1 singular scalar value (eg. the first column of the first row)