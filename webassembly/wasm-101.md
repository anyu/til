# WebAssembly (Wasm)

## What is it & use case
- a low-level assembly language (a compilation result of another language) with near-native performance that can run in modern browsers
- an open standard for running binary programs in browsers
- enables building an entire web app in a non-JS language
- designed initially for web, but also useful for other contrained environments (mobile, IoT)

## Web and Wasm

The web platform has two main components:
- a VM that runs the web's app code (eg. JavaScript)
- a set of web APIs that the web app uses to control browser/device functionality (eg. DOM, WebGL, IndexedDB, etc)

In the past, the VM could only load JS. Generally good enough, but not performant enough for use cases such as 3D, VR, AR, etc.

The VM can now load JS _and_ Wasm.

## Wasm primitives

- **Module**: a Wasm binary that's been compiled by the browser into machine code
- **Memory**: Resizeable ArrayBuffer that contains bytes read/written by Wasm's memory access instructions
- **Table**: Resizeable typed array of references (to functions) that can't otherwise be stored in raw bytes in Memory
- **Instance**: A Module paired with state used at runtime

Wasm JS API can be used to create these modules/memories/tables/instances.

## Using Wasm in apps

### Writing in X language targeting Wasm

1. Write in X language
2. Compile it to Wasm module

Wasm module is isolated from host environment and executes in a sandbox (a VM).

The module communicates with the host via an API.

#### Rust
- compiles to small Wasm sizes
- https://rustwasm.github.io/book/why-rust-and-webassembly.html

#### AssemblyScript
- compiles a strict variant of TypeScript to Wasm

#### Go
- Go produces large binaries so isn't a great candidate as is
- TinyGo can produce compact Wasm code, but lacks some of Go's featureset
