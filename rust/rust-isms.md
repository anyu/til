# Rust-isms

## Destructuring assignments

Currently, destructuring into tuples into an existing variable is not supported in the stable release of Rust.
(it's in the nightly release)

eg. The following results in a compilation error:
```rust
fn main() {
    let mut my_var1 = String::new();
    let mut my_var2 = String::new();
    (my_var1, my_var2) = some_func_that_returns_tuple();
    print!("{} {}", my_var1, my_var2)
}

fn some_func_that_returns_tuple() -> (String, String) {
    (String::from("hey"),String::from("yo"))
}
```
```sh
error[E0658]: destructuring assignments are unstable
 --> src/main.rs:4:24
  |
4 |     (my_var1, my_var2) = some_func_that_returns_tuple();
  |     ------------------ ^
  |     |
  |     cannot assign to this expression
```

The workaround (separately binding variables to existing):
```rust
fn main() {
    let mut my_var1 = String::new();
    let mut my_var2 = String::new();
    let (temp_var1, temp_var2) = some_func_that_returns_tuple();
    my_var1 = temp_var1;
    my_var2 = temp_var2;
    print!("{} {}", my_var1, my_var2)
}

fn some_func_that_returns_tuple() -> (String, String) {
    (String::from("hey"),String::from("yo"))
}
```

- https://github.com/rust-lang/rfcs/pull/2909
- https://stackoverflow.com/questions/34304341/can-i-destructure-a-tuple-without-binding-the-result-to-a-new-variable-in-a-let
