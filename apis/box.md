# Box.com API

### Basic API call with [Box Python SDK](https://github.com/box/box-python-sdk)

1. Set up an app with standard Oauth2 via [dev console](https://app.box.com/developers/console).
1. Run
    ```python
    #!/usr/bin/env python3

    from boxsdk import OAuth2, Client,  LoggingClient
    from boxsdk.object.folder import Folder
    import json

    auth = OAuth2(
        client_id='$CLIENT_ID',
        client_secret='$CLIENT_SECRET',
        access_token='$ACCESS_TOKEN'
    )
    client = Client(auth)
    # for verbose networking details
    # client = LoggingClient(auth) 

    user = client.user().get()
    print(f'The current user ID is {user.id}')

    # GET folder info call
    # https://developer.box.com/reference/get-folders-id/
    folder = client.folder(folder_id='$FOLDER_ID').get(
        # optional
        # extra_network_parameters={"timeout": 2},
    )

    print(json.dumps(folder.response_object))
    ```