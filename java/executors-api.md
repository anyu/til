## Executors API

The Executors API/framework provides a higher level abstraction for working with threads.

- The preferred way of running tasks
- Decouples task submission for execution from thread creation/management
- Executors can run async tasks and manage a thread pool
- Each thread in pool executes multiple tasks one-by-one
- Allocates heavy-weight threads upfront
- Have to be explicitly stopped or they'll keep listening for new tasks.

## Thread creation via the Executors API

- Create task definition class
- Provide a task to an Executor Service
- Start Executor Service once, then use indefinitely (until app is stopped)

## Executor

The [Executor](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Executor.html) is an interface that executes submitted Runnable tasks.
Its purpose is to decouple task submission from thread creation and how the task is run.

```java
void execute(Runnable task);
```

## ExecutorService

The [ExecutorService](https://docs.oracle.com/javase/7/docs/api/java/util/concurrent/ExecutorService.html) extends the Executor interface and provides a lifecycle to the Executors, which has three phases:

1. *initialization* phase - creates required # of threads and starts them if needed (usually hidden)
2. *service* phase - runs submitted tasks
   - `submit()`
3. *destruction* phase - shuts down tasks
   - `shutdown()`: waits for actively running tasks to finish first
   - `shutdownNow()`: interrupts all running tasks

## Executors

The [Executors](https://docs.oracle.com/javase/7/docs/api/java/util/concurrent/Executors.html) class is a factory class with methods that constructs and returns various instances of an ExecutorService, with commonly useful configurations.

- `newFixedThreadPool(int nThreads)`:  at most nThreads can execute concurrently at any time
- `newCachedThreadPool()`: reuses previous threads if they're available, otherwise creates new threads
- `newSingleThreadExecutor()`: used when a background thread is needed to execute tasks one by one, but that no more than 1 task is running at any given time (only uses 1 thread)
   - essentially the same as `newFixedThreadPool(1)` above, except can't be reconfigured to use additional threads

All ExecutorService instances returned by Executors are objects of the ThreadPoolExecutor class.

Example using `newSingleThreadExecutor`:
```java
ExecutorService executor = Executors.newSingleThreadExecutor();
executor.submit(() -> {
    String threadName = Thread.currentThread().getName();
    System.out.println("Hello " + threadName);
});

// OUTPUT:
// Hello pool-1-thread-1
```

## ScheduledExecutorService

The [ScheduledExecutorService](https://docs.oracle.com/javase/7/docs/api/java/util/concurrent/ScheduledExecutorService.html) interface is used to run a task after a delay or periodically.

- `newScheduledThreadPool(int corePoolSize)`: Creates a thread pool with that can schedule commands
  - corePoolSize = the number of threads to keep in the pool, even if they are idle
- `newSingleThreadScheduledExecutor()`: Similar to `newSingleThreadExecutor` (only uses 1 thread), but runs the tasks on a schedule
  - essentially the same as `newScheduledThreadPool(1)` above, but just can't be reconfigured to use additional threads

### Scheduling tasks

- `scheduleAtFixedRate()`: Schedules tasks with a fixed time rate(eg. once every second), and accepts an initial delay
    - Note: Does not take the task duration into account (so if period = 1s, but task duration = 2s, the thread will quickly max out)
- `scheduleWithFixedDelay()`: Schedules tasks with a fixed delay between the end of one execution and the start of the next.
    - useful if you can't predict the duration of scheduled tasks

NOTE: If any *execution* instance of the task encounters an exception, subsequent executions are suppressed.

## Future

The [Future](https://docs.oracle.com/javase/9/docs/api/java/util/concurrent/Future.html) interface represents the result of an async operation.

- A result will eventually appear in the Future after processing is complete
- When you submit a Callable for execution, the ExecutorService returns an instance of a Future object.
- `get()` returns the value returned by the Callable task
- Calls to `future.get() ` blocks the current thread and waits until the underlying callable completes or terminates
- Every non-terminated future will throw exceptions if you shut down the executor
