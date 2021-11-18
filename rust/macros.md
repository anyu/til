# Macros

Macros = a way of metaprogramming/code generation. Write code that generates code for you.

## Macros vs. functions

- Macros can take a **variable number of parameters**; functions must declare # of params and their type
- Macros are **expanded before the compiler interprets** the meaning of the code (eg. it can implement a trait on a type). Functions can't because they're called at runtime, and a trait needs to be implemented at compile time.
- Macros must be defined and brought into scope *before* they're called in a file; functions can be defined and called anywhere.
- Macros can be more complex to read/maintain than functions.

### Declarative macros (aka. 'macros by example', `macro_rules!` macros, just 'macros')

*NOTE: Future versions of Rust will introduce a different type of declarative macros, so don't need to invest too much time here.*

Declarative macros let you write something akin to a Rust `match` expression.

To define a declarative macro, use: `macro_rules!`

```shell
// annotation indicating this macro should be made available
// whenever the crate where the macro is defined is in scope
#[macro_export]
macro_rules! vec {
    ( $( $x:expr ),* ) => {
        {
            let mut temp_vec = Vec::new();
            $(
                temp_vec.push($x);
            )*
            temp_vec
        }
    };
}
```

- `( $( $x:expr ),* )`
    - outer parens = contains the pattern
    - inner `$()` = captures values that match the pattern within the parens for use in replacement code
    - `$x:expr` = matches any Rust expression and gives the expression the name `$x`
    - comma following `$()` = indicates a literal comma separator could optionally appear after the code matched in `$()`
    - `*` = pattern matches zero or more of whatever precedes it
- The macro body
    - `$()` = code within is generated for each part that matches `$()` in the pattern
    - `$x` is replaced with each matched expression

Usage

```shell
let v: Vec<u32> = vec![1, 2, 3];
```

Generated code
```shell
{
    let mut temp_vec = Vec::new();
    temp_vec.push(1);
    temp_vec.push(2);
    temp_vec.push(3);
    temp_vec
}
```
### Procedural macros (proc macros)

Proc macros act more like functions. They take code as input, operate on the code, and produce code as output.

- Proc macro definitions must live in their *own* crate with a special crate type.
- There are 3 types of proc macros: **custom derive macros**, **attribute-like macros**, **function-like macros**

#### Custom `derive` macros

Only works for structs and enums.

Here we have a `hello_macro` crate that defines a `HelloMacro` trait with a `hello_macro` function.

Instead of making users implement `HelloMacro` for each of their types, we provide a proc macro that users can use to get a default implementation of `hello_macro` function.

```shell
use hello_macro::HelloMacro;
use hello_macro_derive::HelloMacro;

#[derive(HelloMacro)]
struct Pancakes;

fn main() {
    Pancakes::hello_macro();
}
```

**How to create a custom derive macro**
1. Make a new crate.
2. Define the `HelloMacro` trait and its function:
   ```shell
   pub trait HelloMacro {
      fn hello_macro();
   }
   ```
3. Create a new crate:
   ```shell
   cargo new hello_macro_derive --lib
   ```
   `hello_macro_derive/Cargo.toml`:
   ```shell
   proc-macro = true

   [dependencies]
   syn = "1.0"
   quote = "1.0"
   ```

4. Define the proc macro and implement the trait
   `hello_macro_derive/src/lib.rs`:
   ```shell
   extern crate proc_macro;

   use proc_macro::TokenStream;
   use quote::quote;
   use syn;

   #[proc_macro_derive(HelloMacro)]
   pub fn hello_macro_derive(input: TokenStream) -> TokenStream {
   // Construct a representation of Rust code as a syntax tree
   // that we can manipulate
   let ast = syn::parse(input).unwrap();

       // Build the trait implementation
       impl_hello_macro(&ast)
   }

   fn impl_hello_macro(ast: &syn::DeriveInput) -> TokenStream {
   let name = &ast.ident;
   let gen = quote! {
        impl HelloMacro for #name {
            fn hello_macro() {
                println!("Hello, Macro! My name is {}!", stringify!(#name));
            }
        }
   };
   gen.into()
   }
   ```

The `hello_macro_derive` function will be called when a user specifies `#[derive(HelloMacro)]` on a type.
due to the `proc_macro_derive` annotation.

#### Attribute-like macros

Attribute-like macros allow you to create new attributes.

- They're flexible. Whereas `derive` macros only work for structs, attributes can be applied to other items like functions.
- Otherwise, works the same way as custom derive macros.

Example of an attribute named `route` that annotates functions:
```shell
#[route(GET, "/")]
fn index() {
```

Signature of macro definition function:
```shell
#[proc_macro_attribute]
pub fn route(attr: TokenStream, item: TokenStream) -> TokenStream {
```

Attribute = metadata applied to some module, used for a variety of things (conditional compilation of code, enable compiler features, etc)

#### Function-like macros

Function-like macros define macros that look like function calls.

- They can take an unknown # of arguments, like declarative macros.
- They can take a `TokenStream` param and manipulate it like other proc macros

Example function-like macro:
```shell
let sql = sql!(SELECT * FROM posts WHERE id=1);
```

Macro definition:
```shell
#[proc_macro]
pub fn sql(input: TokenStream) -> TokenStream {
```

## Popular macros

From standard lib:
```shell
use std::rc::Rc;

#[derive(Debug, Clone)]
struct SomeStruct {}
```

From serde crate:
```shell
use serde::{Deserialize, Deserializer};

#[derive(Debug, Deserialize, Serialize)]
struct SomeStruct {}
```

### Resources

- [Rust book: Macros](https://doc.rust-lang.org/book/ch19-06-macros.html)
- [The Little Book of Rust Macros](https://veykril.github.io/tlborm)
