# Leapp

https://docs.leapp.cloud

Tool for faciliating access to AWS resources.


## Installation

If installing the CLI ([leapp-cli](https://formulae.brew.sh/formula/leapp-cli)) and hit this underlying dependency error (`mach-o file, but is an incompatible architecture (have 'arm64', file, need 'x86_64)`), try running:

```sh
npm install -g @noovolari/leapp-cli
```

per somewhat [buried docs](https://github.com/Noovolari/leapp/blob/master/docs/cli/index.md)

### Handy commands

Open session in web console
```sh
leapp session open-web-console --sessionId $(leapp session list -x | grep SESSION_NAME | awk '{print $1}')
```

Start session
```sh
leapp session start --sessionId $(leapp session list -x | grep SESSION_NAME | awk '{print $1}')
```

Useful to add these as aliases

```sh
alias leapp-SESSION_NAME="leapp session start --sessionId $(leapp session list -x | SESSION_NAME | awk '{print $1}')"
alias leapp-SESSION_NAME-console="leapp session open-web-console --sessionId $(leapp session list -x | grep SESSION_NAME | awk '{print $1}')"
```