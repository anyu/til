# Thread Creation

There are a number of ways to create threads, but they all involve the following:

- a [Thread](https://docs.oracle.com/javase/7/docs/api/java/lang/Thread.html) class object
- a [Runnable](https://docs.oracle.com/javase/7/docs/api/java/lang/Runnable.html) interface implementation (aka. the task)
- an invocation of the Thread object's **start()** method

## Thread creation via the Threads API

### Technique 1: Extend the Thread class
- Extend the Thread class + override its `run()` method
- Pros: Can access basic built-in thread methods that aren't available in Runnable
- Cons: can't extend other classes because Java doesn't support multiple inheritance

```java
// Thread creation via extending Thread class
class Main {
    public static void main(String[] args) {
        int n = 8; // Number of threads
        for (int i = 0; i < n; i++) {
            Example object = new Example();
            object.start();
        }
    }
}

class Example extends Thread {
    public void run() {
        try {
            System.out.println("Thread " + Thread.currentThread().getId() + " is running");
        }
        catch (Exception e) {
            System.out.println("Exception is caught");
        }
    }
}
```
### Technique 2: Implement the Runnable interface
- Create a new class that implements Runnable
- Pros:
   - Can extend other base classes if needed
   - Provides an object that can be shared by multiple threads

```java
// Thread creation via implementing the Runnable Interface
class Main {
    public static void main(String[] args) {
      int n = 8; // Number of threads
      for (int i = 0; i < n; i++) {
        Thread object = new Thread(new Example());
        object.start();
      }
    }
}

class Example implements Runnable {
    public void run() {
        try {
            System.out.println("Thread " + Thread.currentThread().getId() + " is running");
        }
        catch (Exception e) {
          System.out.println("Exception is caught");
        }
    }
}
```

Alternative Runnable implementation using lambda functions
```java
Runnable task = () -> {
    String threadName = Thread.currentThread().getName();
    System.out.println("Hello " + threadName);
};
task.run();

Thread thread = new Thread(task);
thread.start()

System.out.println("Done!");

// OUTPUT:
// Hello main
// Hello Thread-0 // could come after 'Done!'
// Done!
  ```
Due to concurrent execution, the order is non-deterministic - the runnable could be invoked before or after the main thread prints `Done!'.

## Thread.start() vs Thread.run()

`start()`: creates a new thread is created and then executes run() on that new thread.
   - Defined in `java.lang.Thread`class
   - Can't be invoked more than once

`run()`: executes run() on the current/calling thread. Does not create a new thread, so no multi-threading is happening.
   - Defined in `java.lang.Runnable interface`; must be overridden by implementing class
   - Can be invoked multiple times

```java
// Invoking thread.start()
class Main {
  public static void main(String[] args) {
     Example t = new Example();
     t.start();
  }
}

class Example extends Thread {
   public void run() {
      System.out.println("Current thread name: " + Thread.currentThread().getName());
      System.out.println("run() method called");
   }
}

// OUTPUT:
// Current thread name: Thread-0
// run() method called
```

vs.

```java
// Invoking thread.run() directly
class Main {
    public static void main(String[] args) {
        Example t = new Example();
        t.run();
    }
}

class Example extends Thread {
    public void run() {
        System.out.println("Current thread name: " + Thread.currentThread().getName());
        System.out.println("run() method called");
    }
}

// OUTPUT:
// Current thread name: main
// run() method called
```
