# Testing

## Unit tests

[Rust By Example: Unit testing](https://doc.rust-lang.org/rust-by-example/testing/unit_testing.html)

```sh
cargo test --lib
```

## Mocking

Options:
- [Conditional compilation](https://klau.si/blog/mocking-in-rust-with-conditional-compilation/) using `#[cfg(test)]` and `#[cfg(not(test))]`
   - cons: can only mock out a function once; pros: simplicity
- Refactor code to use traits/generics
