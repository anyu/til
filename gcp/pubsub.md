# PubSub

## Subscription access

Project A service needing pull acess to a Project B topic.

1. Project B needs to create a subscription to the topic.
1. Project B needs to grant the following permissions to Project A's service account for that subscription:
    - Pub/Sub Subscriber
    - Pub/Sub Viewer
1. Test permissions:
    ```sh
    $ cat $SERVICE_ACCOUNT_JSON_CREDS > creds.json

    $ gcloud auth activate-service-account --key-file=creds.json

    Activated service account credentials for: [sa@gcp-project-id.iam.gserviceaccount.com]

    $ gcloud pubsub subscriptions pull projects/GCP_PROJECT_ID/subscriptions/SUBSCRIPTION_ID
    ```
