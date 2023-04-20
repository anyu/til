# Structuring React Projects

## Simple Folder Structure

```
└── src/
    └── assets/ # static files (images, fonts)
    └── components/ # components
        └── Button.tsx
        └── Card.tsx
    └── config/ # global configurations
    └── hooks/  # all hooks
        └── useFetch.tsx  
    └── __tests__/ # all tests
        └── components/ # components
            └── Button.test.tsx
            └── Card.test.tsx
        └── hooks/
            └── useFetch.test.tsx         
    └── index.tsx # entry point, the public API
  ```

## Intermediate Folder Structure

Introduces pages, more subfolders, colocated tests.

```
└── src/ 
    └── assets/ # static files (images, fonts)
    └── components/ # shared components
        └── __tests__/
            └── Button.test.tsx
        ├── button/
            └── Button.tsx
    │   ├── card/
    │   ├── modal/
    └── config/ # global configurations
    ├── context/
    │   └── MyProductContextProvider.tsx    
    └── hooks/  # shared hooks
        └── useFetch.tsx    
    └── pages/ # distinct pages
        └── Home/
        └── Login/        
            └── __tests__/
            └── index.tsx
            └── LoginForm.tsx
            └── useLogin.tsx  # login specific hook        
    └── styles/ # shared styles
    └── types/ # shared types
    └── utils/ # shared utilities
    └── index.tsx # entry point, the public API
  ```

## Advanced Folder Structure

Introduces features, simplifies pages, more granular folders.

```
└── src/
    └── assets/ # static files (images, fonts)
    └── components/ # shared components
        └── __tests__/
            └── Button.test.tsx
        ├── button/
            └── Button.tsx
    │   ├── card/
    │   ├── modal/
    └── config/ # global configurations
    ├── context/
    │   └── MyProductContextProvider.tsx  
    └── hooks/  # shared hooks
        └── useFetch.tsx         
    └── features/ # distinct pages
        └── authentication/
            └── components/        
            └── hooks/
            └── services/
            └── index.tsx
        └── todos/
    └── pages/ # simpler files that group together features
        └── Home.tsx 
        └── Login.ts
    └── services/ # code interacting witht external APIs
    └── styles/ # shared styles
    └── types/ # shared types
    └── utils/ # shared utilities
    └── index.tsx # entry point, the public API
  ```

Additional common folders:
  ```
    └── routes/ # route components
    └── data/ # data assets, eg JSON files
    └── lib/ # integrations with external libs
  ```

## Imports

### Default imports and exports

Every module can only have 1 default export

`MyComponent.js`
```
export default SOME_CONST
```

`OtherComponent.js`
```js
import SOME_CONST from MyComponent
```

### Named imports and exports

`MyComponent.js`
```
export { OTHER_CONST }
```

`OtherComponent.js`
```js
import { OTHER_CONST } from MyComponent
```
