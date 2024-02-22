# Overview of JS Runtime Environments

A JS runtime environment provides APIs/features to build JS-based software.
It includes a JS engine (interpreter + JIT compiler).

Examples of runtime environments:

- **browsers**: provides DOM API, Fetch API, timer, storage, etc
- **server environments**: provides file system access, network access, console, etc
    - eg. NodeJS, Deno
- **desktop environments**: provides GUI API, file system access, network access, console, etc
    - eg. Electron
- **mobile environments**:
    - eg. React Native

Note: The event loop is implemented in the runtime environment, not the JS engine.