# JS Performance 101
- JS has more potential for negative performance impact than even images/video
- In simplest cases, reduce use of it if possible (remove unused code, using built-in browser features, CSS animations instead, etc)
- Split JS into multiple files so can handle critical and non-critical parts separately
- Minify, compress code

## Browser page rendering process

1. HTML parsed in order where it appears on page.
2. When CSS encountered, it's parsed. Linked media assets (web fonts, images) started getting fetched.
3. When JS encountered, browser parses, evaluates, and runs it.
4. Browser figures out how each HTML element is styled given the CSS applied to it.
5. Styled result is painted to screen.

## JS execution (step 3 in more detail)

The default is that JS parsing/execution blocks rendering; parsing of any HTML (and thus styling/painting) after encountered JS is blocked until the script is handled.

### Optimization tips

- **Load critical scripts asap**: Can load inside `<head>`, but still render-blocking. Alternative is to use `rel="preload"`, which fetches JS asap, then include the script where wanted. This doesn't guarantee the script will be loaded by the time it gets included, but will be downloaded sooner. Shortens render-blocking time.
    ```js
    <head>
    ...
    <!-- Preload a JavaScript file -->
    <link rel="preload" href="important-js.js" as="script" />
    <!-- Preload a JavaScript module -->
    <link rel="modulepreload" href="important-module.js" />
    ...
    </head>
    ```
- **Defer non-critical JS execution**: Add `async` to script to have it be fetched in parallel to DOM parsing. (alternative is `defer`, which has similar effect). Or use DOM scripting/dynamic module loading to not load the JS until some event trigger.
- **Break down long tasks**: JS is single-threaded, so the main thread can only run 1 task at a time (execeptions being web workers). Single task that take >50ms to run is considered a long task.
    - **Break code into separate functions & yield to main thread**: Browser can then handle high-priority tasks (eg. updating UI) in between split up code.
    Using `yield` and/or `setTimeout()`:
    ```js
    function yield() {
        return new Promise((resolve) => {
            setTimeout(resolve, 0);
        });
    }
    ```
- **JS animations**: Use CSS animations instead if possible (can use Web Animations API to hook into CSS animations w/ JS); use browser to perform DOM animations > manipulating inline styles w/ JS
    - `Window.requestAnimationFrame()` > `setInterval`
- **Optimize event performance**: Continuous events can be expensive, so when they're no longer needed, remove event listeners (`removeEventListener`)
    - Use event delegation when possible. Let's say some code should run if a user interacts with any of a large # of child elements. You can set an event listener on the parent instead of on each child individually. Fewer event listeners = better performance.
- **Reduce DOM manipuation or batch them**: They're computationally expensive, so try to batch in groups vs firing off individual changes.
    - eg. If adding large chunk of HTML, build entire fragment before appending to DOM in one go.
- **Simplify HTML**: the simpler the DOM treee, the faster
- **Reduce looped code**: Loops are expensive. Avoid full loop when unnecessary by using `break`, `continue`. Extract code that doesn't need to be in loop.
- **Move computation off main thread**: async JS is JS that doesn't block main thread. Async APIs are good for handling ops that are particularly bad if they block the main thread (eg fetching resources from network, accessing file system file, opening webcam). Async APIs can execute functions while keeping main thread running subsequent code, and return results from those funcs in the future.
    - **Use web workers**: Creates a separate thread to run JS that sends result back to main thread. Constraint being you can't do DOM scripting inside a web worker.
    - **Use WebGPU**: Browser API that can access underlying system's GPU to carry high performance computations.
- **Remove dead code**: aka tree shaking. Don't include unused modules when bundling during build process to reduce size of code.
    - Newer versions of bundlers (eg. Webpack 4) have tree-shaking configurations
    - Older versions of bundlers may mark code as unused, but not necessarily remove it.
    - Beware of side effects, can mark `sideEffects` in config to skip tree shaking a file