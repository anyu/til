# Vault

## Authentication

1. Store GH PAT at `$HOME/.config/vault/github`.
1. Log in w/ GH PAT: `vault login -method=github token=$(cat $HOME/.config/vault/github)`
1. Resulting Vault token for subsequent API requests is cached at: `~/.vault-token`
