# WebAssembly (Wasm)

## What's Wasm and what's it used for?

[Wasm](https://webassembly.org/)  is a low-level assembly language (a compilation result of another language) with near-native performance that can run in modern browsers.

It's an open standard for running binary programs in browsers; enabling building an entire web app in a non-JS language.

The key features it brings to the table are:

- **Performance** - in historically JavaScript-only environments
- **Portability** - Wasm is easily bundled and distributed; provides common ground for other languages to come to the web

### How Wasm fits into Web

The web platform in general has two main components:
- a VM that runs the web's app code (eg. JavaScript)
- a set of web APIs that the web app uses to control browser/device functionality (eg. DOM, WebGL, IndexedDB, etc)

In the past, the VM could only load JS. Generally good enough, but not performant enough for use cases such as 3D, VR, AR, etc.

The VM can now load JS _and_ Wasm, which unlocks Wasm for such computationally intensive web use cases. While designed initially for web, Wasm is now also being used for other constrained environments (mobile, IoT).

## Key Wasm Concepts

- **Module**: a Wasm binary that's been compiled by the browser into machine code
- **Memory**: Resizeable ArrayBuffer that contains bytes read/written by Wasm's memory access instructions
- **Table**: Resizeable typed array of references (to functions) that can't otherwise be stored in raw bytes in Memory
- **Instance**: A Module paired with state used at runtime

Wasm JS API can be used to create these modules/memories/tables/instances.

## How to Use Wasm

The ecosystem is very young and rapidly changing, but currently the options are:

- **Port from C/C++**: Tools exist for compiling C/C++ source code to a Wasm module
- **Writing Wasm directly**: You could write directly in Wasm text and use tools to convert it to binary
- **Writing in X language targeting Wasm**: Write code in another language (eg. Go, Rust) and compile to a Wasm module

Wasm modules are isolated from the host environment and execute in a sandbox (a VM).

The module communicates with the host via an API.

### Languages Targeting Wasm

#### Rust
- compiles to small Wasm sizes
- https://rustwasm.github.io/book/why-rust-and-webassembly.html

#### Go
- Go produces large binaries so isn't a great candidate as is
- TinyGo can produce compact Wasm code, but lacks some of Go's featureset

#### AssemblyScript
- compiles a strict variant of TypeScript to Wasm
