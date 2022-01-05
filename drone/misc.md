# Drone misc

## Cloning private repos via HTTPS

You can clone private repos in Drone via HTTPS without providing explicit authentication.

This is due to the following magic under the hood:

Drone [injects](https://discourse.drone.io/t/how-does-cloning-private-https-repos-work/2110/2) a [.netrc](https://www.gnu.org/software/inetutils/manual/html_node/The-_002enetrc-file.html) file containing the credentials of the [DRONE_REPO_OWNER](https://docs.drone.io/pipeline/environment/reference/drone-repo-owner/), into its build containers.

### Other Notes

The [DRONE_NETRC_USERNAME/PASSWORD](https://github.com/drone/runner-go/blob/f7a8ed14f07fb159568f28cd3e2841ce90417744/environ/environ.go#L213-L229) env vars are [intentionally not documented](https://discourse.drone.io/t/drone-netrc-username-documentation-usage/4485/2) as it's considered an internal implemention detail.

The documented [DRONE_NETRC_CLONE_ONLY](https://docs.drone.io/runner/docker/configuration/reference/drone-netrc-clone-only/) env var can be used to limit Drone's injection of the .netrc creds to only the clone step.
