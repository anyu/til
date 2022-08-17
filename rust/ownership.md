# Ownership

Essentially Rust's memory management rules.

It's Rust's way of **guaranteeing memory safety**, enforced at compile time.

## Strategies for Memory Management

In general, resource management (including memory management, but other examples include mutex locks, file handles, sockets, DB connections, etc) is about being able to reclaim resources tied to "unreachable objects".

Some languages have **garbage collectors**, which periodically scans memory to:
1. Find unused objects.
1. Release the resources associated with the objects.
1. Release the memory of those objects.

Non-garbage collection languages typically requires the programmer to perform those steps manually.

Rust does neither and uses an **ownership model** instead.

In Rust, memory is automatically freed once the variable that owns it goes out of scope (sometimes referred to as [RAII](https://en.wikipedia.org/wiki/Resource_acquisition_is_initialization) - Resource Acquisition Is Initialization)

## Stack and Heap

> The stack and the heap = parts of memory available to a program's code to use at runtime.

**The stack**: LIFO structure. Data stored here must have a known, fixed size.

**The heap**: When data is put on the heap, you request a certain amount of space. The memory allocator finds a big enough empty spot on the heap, returns a pointer (aka. allocating on the heap)

Pushing data to a stack is faster than allocating on the heap because the allocator is always just putting the data on top of the stack; doesn't have to search for a place.

Accessing data on a heap is slower as you have to follow a pointer to get there.

## Ownership Rules

- Each value in Rust has a variable that’s called its owner.
- There can only be one owner at a time.
- When the owner goes out of scope, the value will be dropped.

Assigning a value to a variable (aka. "binding") or passing function arguments by value (`foo(x)`) transfers ownership of the resources (aka. "moving").

## Types of Strings

#### String literal

- eg. `let s = "hello"`
- immutable
- can't be used for unkown string input, such as user input

Because we know the exact text at compile time and because it's immutable, we can store it on the stack.

#### String object

- eg. `let s = String::from("hello");`
- it's a pointer to the memory that holds the value of the string
- mutable
- can store text unknown at compile time

Because this type must support mutable, text unkown at compile time, we meed to allocate memory on the heap. This entails:

1. Requesting memory from the memory allocator at runtime.
1. Returning the memory back to the allocator when we’re done.

2 is where Rust is different.

GC languages automatically cleans up this memory. In other non-GC languages, you need to figure out when the memory's no longer used and return it.

Rust automatically returns heap memory once the variable that owns it goes out of scope. Behind the scenes, Rust calls a `drop` function automatically at a closing curly bracket.

```rust
let s1 = String::from("hello");
let s2 = s1;
```

When `s1` is assigned to `s2`, the String data on the stack is copied (the pointer, length, capacity), but not its value on the heap. Essentially only the pointer is copied.

Since both variables are pointing to the same heap memory, once the variables go out of scope, they'll both try to free the same memory (aka. double free error).

To avoid this, after `let s2 = s1`, Rust no longer considers s1 valid, so it doesn't free any memory when s1 goes out of scope.

### Moving

### Clone/Copy

### Functions, Return Values

### Resources
- https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html
- http://web.mit.edu/rust-lang_v1.25/arch/amd64_ubuntu1404/share/doc/rust/html/book/first-edition/ownership.html#ownership
