# Using pre-commit to manage Git hooks

### [Pre-commit](https://pre-commit.com/) quickstart

1. Install pre-commit
```
brew install pre-commit
```
2. Seed required `.pre-commit-config.yaml` config file with basic hooks
```
pre-commit sample-config > .pre-commit-config.yaml
```
3. Install git hooks
```
pre-commit install
```

### Cheatsheet

To run hook manually
```
pre-commit run --all-files
```

When desired, skip hook
```
git commit --no-verify
```

### Config

#### Run pre-commit against subdirectory example

```yaml
...
- id: golangci-lint
  name: Golang linting
  language: system
  entry: /bin/bash -c "cd GO_SUBDIR; pre-commit-golangci-lint.sh"
  pass_filenames: false
  types: [go]
```
