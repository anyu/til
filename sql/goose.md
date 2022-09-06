# Goose

[goose](https://github.com/pressly/goose): Lightweight DB migration tool via SQL or Go.

## Setup

1. Install: `brew install goose`
2. Create migration:
   ```
   $ goose create add_initial_tables sql
   $ Created new file: 2022905082421_add_initial_tables.sql
   ```

## Writing migrations

Postgres example:

```sql
-- +goose Up
-- +goose StatementBegin
CREATE TABLE author (
    id UUID DEFAULT gen_random_uuid (),
    name TEXT NOT NULL,
    active BOOLEAN NOT NULL DEFAULT FALSE,
    PRIMARY KEY(id)
);

CREATE TABLE book (
    id UUID DEFAULT gen_random_uuid (),
    name TEXT NOT NULL,
    author_id UUID NOT NULL,
    published_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW() NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (author_id) REFERENCES author(id)
);

CREATE TABLE author_book (
    author_id UUID NOT NULL,
    book_id UUID NOT NULL,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW() NOT NULL,
    PRIMARY KEY(author_id, book_id),
    FOREIGN KEY (author_id) REFERENCES author(id)
    FOREIGN KEY (book_id) REFERENCES book(id)
);

-- +goose StatementEnd

-- +goose Down
-- +goose StatementBegin
DROP TABLE author_book;
DROP TABLE book;
DROP TABLE author;
-- +goose StatementEnd
```

## Running migrations

```
goose -dir $PATH_TO_MIGRATIONS postgres "postgresql://$USER:$PASSWORD@localhost:5432/$DB_NAME" up

# or

goose -dir $PATH_TO_MIGRATIONS postgres "host=localhost user=$USER password=$PASSWORD dbname=$DB_NAME" up
```

## Rollback

```
goose -dir $PATH_TO_MIGRATIONS postgres "postgresql://$USER:$PASSWORD@localhost:5432/$DB_NAME" down

# or

goose -dir $PATH_TO_MIGRATIONS postgres "host=localhost user=$USER password=$PASSWORD dbname=$DB_NAME" down
```

## Misc

Get status of migrations:
```
goose -dir $PATH_TO_MIGRATIONS postgres "postgresql://$USER:$PASSWORD@localhost:5432/$DB_NAME" status
```

goose adds the following tables to keep track of migrations

```
goose_db_version
goose_db_version_id_seq
```