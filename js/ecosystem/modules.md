# Modules

Node supports both module systems (default is based on explicit config/file extensions or Node will inspect code for either syntax)

`.cjs` files = CommonJS,
`.mjs` files = ES module

## ES Modules

If not already enabled, enable ES modules by adding to `package.json`:
```json
{
  // ...
  "type": "module",
  // ...
}
```

### Default exports/imports

A module can only have 1 default export. Default exports are used to expose a single entity as the "default" export.

The importing module can alias the name to whatever.

`module.js`
```
const myVar = 42
export default myVar;
```

`anotherModule.js`
```js
import myAlias from './module';
```

### Named exports/imports

Used when you want to expose multiple entities.

`module.js`
```
export const var1 = 42;
export const var2 = 'hello';

export function greet(name) {
    return `Hello ${name}`;
}
```

`anotherModule.js`
```js
import { var1, var2, greet } from './module';
```
