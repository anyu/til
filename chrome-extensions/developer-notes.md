# Chrome Extensions

Notes on developing Chrome extensions

## Extension files

1. `manifest.json`: JSON file containing extension configuration info
  - the only required file, and has a specific file name
  - must be in root directory
2. **service worker**: Script that runs in the background (in its own environment) and listens for and handles browser events
  - cannot interact directly with web page content
  - event examples: when extension is installed, new tab is created, a new bookmark is added, etc
  - can access the [Extension APIs](https://developer.chrome.com/docs/extensions/reference/extension/)
3. **content scripts**: Executes JS on a web page.
  - can read and modify DOM of pages they're injected in (but run in a separate JS environment)
  - can only use subset of Chrome APIs, but can access the rest by exchanging messages with the service worker
4. **pop up, options, side panel, chrome override, sandbox pages etc**: Other types of pages that have access to Chrome APIs.

## What extensions have access to

- all [JS browser APIs](https://developer.mozilla.org/en-US/docs/Web/API)
- [Chrome APIs](https://developer.chrome.com/docs/extensions/reference/)

## Things to be aware of

1. As of Chrome [Manifest V3](https://developer.chrome.com/docs/extensions/mv3/intro/) (Nov 2020):

    You can [no longer load and execute remotely hosted files](https://developer.chrome.com/docs/extensions/migrating/improve-security/#remove-remote-code) (eg. JS libraries hosted on CDNs). Used to be able to set `content-security-policy` in the manifest to allowlist domains.

    Workarounds:
    - Bundle minified 3rd party libs
    - Can still used remote config files loaded/cached at runtime
    - Can call a remote web service (another pro: don't have to resubmit to Chrome store)
    - Can still use remotely hosted code in sanboxed iframes

2. shadow DOMs
- shadow DOM needs to be in open state to access elements within
- might need to use timer to keep checking if shadow DOM has loaded

TODO: Give example
