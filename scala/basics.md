
### Rename imports to avoid collisions

```scala
// Rename so both Java and Scala's Array classes can be used
import java.lang.reflect.{Array as JavaArray};
```

### Print binary representation of integer
```scala
val i = 24
println(s"$i in binary: ${Integer.toBinaryString(i)}") // 24 in binary: 11000
```

### Compute md5 hash
https://scastie.scala-lang.org/knRVEoe9RwuhjTQfgpywyg

```scala
import java.security.MessageDigest
import java.util.Arrays;

val input = "heyoo"

val hash = MessageDigest.getInstance("MD5").digest(input.getBytes("UTF-8")) // results in a 16 byte array
val byteArrayStr = Arrays.toString(hash) // convert to string for printing
println(s"md5 byteArrayStr: $byteArrayStr")
```

### Initialize byte array
```scala
import java.util.Arrays;

// need to cast elements to bytes since 192, 168 are outside the range of byte literals, [-128, 127].
val byteArray = Array(192, 168, 1, 1).map(_.toByte)
val byteArrayStr = Arrays.toString(byteArray)
println(s"md5 byteArrayStr: $byteArrayStr")
```

### Get last byte of byte array
```scala
import java.util.Arrays;
import java.lang.reflect.{Array as JavaArray}; // Rename import since also need Scala Array class

val byteArray = Array(192, 168, 1, 1).map(_.toByte)
val byteArrayStr = Arrays.toString(byteArray)
println(s"md5 byteArrayStr: $byteArrayStr")

val lastByte = JavaArray.getByte(byteArray, byteArray.size-1)

// print decimal and binary representations
println(s"lastByte: $lastByte, ${Integer.toBinaryString(lastByte)}")
```

### Convert from signed to unsigned bytes

In Java/Scala, a byte is an 8-bit signed data type.

The leftmost bit denotes the sign (`0` = positive, `1` = negative).
The remaining bits represents values from `-128 (-2^7)` to `127 (2^7-1)`, so out of the 8 bits, only 7 bits store values, which is why the values only go up to 127.

Java/Scala doesn’t have unsigned bytes (whose values range from `0` to `255`).

To make an unsigned byte, we can cast the byte into an int* and mask (bitwise AND) the new int with `0xff` (hexadecimal representation of `255`*) to get just the last 8 bits.

**an int16 is needed at a minimum, as the extra values (128 – 255) are unable to fit into a single byte. int32 is Java's default int so that works too*

**`0xff` = 255 in unsigned decimal = -127 in signed decimal = 11111111 in binary*

```scala
val b: Byte = -127 // or if outside -127 to 128 range, -192.toByte
val unsignedb = b & 0xff
println(s"unsignedb: $unsignedb, ${Integer.toBinaryString(unsignedb)}")
 ```

 ### Bitshift operators

 ```scala

val bitShiftSecondLastByte = secondLastByte << 8
println(s"bitShiftSecondLastByte: $bitShiftSecondLastByte, ${Integer.toBinaryString(bitShiftSecondLastByte)}")
 ```
