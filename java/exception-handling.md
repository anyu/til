# Java Exception Handling

An exception is a problem that arises during a program's execution.

## Three categories of exceptions

- **Checked exception**: an exception that is usually *user error* or an error that *can't be foreseen* by the programmer.
  - These are checked at compile time (eg. DB errors, network connection errors, missing files)

- **Runtime exceptions**: these are exceptions that can probably have been avoided by the programmer.
  - These are considered *unchecked exceptions* as they are ignored at compile time.

- **Errors**: These are not exceptions, but problems beyond the control of the user or programmer.
  - These are considered *unchecked exceptions* as they are ignored at compile time.

---
                JAVA EXCEPTION HIERARCHY

                   ┌───────────────┐
                ┌─▶│   Throwable   │◀─┐
                │  └───────────────┘  │
                │                     │
        ┌───────┴───────┐      ┌──────┴────────┐
        │     Error     │      │   Exception   │
        └───────────────┘      └───────────────┘
                                 ▲           ▲
                                 │           └────────────────────┐
                                 │                                │
                       ┌───────────────────┐         ╔════════════════════════╗
                       │ RuntimeException  │         ║ non-RuntimeExceptions  ║
                       └───────────────────┘         ╚════════════════════════╝
                                 ▲                               ▲
                                 │                               │
                                 │                               │
                  ┌──────────────┴──────────────┐  ╔═════════════╩═══════════════╗
                  │                             │  ║                             ║
                  │    NullPointerException     │  ║         IOException         ║
                  │    NumberFormatException    │  ║        SQLException         ║
                  │  IndexOutOfBoundsException  │  ║    MalformedURLException    ║
                  │             ...             │  ║             ...             ║
                  │                             │  ║                             ║
                  └─────────────────────────────┘  ╚═════════════════════════════╝

                                         ──── unchecked
                                         ════ checked

## Throwing exceptions

All exceptions and errors are of a type with [Throwable](https://docs.oracle.com/en/java/javase/16/docs/api/java.base/java/lang/Throwable.html) class.

With an error occurs within a method, the method creates an exception object (containing info about the error) and hands it off to the runtime.

Creating an exception object and handing it to the runtime is called *throwing an exception*.

To throw an exception, use *throw*:
```java
public void method()
{
   //throwing an exception
   throw new SomeException("message");
}
```

## Handling exceptions

There are two choices when an exception object is created:

- Handle it within method (via try-catch)
- Throw the exception to the calling method to handle via `throw`

A method should clearly indicate which exceptions it will handle and which it will not, via the `throws` keyword in the method declaration.

> If an exception is not handled in the application, it propagates to the JVM and JVM usually terminates the program!

Handling an exception within method
```java
try {
    //code
}
catch(Exception e) {
    // handle exception
}
```

An exception cannot be both thrown by the method and also caught in the same method.

If an exception is thrown from **within** the catch block, the program stops the execution.

**try-catch-finally**: `finally` contains code that executes regardless whether an exception occurred or not

### Checked vs unchecked exceptions

**Checked exceptions** (aka. compile time exceptions) are those that a method *must* handle in its body or throw to its caller.
```java
FileReader file = new FileReader("somefile.txt");  // if file isn't found, this throws a FileNotFoundException
```
For program to compile, we need to handle it in a try-catch block.
```java
public static void main(String[] args) {
  try {
    FileReader file = new FileReader("somefile.txt");
  }
  catch (FileNotFoundException e) {
    e.printStackTrace();
  }
}
```

**Unchecked exceptions** (aka. runtime exceptions, but also errors(?)) are not checked by the compiler.

It is not mandatory to handle the exception or declare it in the method signature.

### Best practices

1. Checked exceptions should ideally never be used for programming errors, but absolutely for resource errors.
1. Throw only exceptions that a method can't handle. The method should first try to handle it inside the method.
1. If a client can reasonably be expected to recover from an exception, make it a checked exception.
   If a client cannot do anything to recover from the exception, make it an unchecked exception.

In reality, most applications will have to recover from pretty much all exceptions including NullPointerException, IllegalArgumentExceptions and many other unchecked exceptions.
(???)

Q. Can you throw a new error in a try block and catch it in the catch block? Or does `catch` only throw non-new errors from try

## Resources

https://howtodoinjava.com/java/exception-handling/
