# Character Encoding

https://tapoueh.org/tags/data-types/

There are 4 different encoding settings:
- The server side encoding for the database
- The client encoding that the PostgreSQL client announces to the PostgreSQL server. The PostgreSQL server assumes that text coming from the client is in `client_encoding` and converts it to the server encoding.
- The OS default encoding. This is the default `client_encoding` set by psqlif you don't provide a different one. Other client drivers might have different defaults; eg PgJDBC always uses utf-8.
- The encoding of any files or text being sent via the client driver. This is usually the OS default encoding, but it might be a different one - for example, your OS might be set to use utf-8by default, but you might be trying to COPY some CSV content that was saved as latin-1.
You almost always want the server encoding set to utf-8. It's the rest that you need to change depending on what's appropriate for your situation. You would have to give more detail (exact error messages, file contents, etc) to be able to get help with the details.

```sql
$ show client_encoding;
$ show server_encoding;

# see full table
$ \l
client_encoding = utf8
```
