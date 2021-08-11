# Java Concurrency Concepts

A Java application run in its own process.

Multiple threads are used for parallel processing.

## Processes vs Threads

**Process**: A process runs independently and is isolated from other processes.
  - The OS allocates resources (memory, CPU time) to the process

**Thread**: A "lightweight process" that has its own call stack but can access shared data.
  - Every thread has its own memory cache
  - If a thread reads shared data, it stores it in its own cache
  - A thread can re-read the shared data

## Threads
- Threads can be put to sleep (handy for simulating long running tasks).
- Threads can be directly used and may be sufficient for basic tasks, but have disadvantages:
  - Creating a new thread has some performance overhead
  - Too many threads can reduce performance (CPU needs to switch between threads)
  - It's difficult to control the # of threads, so it's easy to run out of memory due to too many threads
  - Higher-level building blocks are often needed.

## Executors

### Thread Pools

A **thread pool** manages a pool of worker threads, and contains a work queue which holds tasks pending execution.

**Fixed thread pool**
- Always has a specified # of threads running.
- If a thread is somehow terminated while in use, it's automatically replaced with a new thread.
- Tasks are submitted to the pool via an internal queue, which holds extra tasks whenever there are more active tasks than threads.

An important advantage of a fixed thread pool is that it allows graceful degradation.

>*Example*: A server that handles each HTTP request via a separate thread. If the server creates a new thread for every request, if it receives more requests than it can handle immediately, it'll stop responding to all requests.
>
> By capping the # of threads that can be created, while the server won't respond to requests as quickly as they come in, it'll sere them as quickly as it can sustain.

### Callables

Callables are functional interfaces like Runnables, but return a value.

Since `submit()` doesn't wait for the task to complete, the executor can't return the Callable result directly, so it returns a Future (used to retrieve the result at a later time)

```java
ExecutorService executor = Executors.newFixedThreadPool(1);
Future<Integer> future = executor.submit(task);

System.out.println("Is future done? " + future.isDone());

Integer result = future.get();

System.out.println("Is future done? " + future.isDone());
System.out.print("result: " + result);
```


## ScheduledExecutorService

`ScheduledExecutorService` is used to run a task after a delay or periodically.

### Creating ScheduledExecutorService objects

- `newScheduledThreadPool(int corePoolSize)` // Creates a thread pool that can schedule commands
- `newSingleThreadScheduledExecutor()`       // Creates a single-threaded executor that schedules commands

The TLDR difference between the two is that `newScheduledThreadPool` lets you add more threads.

### Scheduling tasks

- `scheduleAtFixedRate()`: Schedules tasks with a fixed time rate(eg. once every second), and accepts an initial delay

  - Note: Does not take the task duration into account (so if period = 1s, but task duration = 2s, the thread will quickly max out)

- `scheduleWithFixedDelay()`: Schedules tasks with a fixed delay between the end of one execution and the start of the next.

  - useful if you can't predict the duration of scheduled tasks


## Resources
- Notes/examples mostly from: https://winterbe.com/posts/2015/04/07/java8-concurrency-tutorial-thread-executor-examples/
- [Executor interfaces](https://docs.oracle.com/javase/tutorial/essential/concurrency/exinter.html)
