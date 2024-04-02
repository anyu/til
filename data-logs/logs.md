# Logs

Data logs as opposed to application logs.

> The magic of the log is that if it is a complete log of changes, it holds not only the contents of the final version of the table, but also allows recreating all other versions that might have existed. It is, effectively, a sort of backup of every previous state of the table.

## Physical logging vs logical logging

- physical logging = logging the contents of each row that's changed
- logical logging = logging the commands that led to the row changes

## Processing and replication approaches

- "state machine model" generally refers to an active-active model where a log of incoming requests is kept and each replica processes each request
  - eg. log transformations like "+1", "*2" -> each replica applies these transformations
- "primary-backup model" elects 1 replica as the leader and allows this leader to process requests in order of arrival and log out changes to its state from processing the requests
  - the other replicas apply the state changes the leader makes (to stay in sync), and be ready to take over as a leader if necessary
  - eg. leader executes transformations and logs the *result* like "3", "6"

## Misc

- has similarities with version control


### Resources
- https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying
- https://www.confluent.io/blog/publishing-apache-kafka-new-york-times/