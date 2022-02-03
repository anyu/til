# Multiple commands

There are 3 ways to group multiple Redis commands together: 1) pipelining, 2) transactions, 3) Lua scripts.

## Pipelining (aka. "batching")
Sends multiple commands to the server in the same message.

- can't access intermediate values (all responses arrive at the end)
- simplest of the three ways: just a grouping a bunch of commands
- mainly to optimize sending multiple commands more efficiently. Server buffers all the results in memory and sends all at once at the end.

## Transactions (`MULTI` commands)
Queues commands, can decide later whether to execute them all or not at all.

- can't access intermediate values (all responses arrive at the end)
- uses special commands to mark the start and end of the transaction

## Lua scripts

Redis can execute scripts in Lua. The script is loaded to the server and later invoked with parameters (via the `EVALSHA` command)
- _can_ access intermediate values
- Lua scripts are atomic; blocks (impacts performance if script is too slow)
- can access keys via `KEYS[1], KEYS[2]`, args via `ARGV[1], ARGV[2]`

### Gotchas
- Redis stores values as strings
- Need to use tonumber() function if doing integer comparisons
- Mind the return types from redis calls; nils are weird
- Redis.string/bool/etc wrappers around calls returns an error (`ErrNil`) if nil results
- Print statements won’t show
- Script needs to know key before script is evaluated (need to pass key in as arg vs getting dynamically in script)
- Script caching? Pass params in as args

### Running lua script locally


```
# myscript.lua

local key1 = KEYS[1]
local current_time = tonumber(ARGV[1])

local myval = redis.call('GET', key)
if (myval == true) then
  redis.call('SET', key1, current_time)
  return 1
else
  return 0
end
```

`redis-cli --eval ./myscript.lua my:key 11512323`
