# Bitwise operations

## Bit masking

A mask defines the bits you want to keep.
Masking = applying a mask to a value.

### Bit masking with AND
Keeps the bits that have `1`'s in the mask.

```
     1 1 1 0 1 1 0 1   [input]
(&)  0 0 1 1 1 1 0 0    [mask]
------------------------------
     0 0 1 0 1 1 0 0  [output]
```
### Bit masking with OR
Sets `1` if either input or mask bit is `1`.

```
     1 1 1 0 1 1 0 1   [input]
(|)  0 0 1 1 1 1 0 0    [mask]
------------------------------
     1 1 1 1 1 1 0 1  [output]
```

### Bit masking with XOR
Flips the bits

```
     1 1 1 0 1 1 0 1   [input]
(^)  0 0 1 1 1 1 0 0    [mask]
------------------------------
     1 1 0 1 0 0 0 1  [output]
```

## Shift operators

### Left shift `<<`
- Shifts bits to the left.
- 11011010 << 8 = 1101101000000000

### Right shift`>>`
- Shift bits to the right.
- 1101101000000000 >> 8 = 11011010
- In Go, right shift is:
  - a [logical shift](https://en.wikipedia.org/wiki/Logical_shift) (rounds to zero) on *unsigned* values
  - an [arithmetic shift](https://en.wikipedia.org/wiki/Arithmetic_shift) (rounds to -∞) on *signed* values
