# Concurrency in Go

- Many Goroutines execute within a single OS thread
- the Go runtime scheduler determines which Go routine is running and at what time. Scehdules goroutines inside an OS thread. Like a little OS within a single OS thread.
- Go is running within 1 OS thread

## Synchronization

Sycnhronization techniques are used to avoid undesired interleavings between goroutines
The idea is to have a global event that's viewable by different goroutines.

### WaitGroups

`sync.WaitGroup` forces a goroutine to wait for other goroutines.

## Channels

Channels are for transferring data between goroutines.

### Unbuffered channels

Unbuffered channels can't hold data in itself.

- Sending channel blocks until data is received by the receiver
- Receiving channel blocks until data is sent

### Buffered channels

Channels can contain a limited number of objects (capacity).
Buffer channels are useful in cases where you don't want the sender and receiver to operate at exactly the same speed/be in lock step (eg. in producer/consumer situations)

- Sending only blocks if the buffer is full (if buffer is not full, it can keep receiving)
- Receiving only blocks if the buffer is empty
