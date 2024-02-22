# Node

- runs on top of V8 engine
- highly scalable and performant (still limited due to single-thread, but worker threads is addressing this)
- mature
- event loop allows entire app to run on single thread w/o bocking
- outsources async blocking operatons to a 3rd party library, `libuv`
- new feature Worker Threads enable isolated JS runtimes to be spun up for multi-threading/parallel processing
- cons: easy to get into callback hell when doing async programming (can be ameliorated with Promises, async/await)