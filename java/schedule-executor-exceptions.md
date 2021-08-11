# Handling ScheduleExecutorService exceptions

When using the ScheduledExecutorService to schedule Runnable tasks, and the Runnable throws an Exception.

[source](https://www.dontpanicblog.co.uk/2021/05/15/exception-handling-in-scheduledexecutorservice/)


```java
// Task is scheduled successfully and started, but the exception is not handled.

class Main {
  public static void main(String args[]) {
    ScheduledExecutorService executor = Executors.newSingleThreadScheduledExecutor();
    Runnable task = () -> System.out.println("42 /  0 = " + 42/0);
    try {
        executor.schedule(task, 0, TimeUnit.MILLISECONDS);
    } catch (Exception e)  {
        e.printStackTrace();
    }
    System.out.println("Done!");
	}
}
```

This is because the result of a scheduled task is available as a ScheduledFuture, which doesn't immediately contain the result since the task is scheduled to run later.

We can wait for the result with `ScheduledFuture.get()`, which either
- returns the value of a Callable
- rethrows the Callable / Runnable exception of it failed

```java
class Main {
  public static void main(String args[]) {
    ScheduledExecutorService executor = Executors.newSingleThreadScheduledExecutor();
    Runnable task = () -> System.out.println("42 /  0 = " + 42/0);
    ScheduledFuture<?> result = executor.schedule(task, 10, TimeUnit.SECONDS);
    try {
        result.get();
    } catch (Exception e) {
        e.printStackTrace();
    }
	}
}
```
TODO: But there are problems with this.


Repl: https://replit.com/@anyu/ScheduledExecutorExceptions


- Also, when [scheduleWithFixedDelay](https://docs.oracle.com/javase/7/docs/api/java/util/concurrent/ScheduledExecutorService.html#scheduleWithFixedDelay(java.lang.Runnable,%20long,%20long,%20java.util.concurrent.TimeUnit)) fails, `if any execution of the task encounters an exception, subsequent executions are suppressed`.
