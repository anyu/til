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


## Commands

```
# Generate a migration
alembic revision --autogenerate -m "Added price column"

# Run the upgrade cmd
alembic upgrade head

```