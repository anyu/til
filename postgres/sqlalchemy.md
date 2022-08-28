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
from sqlalchemy import Column, Integer, String, VARCHAR
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()

class Book(Base):
    __tablename__ = 'book'
    id = Column(UUID(as_uuid=True), primary_key=True)
    title = Column(VARCHAR(255), nullable=False)
    author = Column(String)
    pages = Column(Integer)
    # timestamps get involved; this is a basic example
    published=datetime(2016, 11, 18)
```

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
