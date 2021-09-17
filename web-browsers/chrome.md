# Chrome

## Browser architecture

**Processes**

| Process  | What it controls                                                                                           |
|----------|------------------------------------------------------------------------------------------------------------|
| Browser  | Controls "chrome" part (address bar/bookmarks/back) and privileged actions (network requests, file access) |
| Renderer | Controls anything inside the tab where site is displayed                                                   |
| Plugin   | Controls any plugins                                                                                       |
| GPU      | Handles GPU tasks in isolation from other processes                                                        |

(can see all in Task Manager)

The browser process coordinates with other processes, such as the renderer, plugin, utility, GPU processes.

### Benefits of multi-process architecture

In simplest case, each tab has own render process.

- isolates unresponsive renderer processes from others
- security & sandboxing: file access is restricted to browser, renderer process
- processes have own private memory space, so often contain copies of common infra (eg. V8)
  - means more memory usage (why Chrome has a limit of # of tabs open). If it starts hitting limit, starts running multiple tabs from the same site in 1 process)

### More memory optimizations
- On powerful machine, Chrome splits services (browser programs) into different processes
- On constrained device, Chrome merges some services into one process

### Site isolation
- Chrome has started running a separate renderer process for each cross-site iframe; not just a separate renderer process per tab
- running Ctrl+F on a page may mean searching across different renderer processes!

## Under the hood: Navigating to a site

When a user types into the address bar...

**Step 1: Handle input**

Browser processes' UI thread parses input to determine if it's a query or URL

**Step 2: Start navigation**

On submit, UI thread initiates a network call to get site content
   - Network thread goes through DNS lookup, establishes TLS connection

**Step 3: Read response**

Once response body comes in, network thread checks what the content type really is
- If content is an HTML file, network thread passes the data to the renderer process
- If content is a ZIP file, network thread passes the data to download manager

**Step 4: Find a renderer process**

1. The network thread tells UI thread that the data is ready.
1. UI thread finds a renderer process to render the page.

**Step 5: Commit navigation**

1. An IPC is sent from browser process to renderer process to commit the navigation.
1. Data is also passed to the renderer process.
1. Once browser process gets confirmation, the navigation is complete.

## Under the hood: Rendering a page

> The renderer process is responsible for everything that happens within a tab, including executing JavaScript code.

When the renderer process receives the commit for a navigation and starts receiving HTML data...

**Step 1: Parsing**

1. **DOM construction** - main thread in renderer process parses HTML and turns it into a DOM.
  - DOM = browser's internal representation of the page

2. **Subresource loading** - a preloader scanner runs concurrently, looking for image or link tags. Sends requests to network thread.

3. **JavaScript code** - when the HTML parser encounters a `<script>` tag, it pauses HTML parsing and loads/parses/executes the JS. This is because JS can change the entire DOM structure.

4. **CSS calculation** - main thread parses CSS and determines computed style for each DOM node.

**Step 2: Layout**

1. Layout tree - main thread walks through the DOM+computed style to create layout tree (xy coordinates, bounding boxes)
   - only contains info on what's visible on the page (eg. `display: none` elements are not part of the layout tree)

**Step 3: Paint**

1. **Determining order** - main thread walks through layout tree and creates paint records (eg. what goes in front of what, z-index)


 **Step 4: Compositing**

 1. **Rasterizing** - transforming info into screen pixels

---

### Resources
- https://developers.google.com/web/updates/2018/09/inside-browser-part1
- [The Google Chrome Comic](https://www.google.com/googlebooks/chrome/big_00.html)
