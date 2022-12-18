# Bashisms

`export` exports the variable assignment to child processes of the shell in which the export command was ran.

The CLI environment is the parent of the script's shell, so it does not see the variable assignment.

You can use the `.` (or `source`) bash command to execute the script commands in the current shell environment:

```sh
source ./script.sh
echo "$BASE"
```
