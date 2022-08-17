# AWS Simple Queue Service (SQS)

A distributed queuing system.

- Messages are NOT pushed to receivers. Receivers have to poll.
- Messages can only be stored for a short duration (max 14 days)
- Messages can’t be received by multiple receivers at the same time.
- Polling inherently introduces latency
- Use case: Decoupling applications and allowing parallel asynchronous processing

Often used with SNS.
