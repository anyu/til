# Async 

SQLalchemy async extension: https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html

### Key changes

1. Use async methods
1. Update connection string prefix to: `postgresql+asyncpg://`
1. Use async version of connection/engine functions
1. Replace some query functions

```py
import asyncio

from sqlalchemy.ext.asyncio import create_async_engine

async def async_main():
    engine = create_async_engine(
        "postgresql+asyncpg://scott:tiger@localhost/test",
        echo=True,
    )

    async with engine.begin() as conn:
        await conn.run_sync(meta.drop_all)
        await conn.run_sync(meta.create_all)

        await conn.execute(
            t1.insert(), [{"name": "some name 1"}, {"name": "some name 2"}]
        )

    async with engine.connect() as conn:
        # select a Result, which will be delivered with buffered results
        result = await conn.execute(select(t1).where(t1.c.name == "some name 1"))

        print(result.fetchall())

    # for AsyncEngine created in function scope, close and
    # clean-up pooled connections
    await engine.dispose()


asyncio.run(async_main())
```