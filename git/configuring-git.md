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
