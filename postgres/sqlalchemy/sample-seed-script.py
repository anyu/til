#!/usr/bin/env python3
"""
Sample script to seed tables using sqlalchemy.

Deps: Python3, sqlalchemy, psycopg2, click installed.
./bin/sample-seed-script.py -c config.yml
"""
from datetime import datetime
from random import randint
import click
import yaml
from sqlalchemy import MetaData, Table, create_engine

@click.command()
@click.option("-c", "--config", "config_path", required=True, help="Path to config.yml")

def main(config_path: str):
    config = load_from_yaml(config_path)
    seed_tables(config["postgres"])

def seed_tables(db_cfg):
    engine = create_engine(
        f'postgresql://{db_cfg["username"]}:{db_cfg["password"]}'
        f'@{db_cfg["host"]}:{db_cfg["port"]}/{db_cfg["database"]}'
    )
    meta = MetaData()

    # Use reflection to get table schemas
    meta.reflect(engine, only=["books, shelves"])
    book_table = Table("books", meta, autoload=True, autoload_with=engine)
    shelf_table = Table("shelves", meta, autoload=True, autoload_with=engine)

    # Generate random integers for test data
    random_num = randint(0, 1000000)

    book_record = {
        "name": f"some-book-{random_num}",
        "created_at": datetime.utcnow(),
    }
    # insert book record
    result = engine.execute(book_table.insert(), book_record)

    # if need to grab just inserted auto-generated primary ID
    new_book_id = result.inserted_primary_key[0]

    shelf_record = {
        "name": f"some-shelf-{random_num}",
        "book_id": new_book_id,
    }

    # insert record
    engine.execute(shelf_table.insert(), shelf_record)


def load_from_yaml(config_path: str) -> dict:
    with open(config_path) as config_raw:
        return yaml.safe_load(config_raw)

if __name__ == "__main__":
    main()
