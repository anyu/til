# Terraform migrations

## Migrating TF state

From one remote to another remote bucket.

1. Pull down existing state locally

    ```
    terraform state pull
    ```

2. Update backend to use new bucket

3. Migrate
    ```
    terraform init -migrate-state
    ```
