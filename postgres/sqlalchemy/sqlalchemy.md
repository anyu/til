# SQLalchemy

Most popular Python ORM for SQL DBs.

## Getting started

```
pip install sqlalchemy

# Install Postgres driver to let SQLA get a connection to Postgres
pip install psycopg2

# If want to use included migration tool
pip install alembic
```

NOTE:

Unfortunately Postgres has to still be additionally installed:

```
brew install postgresql
```

SQLAlchemy has a dependency on `psycopg2`, which in turn, expects a `pg_config` file.

- On macOS, installing `psycopg2-binary` would typically be the way to forgo the `pg_config` dep. there is a [known issue](https://github.com/psycopg/psycopg2/issues/1286) with this for Apple M1 chips. A workaround exists using a 3rd party user's [test binary](https://github.com/psycopg/psycopg2/issues/1286#issuecomment-1186353903), but that seems riskier than just going with the brew formula.
- On Linux envs, this can be solved via installing deps such as `libpq`, `python3-dev` (exact package depends on linux distro)

If hit this error on running SQLalchemy app:
```
Library not loaded: '/opt/homebrew/opt/postgresql/lib/libpq.5.dylib'
```

May need to find/symlink where the libpq file is:

```
sudo ln -s /opt/homebrew/opt/postgresql@14/lib/postgresql@14/libpq.5.dylib /usr/local/lib/libpq.5.dylib
```

## Organization

```
app/
  config.py
  db.py
  models/
    book.py
```

## Basic models

```py
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Text, text, VARCHAR
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    id = Column(UUID(as_uuid=True), server_default=text("gen_random_uuid()"), primary_key=True)
    created_at = Column(DateTime(timezone=True), server_default=utcnow(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True), server_default=utcnow(), server_onupdate=utcnow(), nullable=False
    )
    author = Column(Text)

class Book(Base):
    __tablename__ = 'books'
    id = Column(UUID(as_uuid=True), server_default=text("gen_random_uuid()"), primary_key=True)
    title = Column(VARCHAR(255), nullable=False)
    # `ondelete="CACASDE": book record is also deleted if author record deleted
    author_id = Column(UUID(as_uuid=True), ForeignKey("authors.id", ondelete="CASCADE"), nullable=False)
    active = Column(Boolean, server_default=text("false"), nullable=False)

    # Relationships
    book = relationship("Book")
    # Indexes
    books_author_id_fkey = Index("books_authory_id_fkey", author_id)
    # Constraints
    unique_constraint = UniqueConstraint(author_id, title)

# Intersection/join model - there's a simpler way if you don't need to add extra fields
class BookAuthor(Base):
    __tablename__ = "books_authors"

    some_extra_field = Column(Text)
    book_id = Column(
        UUID(as_uuid=True), ForeignKey("books.id"), primary_key=True, nullable=False
    )
    author_id = Column(
        UUID(as_uuid=True), ForeignKey("authors.id"), primary_key=True, nullable=False
    )

    book = relationship("Book")
    author = relationship("Author")
```

`utcnow()` func needs to be added manually - see https://docs.sqlalchemy.org/en/14/core/compiler.html#utc-timestamp-function

```py
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql import expression
from sqlalchemy.types import DateTime

class utcnow(expression.FunctionElement):
    type = DateTime()

@compiles(utcnow, "postgresql")
def pg_utcnow(element, compiler, **kw):
    return "TIMEZONE('utc', CURRENT_TIMESTAMP)"
```

## Gotchas
- sqlalchemy does not pick up `default` attributes, so need to use `server_default`

## Connecting

```py
### config.py ###

# Scheme: "postgres+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"

DATABASE_URI='postgres+psycopg2://postgres:password@localhost:5432/mydatabase'
```

```py
### db.py ###
from sqlalchemy import create_engine

engine = create_engine(DATABASE_URI)

# Creates models/tables
Base.metadata.create_all(engine)

# Drop models/tables
Base.metadata.drop_all(engine)

def recreate_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
```

## Using Sessions

Sessions allow transactions – rows can be added and committed when ready. Rollbacks roll back the whole transaction.

Sessions also hold queried data as Python objects. Changes can be made to objects in the session and committed back to the DB if needed.

```py
### db.py ###

from sqlalchemy.orm import sessionmaker

# Create global Session object
Session = sessionmaker(bind=engine)
```

When interacting w/ the DB, create new sessions from the global session.

```py
s = Session()

s.add(book)
s.commit()

# Test queries
s.query(Book).first()
s.query(Book).all()

# filter_by works for simple filtering
s.query(Book).filter_by(title='Some book').first()

# filter is needed for more advanced filtering
# ilike = ignore case
s.query(Book).filter(Book.title.ilike('Some book')).first()

# Between
s.query(Book).filter(Book.published.between(start_date, end_date)).all()

# And/Or
s.query(Book).filter(
    and_(
       Book.pages > 750,
       Book.published > datetime(2016, 1, 1)
    )
).all()

# Order by
s.query(Book).order_by(Book.pages.desc()).all()

# Limit
s.query(Book).limit(5).all()

# Filters can be chained
s.query(Book)\
    .filter(...)\
    .filter(...)\
    .order_by(...)\
    .limit()\
    .all()

# Make sure to close the session when done to free connections.
# Open sessions will prevent db recreates.
s.close()
# or close all open session
# s.close_all()
```
