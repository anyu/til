# Tornado

[Tornado](https://github.com/tornadoweb/tornado) is an open source Python web framework and async networking library.

Unlike a  traditional synchronous web server that just has 1 thread devoted to each user (expensive), Tornado is a **non-blocking I/O** web server. It uses a **single-threaded** event loop. All app code should be async and not be blocking because only 1 operation can be happening at a time. Tornado allows for thousands of async open connections.

## Good use cases
- RESTful APIs
- App with large scale/high performance that needs lot of open connections / thousands of concurrent users
- Web sockets
- App with slow DB queries

## Bad use cases
- App is CPU heavy(?)
- If there’s not an async DB driver available (eg. mysql)

## Concepts

- **Blocking**: When a function waits for something to happen before returning. A function can block in some respects and not others. We’re mostly talking about network I/O blocking with Tornado.
- **Async**: An async function returns before it’s finished. Async operations in Tornado generally return placeholder objects (Futures), with some low-level components (eg. IOLoop) that uses callbacks. Futures are usually transformed into their result with the await or yield keywords.

## Examples

A sync function
```python
from tornado.httpclient import HTTPClient

def synchronous_fetch(url):
    http_client = HTTPClient()
    response = http_client.fetch(url)
    return response.body
```

An async function
```python
from tornado.httpclient import AsyncHTTPClient

async def async_fetch(url):
    http_client = AsyncHTTPClient()
    response = await http_client.fetch(url)
    return response.body
```

## Setup

```sh
pip install tornado
```

Basic setup (no async)

```python
import asyncio
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
```

## Recommended async approach

Native coroutines (Python 3.5’s async/await keywords to suspend and resume execution) are the recommended form for async-ness when possible.
