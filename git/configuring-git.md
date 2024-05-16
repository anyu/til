# Configuring git

If `~/.gitconfig` has this set up:
```shell
[url "ssh://git@github.com/"]
	insteadOf = https://github.com/
```

May need to generate SSH key and add to agent
```shell
eval `ssh-agent -s`
ssh-add
```

## Setting up multiple profiles

Have two separate gitconfigs:

```
.gitconfig
.gitconfig-personal
```

In `.gitconfig`:

```
[user]
	email = hi@work-email.com
[core]
	sshCommand = ssh -i ~/.ssh/id_rsa_work
...
# This needs to be at end (or at least after user?)
# Note that if dir is not a git directory, final `/` is needed
[includeIf "gitdir:~/Desktop/personal/"]
	path = .gitconfig-personal
```

In `.gitconfig-personal`:

```
[user]
	email = hi@personal-email.com
[core]
	sshCommand = ssh -i ~/.ssh/id_rsa_personal
```	