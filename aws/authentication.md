# AWS Authentication

## Configuration & login

There are a number of config and cache files involved with logging in to AWS programmatically that can be hard to keep straight.

### AWS SSO Login

### TLDR of aws config files

| Dir/file name        | Description
| :------------- |:-------------
| `~/.aws/config` | - Primary config file for non-sensitive credentials info<br>- Created manually or by `aws configure`
| `~/.aws/credentials`    | - Default config file for *sensitive* credentials info<br>- Created by `aws configure`<br>- Notably and unfortunately NOT created by `aws sso login`
| `~/.aws/sso/cache`      | - Cache directory of SSO tokens<br>- Created by `aws sso login`
| `~/.aws/cli/cache`      | - Cache directory of CLI creds<br>- Created by `aws sts get-caller-identity`

Note the [precedence](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-precedence) in which config/creds are applied.
Reference AWS' [official docs](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) for more details.

### Get logged in

1. Create such files at `~/.aws/config` with [named profiles](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html) pointing to your accounts:


```go
[profile dev]
sso_start_url = https://SOME-START-URL.awsapps.com/start
sso_region = SOME_REGION
sso_account_id = SOME_ACCOUNT_ID
sso_role_name = AWSAdministratorAccess
region = SOME_REGION
output = json

[profile prd]
sso_start_url = https://SOME-START-URL.awsapps.com/start
sso_region = SOME_REGION
sso_account_id = SOME_ACCOUNT_ID
sso_role_name = AWSAdministratorAccess
region = SOME_REGION
output = json
```

This information can also be found via the AWS admin console.

2. Run the [aws-sso-login.sh](../scripts/aws-sso-login.sh) script. You'll be prompted to log in via the browser in the process.
   Reference the script comments for details on what's happening under the hood.

### Authenticating Docker to ECR

If you need to pull an image from a private ECR, you'll need to authenticate Docker to ECR:

```shell
# dev
aws ecr get-login-password --region SOME_REGION | docker login --username AWS --password-stdin AWS_ECR_URL.amazonaws.com
```
