# gh-cli

[GitHub CLI](https://github.com/cli/cli) tool.
- [Docs](https://cli.github.com/manual/)

```shell
$ brew install gh
$ gh auth login
```

### Make Github API requests
- [GH API docs](https://docs.github.com/en/rest)

#### Get repo information
```shell
gh api /repos/ORG/REPO
```

#### Delete branch protection
```shell
$  gh api -X DELETE /repos/ORG/REPO/branches/BRANCH/protection
```
