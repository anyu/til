# V8 Optimizations

## Hidden Classes

Most JS interpreters use dictionary-like objects to store location of object property values in memory.

It's very inefficient, so instead, V8 attaches a **hidden class** to every object to optimize property access time.

Whenever a property is added to an object, a "class transition" occur where the old hidden class is switched to the new hidden class.

## Inline Caching

There are 3 main types of inline caching:

- **Monomorphic** (optimized): same type of object is always passed
- **Polymorphic** (slightly optimized): limited # of different types of objects passed
- **Megamorphic** (unoptimized): many # of different types of objects passed

## How hidden classes and inline caching related

Whene a method is called on an object, the V8 engine performs a lookup to that object' hidden class to determine the offset for accessing a specific property. 

After 2 successful calls of the same method to the same hidden class, V8 skips the hidden class lookup and simply adds the offset of the property to the object pointer itself. 

For all future calls of that method, the V8 engine assumes that the hidden class hasn’t changed, and jumps directly into the memory address for a specific property using the offsets stored from previous lookups.

## Best Practices

1. Declare object properties in constructor
    - Changing object properties results in hidden classes that force TurboFan to re-optimize.
    ```js
    class Point {
        constructor(x, y) {
            this.x = x;
            this.y = y;
        }
    }

    var p1 = new Point(11, 22);  // hidden class Point created
    var p2 = new Point(33, 44);

    p1.z = 55;  // another hidden class Point created
    ```

2. Keep object property ordering constant
    - Hidden class transitions are dependent on the order in which properties are added to an object:

    ```js
    1  function Point(x,y) {
    2    this.x = x;
    3    this.y = y;
    4  }
    5 
    7  var obj1 = new Point(1,2);
    8  var obj2 = new Point(3,4);
    9
    10 obj1.a = 5;
    11 obj1.b = 10;
    12
    13 obj2.b = 10;
    14 obj2.a = 5;
    ```
    Up until L9, these two objects shared the same hidden class.
    But since properties `a` and `b` are added in different orders, they end up with different hidden classes.


3. Fix function arg types (decrease polymorphic/megamorphic caching)
- If multiple arg types are used when calling a func, TurboFan stops optimizing.

4. Don't declare classes in the function scope
    ```js
    function createPoint(x, y) {
        class Point {
            constructor(x, y) {
                this.x = x;
                this.y = y;
            }
        }
        return new Point(x, y);
    }

    function length(point) {
        ...
    }
    ```

    Every time `createPoint` is called, a new `Point` prototype is created.
    Each new prototype has new object shape, so `length` sees a new shape with each new point. TurboFan will stop optimizing `length` if too many object shapes.

5. Use `for... in` loops
    - 4x faster than functional iteration, with arrow funcs, or `Object.keys` in a loop