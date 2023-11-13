# Git commands

#### Less frequently used Git commands I tend to forget

Checkout/cherry-pick file from other branch
```shell
git checkout $BRANCH_NAME -- $PATH_TO_FILE
```

Stash only staged changes (as of v2.35)
```shell
git stash --staged
```

Stash with label
```shell
git stash push -m "some-msg"
```

Show file list of most recent stash
```shell
git stash show
```

Show changes of most recent stash
```shell
git stash show -p
```

Show changes of specific stash
```shell
git stash show -p $STASH_INDEX
```

Drop stash
```shell
git stash drop $STASH_INDEX
```

Delete local branch
```shell
git branch -d local-branch

# delete even if branch contains unmerged/unpushed commits
git branch -D local-branch
```

Diff with only file names

```shell
git diff --name-only
```

```shell
git diff --name-only head head~1
```