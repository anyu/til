# Alembic

```sh
pip install alembic

# Init alembic in project root
alembic init alembic
```

Output:
```sh
project
│   alembic.ini
│   config.py
│   crud.py
│   models.py
│
└───alembic
    │   env.py
    │   README
    │   script.py.mako
    │
    └───versions
```

## Core commands

```
# Generate a migration
# May need to manually modify after
alembic revision --autogenerate -m "Added price column"

# Run the upgrade cmd
alembic upgrade head

# See ran migrations
# alembic history

# Rollback last migration
alembic downgrade -1

# Rollback specific migration
alembic downgrade HASH

# Rollback all migrations
alembic downgrade base
```k

## More commands

```
# Make alembic think NO migrations have been run (but won't undo migrations)
# maybe useful for specific cases...
alembic stamp base
```