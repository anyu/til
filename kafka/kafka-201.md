# Kafka 201

When a new consumer joins or leaves a group, Kafka needs to rebalance the partitions, which can lead to reassignment of partitions to different consumers or message re-processing if partitions are reassigned.

This is the default behavior w/o static membership.

## Static Membership
Static membership is a Kafka 2.4+ feature that allows Kafka to reduce rebalancing events when a consumer joins/leaves.

Kafka tries to reuse existing partition assignments for remaining consumers and only rebalances when absolutely required (eg. consumer crashes or leaves), minimizing rebalance disruptions and change or re-processing messages.

### How It Works
- Each consumer in a group gets a unique member ID, and Kafka tracks that.
- Sticky assignment: new consumers get assigned available partitions, and existing consumers keep their old assignments.

### Sarama's Static Membership implementation
- Allows choice of specific rebalance strategy

## Tracking consumer offet

- When a Kafka consumer reads a message, Kafka tracks the "offset" (pointer) of messages that have been consumed.
- Consumers typically commit offsets to Kafka to record the last message they have successfully processed
- If consumer crashes, it picks up from the last committed offset
- The Kafka broker stores offsets for each group in a metadata topic (`consumer offsets`)