# Bit arrays

*aka. bit sets, bit maps, bit strings, bit vectors*

## What's a bit array?

A data structure that stores bool values or bits (sometimes refered to as "flags") in an array. A bit can be `1` or `0`.

`0 1 1 0 1 1 0 1` is an 8-bit array.

Each bit can have 2 values, so the capacity of a bit array = 2^(number of bits).

So, an 8-bit array has a capacity of 2^8 = 256.

## Bit array density

**Population** or **hamming weight** refers to the number of 1's in a bit array.

- A bit array is **dense** if each bit has a >=50% chance of being 1. Less compressable.
- A bit array is **sparse** if each bit is less likely to be 1. More compressable.

Compression often done through run length encoding.

## Pros and cons

### Pros
- extremely compact

### Cons
- without compression, they're wasteful for sparse sets
- accessing individual elements can be expensive
