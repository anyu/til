# Kafka 101

## What is it

- "A distributed event streaming platform"
- Generally used for real-time data pipelines and streaming applications
- Essentially a pubsub messaging system, but especially good for high throughput/scalability/fault tolerance

## Core Concepts

### Producer
- Sends/publishes data to Kafka

### Consumer
- Reads/subscribes to data from Kafka

### Topic
- Data published to topics
- Topics are split up into partitions for scalability, replicated for fault tolerance

### Broker
- A broker is a Kafka server that handles read/write requests. Kafka runs as a cluster of these brokers.

### Consumer Group
- Multiple consumers can form a group to share a workload (shares a group ID)
- Kafka ensures each message is processed only **once per group**, distributed across consumers.
- Consumers in the same group can't read from the same partition

## High Level
1. Connect to a Kafka broker.
1. Subscribe to a topic.
3. Consume messages/events as they arrive.
4. Process each event.

