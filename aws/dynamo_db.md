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

## Core concepts

- **table** = collection of items
- **item** = a collection of attributes (eg. like a row)
  - single data record in a table
- **attributes** = data attached to an item (eg. like a column)
  - not required on items, except for attirubtes that make up the primary key
- **primary key**
  - uniquely identifies an item in a table
  - two types:
    - 1) simple primary key - just a partition key (aka. 'hash key')
      - hash key is used to evenly distribute the item across a key space
    - 2) composite primary key - a parition key + sort key (aka 'range key')
      - partition key doesn't have to be globally unique if paired w/ a sort key
      - sort keys enable range-like operations (sorts items in the same partition)
      - if the partition key is unique (eg. all your order IDS are unique), don't need sort key
- **secondary indexes**
  - 1) local secondary indexes - uses the same partition key as the underlying table, but a different sort key
    - another way to resort the data, but not regroup the data
    - LSI updates are strongly consistent
  - 2) global secondary indexes (GSI)
    - defines an entirely different primary key for a table (could alternate partition and/or sort key)
    - enables querying on other attributes. Can add GSIs anytime after table is created
    - GSI updates are eventually consistent

## Behind the Scenes

- Partitions are replicated 3 ways
- sort applies before the read
- filter conditions apply after the read

### Access Options

- **scan operation**: reads over every record in table, use filter expression (eg. `country=USA` to get all users in X country)
  - inefficient, costly as you get charged for reading each row
- use global secondary indexes
- have the option of strongly consistent read (read is from primary node) or eventually consistent  read (read is from any other node; half the cost b/c there's more nodes to choose from)

### Designing Schemas

- Tenets of NoSQL data modeling:
  - Identify the access patterns (read/write workloads, query dimensions/aggregations, document workflows)
  - Avoid relational design patterns, use 1 table
- Selecting a partition key:
  - large number of distinct values
  - items are uniformly requested and randomly distributed
  - good examples: customer ID, device ID
  - bad: status, gender
- Selecting a sort key
  - model 1:n, n:n relationships
  - efficient/selective patterns
  - leverage range queries
  - examples: orders, order items

#### Resources
- [Best practices for designing & architecting with DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices.html)
- [aws dynamo lab best practices](https://amazon-dynamodb-labs.workshop.aws/game-player-data/plan-model/step1.html)

### Attributes types

| Identifier  | Type       |
| ----------- | ---------- |
| S           | string     |
| N           | number     |
| B           | binary     |
| BOOL        | boolean    |
| NULL        | null       |
| L           | list       |
| M           | map        |
| SS          | string set |
| NS          | number set |
| BS          | binary set |

## Basic setup

1. `brew install awscli`
2. If hitting AWS:
    1. Create IAM profile with DynamoDB perms
    2. Complete `aws configure`
3. If using DynamoDB locally:
    1. Download zip: https://www.dynamodbguide.com/environment-setup#optional-use-dynamodb-local
    2. Install Java onto path.
    3. Start DynamoDB
        ```sh
        java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb
        ```
    4. Run dynamodb commands with `--endpoint-url http://localhost:8000`


## Commands

#### Create a table
```sh
 aws dynamodb create-table \
  --table-name UsersTable \
  --attribute-definitions '[
    {
        "AttributeName": "Username",
        "AttributeType": "S"
    }
  ]' \
  --key-schema '[
    {
        "AttributeName": "Username",
        "KeyType": "HASH"
    }
  ]' \
  --provisioned-throughput '{
    "ReadCapacityUnits": 1,
    "WriteCapacityUnits": 1
  }'
```

#### List/describe table
```sh
aws dynamodb list-tables

aws dynamodb describe-table --table-name UsersTable
```

### Retrieve only particular attributes from an item

```sh
aws dynamodb get-item \
  --table-name UsersTable \
  --projection-expression "Age, Username" \
  --key '{"Username": {"S": "alice"}}'
```

### Describe table

```sh
aws dynamodb describe-table --table-name $TABLE_NAME
```

# Querying

```sh
❯ aws dynamodb query \
--table-name $TABLE_NAME \
--index-name my_idx_name \
--key-condition-expression "my_idx_name = :keyword" \
--expression-attribute-values '{":keyword":{"S":"SOME_VAL"}}' \
--exclusive-start-key '{"my_idx_name":{"S":"SOME_VAL"},"principal":{"S":"SOME_PRINCIPAL"},"sort_key":{"S":"SOME_SORT_KEY"},"created_sort_idxkey":{"N":"1678906760.5004647"}}' \
--no-scan-index-forward
```

NOTE: If a timestamp is being used, watch out for truncated digits/rounding. May affect which records get pulled.

# GSIs

[Attribute projections](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSI.html#GSI.Projections) = set of attributes copied from a table to a secondary index
- the partition and sort keys are always projected onto the index
- can figure what other attributes are projected: `KEYS_ONLY`, `INCLUDE`, `ALL`

## Query a GSI
- [Using Global Secondary Indexes in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSI.html)
- [Query a GSI](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GCICli.html#GCICli.QueryAnIndex)

Given this GSI:

- GSI name: `my_gsi_idx`
- GSI hash key: `gsi_hash_idxkey`
- GSI sort key: `gsi_sort_idxkey`

```sh
aws dynamodb query \
  --table-name $TABLE_NAME \
  --index-name my_gsi_idx \
  --key-condition-expression "gsi1_hash_idxkey = :keyword" \
  --expression-attribute-values '{":keyword": {"S": "some-value"} }'
```
with `:keyword` being just the variable used between the key condition expresssion and expression attribute values