# Postgres Commands

## Setup
```
brew install postgres
brew services start postgresql
psql postgres
```

### Create DB

```
CREATE database DB_NAME;
```

### Connect to DB
```
\c DB_NAME
```

### Create table

```
CREATE TABLE TABLE_NAME (
  id SERIAL NOT NULL PRIMARY KEY,
  name TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
);
```

### Describe table

```
\d TABLE_NAME
```

### Drop table

```
DROP TABLE TABLE_NAME
```
