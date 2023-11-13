# Untangling dealing with bytes

## make([]byte,...) vs bytes.Buffer

### `make([]byte, ...)`

- Creates a byte slice with a specified length and capacity.
- Good for when you have a good estimate of the required buffer size or working with a fixed-size byte slice.
- `bytes` providers readers/writers where the entire input/output is in memory

### `bytes.Buffer`

- Provides a dynamic buffer for building/manipulating byte slices.
- Allows read/write, but doesn't flush data itself
- Good for when you need to concatenate or manipulate byte data, but don't know the final size in advance.
- Also implements a lot of methods, so you can pass a []byte to other libs expecting a Reader, or to construct a []byte with a library expecting a Writer.
- It's a buffer with 2 ends; you can only read from its start or write to its end. No 'seeking'.

### `bufio` package
`bufio` provides data buffering and reads/write it upstream when the buffer is empty/filled.

*"In general I use `bytes.Buffer` for writing to byte slices, and `bytes.Reader` for reading from byte slices."*


## bytes.Reader vs bufio.Reader

Normally, when apps run I/O ops to files, network, or a DB, they trigger system calls under the hood. Buffer IO is a technique to temporarily accumulate results for IO operations before transmitting them forward, thus reducing the # of sys calls.

`bytes.NewReader` creates a Reader from a byte slice (aka. a chunk of memory you already have in your program). Useful for passing a byte slice to another API that expects a Reader.

`bufio.NewReader` is for wrapping existing Readers (whose Read method is relatively expensive, eg. a TCP connection or file) to coalesce a lot of easy to program small Read calls into a few larger ones.

This function takes a byte slice where the data will be read into as an argument.

```go
package main

import (
  "bufio"
  "fmt"
  "os"
)

func main() {
  file, err := os.Open("file.txt")
  if err != nil {
    fmt.Println(err)
    return
  }

  reader := bufio.NewReader(file)
  data := make([]byte, 100)
  _, err = reader.Read(data) // read 100 bytes from the file into a byte slice.
  if err != nil {
    fmt.Println(err)
    return
  }

  fmt.Println(string(data))
}
```

`io.Reader` is the interface. If working with various data sources or need a more general solution.

## bytes.Reader vs *bytes.Reader

In most cases, you can use `bytes.Reader` for reading data from a byte slice without needing to modify the reader's state. 

If you need to modify the reader's state, then you might use `*bytes.Reader`. 

---

## Returning `bytes.Buffer` vs `[]byte`

Generally more prevalent to return `[]byte` since `bytes.Buffer` provides an implementation on top of it, which may not be necessary to the caller.

1. Does this method always hold the entire data in memory at once? `[]byte` is good.

2. If this method works with an indeterminate length of data, or perhaps you want the user to decide where the data is stored, accept `io.Writer` as a parameter and let the caller decide where to place that data (This is almost always the right approach unless you are already dealing with `[]byte` as a result of using the standard library).

3. In any other situation return `bytes.Buffer` (as you can see, this is quite rare).

Buffers are generally implementation details, a tool you use to do something. It's pretty rare that it should be a return parameter.