# Redis Data Types

- Strings
  - [SET](https://redis.io/commands/set) - `O(1)`, [GET](https://redis.io/commands/get) - `O(1)`, [INCR](https://redis.io/commands/incr) - `O(1)`
- Lists: a collection of strings sorted according to insertion order
  - [LPUSH](https://redis.io/commands/lpush) - `O(1)`, [RPUSH](https://redis.io/commands/rpush) - `O(1)`, [LRANGE](https://redis.io/commands/lrange) - `O(S+N)`
- Sets: a collection of unique, unsorted strings
  - [SADD](https://redis.io/commands/sadd) - `O(1)`, [SMEMBERS](https://redis.io/commands/smembers) - `O(N)`
- Hashes: maps of field value string pairs
  - [HSET](https://redis.io/commands/hset) - `O(1)`, [HGET](https://redis.io/commands/hget) - `O(1)`, [HGETALL](https://redis.io/commands/hgetall) - `O(N)`
- Sorted Sets: like a set, but every string element is associated/sorted with a number value
  - [ZADD](https://redis.io/commands/zadd) - `O(log(N))`, [ZRANGE](https://redis.io/commands/zrange) - `O(log(N)+M)`
- Bitmaps
  - [SETBIT](https://redis.io/commands/setbit) - `O(1)`, [GETBIT](https://redis.io/commands/getbit) - `O(1)`


### Hashes

    ```
          hash key ───────▶  ┌──somekey───────────────────────────┐  ┌──somekey----------─────────────────┐  ┌──somekey───────────────────────────┐
                             ├──────────────────────┬──────────── │  ├──────────────────────┬──────────── │  ├──────────────────────┬──────────── │
                             │                                    │  │                                    │  │                                    │
            fields  ──────▶  │ "field1"             │  someval    │  │ "field1"             │  someval    │  │ "field1"             │  someval    │
       (unordered)           │                                    │  │                                    │  │                                    │
                             │ "field2"             │  someval2   │  │ "field2"             │  someval2   │  │  "field2"            │  someval2  │
                             │                                    │  │                                    │  │                                    │
                             └──────────────────────┴─────────────┘  └──────────────────────┴─────────────┘  └──────────────────────┴─────────────┘
    TTL of hash key ──────▶   TTL = 86400s                ▲
                                                          │
                                                        values
    ```


### Resources

- https://redis.io/topics/data-types
- https://redis.io/topics/data-types-intro
