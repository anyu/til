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
    - 2) composite primary key - a parition key + sort key (aka 'range key')
      - partition key doesn't have to be globally unique if paired w/ a sort key
      - sort keys enable range-like operations (sorts items in the same partition)
      - if the partition key is unique (eg. all your order IDS are unique), don't need sort key
- **secondary indexes**
  - 1) local secondary indexes - uses the same parittion key as the underlying table, but a different sort key
  - 2) global secondary indexes (GSI) 
    - defines an entirely different primary key for a table
    - enables querying on other attributes. Can add GSIs anytime after table is created

### Access Options

- **scan operation**: reads over every record in table, use filter expression (eg. `country=USA` to get all users in X country)
  - inefficient, costly as you get charged for reading each row 
- use global secondary indexes

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
  --tabe=le-name UsersTable \
  --projection-expression "Age, Username" \
  --key '{"Username": {"S": "alice"}}'
```