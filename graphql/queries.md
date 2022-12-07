# GQL Queries

Query 
```gql
query someQueryName{
  event{
    id,
    attendeeList{
      attendees{id, name}
    }
  }
}

```

Mutation
```gql
mutation($input: MyCustomInput){
  editEvent(input: $input){
    event{
      id, title
    }
  }
}
```

with JSON input
```json
{
  "input": {
    "id": "some-id",
    "title": "some-new-title"
  }
}
```