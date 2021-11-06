# Docker

## Volumes vs. Bind mounts vs tmpfs

### Bind mounts
- Early Docker feature
- Exposes a file or directory on host machine to container
- The file does NOT need to exist on your host already; it'll get created if not exist
- Bind mounts rely on host machine's filesystem
- You can change the host filesystem via container processes!
- More limited than volumes

### Volumes

- Completely handled by Docker; independent from your host machine dir structure
- A new directory is created within Docker's storage directory on the host machine. You can also store volumes on remote hosts.
- Volume benefits
  - Storage isn't coupled to container lifecycle
  - You can attach volumes to multiple running container simultaneously
  - Doesn't increase Docker container size

### tmpfs mounts

- Only available w/ Docker on Linux
- Temporary mount that only persists in host memory; removed when container stops. Files are not persisted.
- Good for secrets you don't want on either host or container
- Limitations: can't share `tmpfs` mount between containers

## RUN vs CMD vs ENTRYPOINT

`RUN`: Runs a command and commits the result.

`CMD`: Used to specify a default command to run if user does not provide via command line. Does not execut anything at *build* time.

`ENTRYPOINT`: Used to set commands that will ALWAYS run when container is initiated; can't be ignored or overriden.

## shell vs exec form

- **Shell form**: `RUN <command>`
  - Commands are run in a shell, defaults to `/bin/sh -c` on Linux
  - Written without brackets
- **Exec form**: `RUN ["executable", "param1", "param2"]`
  - Commands are run directly, not through a shell, so shell processing does not happen
  - Written with brackets
  - Removes the extra shell process
  - If shell processing is desired, either use shell form or execute a shell directly: `RUN [ "sh", "-c", "echo $HOME" ]`

Recommended forms:
- `RUN`: shell
- `ENTRYPOINT`: exec
- `CMD`: exec

Rule of thumb: use exec form unless shell features are needed; but also if shell features are needed for ENTRYPOINT or CMD, consider writing a shell script and executing with exec form.