# ghz

```sh
ghz \
--cacert certs/ca.pem \
--cert certs/cert.pem \
--key certs/key.pem \
--proto PATH_TO_PROTO_FILE.proto \
--call=my.custom.server.Service/Method \
--import-paths="./proto" \
--connections=1 \
-c 1 \
-n 5 --load-schedule=step --load-start=1 --load-end=5 --load-step=1 --load-step-duration=1s \
-d '{"some_field": 44}' --debug debug.json SERVER_URL:443
```
