# zsh

## Slow startup times

### Checking what's taking so long

Add at the beginnning and end of `.zshrc` file:

```sh
zmodload zsh/zprof

# zshrc contents

zprof
```