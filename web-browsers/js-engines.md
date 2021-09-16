# JavaScript Engines

JavaScript engines execute JS code.

## V8 (Chrome V8)

- V8 can execute JS within or outside of a browser.
- V8 compiles JS into machine code and executes that code.
- Performs just-in-time (JIT) compilation (compiles as it's executing).
- More components here that optimize compilation for performance.

### Sandboxing
- Each process in V8 is sandboxed (JS functions run separately)

## Node.js (tangent)

- Node is a runtime environment for executing JS code
- Built on the V8 engine
- Does not have sandboxing like V8

---

### Resources

https://blog.sessionstack.com/how-does-javascript-actually-work-part-1-b0bacc073cf
