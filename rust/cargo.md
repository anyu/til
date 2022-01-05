# Cargo

## Importing private dependencies

#### Add dependency to cargo.Toml via HTTPS

In `Cargo.toml` ([src](https://doc.rust-lang.org/cargo/reference/specifying-dependencies.html#specifying-dependencies-from-git-repositories))
```
[dependencies]
some-dep = { git = "https://github.com/some-dep" }
```

In `.cargo/config.toml` ([src](https://doc.rust-lang.org/cargo/reference/config.html#netgit-fetch-with-cli))
```
[net]
git-fetch-with-cli = true   # use the `git` executable for git operations
```

If the git binary is already authenticated, you're good to go.

### Resources
- [Cargo Git Authentication](https://doc.rust-lang.org/cargo/appendix/git-authentication.html)
