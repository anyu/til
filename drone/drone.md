# Drone

## Drone CLI
View build logs
```shell
drone log view PIPELINE_NAME BUILD_ID STAGE_ID STEP_ID

# drone log outputs to stderr, so need to capture stderr to write to file
drone log view PIPELINE_NAME BUILD_ID STAGE_ID STEP_ID 2> output.txt
```

View repo info
```shell
drone repo info ORG/REPO
```

Assume ownership
```shell
drone repo chown ORG/REPO
```

---

## Drone Pipeline

To clone additional git repo

```
...
steps:
  - name: clone-additional-repo
    image: docker:git
    commands:
      - git clone https://github.com/ORG/REPO.git
```
