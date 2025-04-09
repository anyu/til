# Monitoring

## Measuring consumer lag
- Common method of monitoring performance of Kafka consumers: measuring lag between last produced message to a topic partition and the last consumed message for that partition.
- lag = last produced message - last consumed message

### Potential causes of consumer lag
- spike in traffic
    - may need more consumers
- uneven load in partitions (eg. if message key is based on a source ID like user ID > could cause one source to be noisy > one partition loaded more than others)
