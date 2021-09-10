# Terms

- Most Significant Bit/Byte (MSB) = leftmost bit/byte with largest value
- Least Significant Bit/Byte (LSB) = rightmost bit/byte with largest value

### Endianness
Relates to the order in which bytes are stored in memory.

- **little-endian**: when the LSBs are stored before the MSBs
- **big-endian**: when the MSBs are stored before the LSBs

We generally write numbers with the MSB first, thus big-endian is in a sense the "normal" way.

- `0x12345678` stored using little-endian
  ```
  78 56 34 12
  ```
- `0x12345678` stored using big-endian
  ```
  12 34 56 78
  ```
### IRL
- little-endian is mostly used by processors, eg. x86_64 processors (Intel/AMD)
- big-endian is often used to transmit data, eg. TCP/IP

### Advantages of little-endian
- easy to read the value in a variety of type sizes
- easy to cast the value to a smaller type

### Advantages of big-endian
- easy to test whether number is positive or negative
- numbers stored in order in which they're printed, so binary->decimal operations are very efficient
