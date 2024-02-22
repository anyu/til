# Transpilers

## SWC (speedy web compiler)
- modern, faster Babel
- devs don't use directly, but used by other tools (eg. Vite 4 moved from Babel to SWC, Turbopack)

## Babel
- transpiles latest JS (ES6/ECMAScript 2015+) to older JS (ES5-)
- open source
- could be used w/ tsc to transpile TS to JS if more extensive support for optimizing JS code is needed
- written in JS, so slower than newer tools on the block

## Others
- esbuild has some transpiling features