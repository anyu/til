# Rust 101

## CLI Cheatsheet
```shell
# Compile
$ rustc main.rs

# Run
$ ./main

# New Cargo project
$ cargo new my_project

# Compile cargo project; creates binary in `target/debug`
$ cargo build

# Compile and run cargo project
$ cargo run

# Check compilability but does not produce binary
$ cargo check

# Compile w/ optimizations; creates binary in `target/release`
$ cargo build --release

# Open docs for dependencies
$ cargo doc --open
```

## GitHub Cargo dep failures

```sh
eval `ssh-agent -s`
ssh-add
```

## Rust Package Layout

[Conventional layout](https://doc.rust-lang.org/cargo/guide/project-layout.html):
```shell
├── Cargo.lock
├── Cargo.toml
├── src/
│   ├── lib.rs  # default library file
│   ├── main.rs # default executable file
│   └── bin/ # place for other executables
│       ├── named-executable.rs
│       ├── another-executable.rs
│       └── multi-file-executable/
│           ├── main.rs
│           └── some_module.rs
├── benches/
│   ├── large-input.rs
│   └── multi-file-bench/
│       ├── main.rs
│       └── bench_module.rs
├── examples/
│   ├── simple.rs
│   └── multi-file-example/
│       ├── main.rs
│       └── ex_module.rs
└── tests/
    ├── some-integration-tests.rs
    └── multi-file-test/
        ├── main.rs
        └── test_module.rs
```
