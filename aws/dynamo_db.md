# AWS DynamoDB

A managed, serverless key-value NoSQL DB -- optimized for high performance at scale.

## Use cases / Benefits
- easy to scale out horizontally
- high availability: high uptime guarantee
- durability: DynamoDB stores multiple copies of data across multiple nodes
- ideal for applications with **known access patterns** 
- integrates well with other AWS Services
- cost effective 

## Cons
- may find it harder to perform certain queries if access patterns change

## Management

- can access via APIs, but more commonly via ORMs (python = boto3)
- IAM authorization

## Concepts

- **Tables** = collection of items
- **Items** = collections of attributes or KV pairs (eg. the columns)
- primary keys can consist of a **partition key** and **sort key**
  - partition key doesn't have to be globally unique if paired w/ a sort key
  - sort keys enable range-like operations
  - if partition key is unique (eg. all your order IDS are unique), don't need sort key

### Access Options

- **scan operation**: reads over every record in table, use filter expression (eg. `country=USA` to get all users in X country)
  - inefficient, costly as you get charged for reading each row 
- **global secondary index** (GSI): enables querying on other attributes
  - can add GSIs anytime after table is created