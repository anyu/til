# Parallelism vs Concurrency

- **Parallel**: Execution occurs at exactly the same time.
- **Concurrent**: Execution's start and end times overlap.

## Parallel tasks
- Must be executed on different hardware (separate CPU cores)

## Concurrent tasks
- May be executed on same hardware
- Mapping from tasks to hardware is _not_ directly controlled by the programmer, at least in Go
- Programmer determines which tasks _can_ be executed in parallel, not what _will_ be excuted in parallel
  - actual parallelism depends on how tasks are mapped to hardware - depends on OS, Go's runtime scheduler
- Even with just 1 core, concurrency can help by hiding latency (tasks may need to wait for other reasons - eg. memory access; so another task can execute in between)

## Moore's Law
Moore’s Law is the observation that the number of transistors in a dense integrated circuit doubles roughly every 2 years.

It’s stopped being true in recent years because of the following limitations:
- Increased transistor density leads to increased power consumption leads to increased temperature. The high temperatures are getting hard to counteract and could melt chips.
- To save power, voltage can be reduced. However, there’s a point at which you can’t reduce voltage anymore, otherwise the transistors can’t switch on. Also, below a certain threshold, there’s more added noise.
- Insulators on the chips are becoming thinner, leading to increased leakage power.
- Silicon transistors are now so small that it’s difficult to make them smaller without quantum mechanical effects occurring that would make them unreliable
- The cost of building new CPUs is higher as energy/cooling costs for making smaller chips grows, to the point that it’s less economically worthwhile to do so.

# Processes

An instance of a running program.

What's unique to a process:
1. Memory
2. Registers

# Operating Systems

Essentially allows many processes to execute concurrently. Gives processes fair access to resources.

## Scheduling Processes

- scheduling algorithms: round robin, give user tasks higher priority, etc

## Context Switching

- When the OS moves from one process to another, it must save the state of Process A to memory somewhere, then find/access Process B's state from memory.

## Threads vs Processes

There used to be only processes. But context switching is slow.

A process can have multiple threads. Threads have unique context but also share some context (because the whole point is to reduce context switching): eg virtual memory, file descriptors.

Modern OS's can schedule threads instead of just processes.

## Race conditions

When outcome is non-deterministic.

### Side notes

- on physical chip, there's distance between CPU, memory, video card components. This physical distance is a source of latency! Sounds obvious but I never thought about it that way.
- cache memory can be closer to each core, vs shared memory, which is why it's faster
