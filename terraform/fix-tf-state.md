# Fixing terraform state

Terraform state borked?

```shell
terraform init

# See existing state
terraform state list
terraform state show <RESOURCE>
# If resource is a collection, may need to escape quotes
# terraform state show "github_team_membership.some-team-name[\"user1\"]"

# Reconcile state as needed
terraform state rm <RESOURCE>
terraform import <RESOURCE>

# Check diff; apply once synced
terraform plan
terraform apply
```

If resource is a collection/map of resources (exemplified by existence of `for_each` in the resource definition)
eg.
```shell
github_team_membership.some-team-name["user1"]
github_team_membership.some-team-name["user2"]
github_team_membership.some-team-name["user3"]
```

will need to import each item via a loop
```shell
for gh_handle in user1 user2 user3; do
    terraform import 'github_team_membership.some-team-name['\"${gh_handle}\"']' "${GH_TEAM_ID}:${gh_handle}"
done
```
otherwise will get the following error when adding more than 1 member with individual import runs:
```shell
│ Error: Resource already managed by Terraform
│
│ Terraform is already managing a remote object for github_team_membership.some-team-name.
| To import to this address you must first remove the existing object from the state.
```

Note: Having a top level resource per item is often clearer than using collections, eg:
```shell
github_team_membership.some-team-name-user1
github_team_membership.some-team-name-user2
github_team_membership.some-team-name-user3
```
