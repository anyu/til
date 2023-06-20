# Tracking Data Changes - RDBS

Often, we may need to keep track of historical data changes in a relational DB. This could be referred to as:
- tracking historical changes
- versioning
- audit trail / audit log
- temporal tracking

An optimal design depends on the use case: how often various fields change, how likely multiple fields change at the same time, how previous changes are accessed, etc.

Let's use a specific example: managing a habit schedule.

`Habits` table

| Column        | Data Type
| :------------- |:-------------
| id | uuid
| created_at | timestamp
| habit_name | text
| days_of_week | string
| schedule_type | enum
| duration | number
| active | boolean

In this example, the use case are:
- I want to track many habits at the same time. 
- I'm likely to change `days_of_week`, `schedule_type`, and `duration` for a particular habit.
- I'd like to be able to see what all my habit schedules were at any given point in the past.
- A habit can already be `active` or not active

## Using `Effective From/To` fields

In this approach, we use the same existing table and add `effective_from` and `effective_to` fields:

| Column        | Data Type
| :------------- |:-------------
| id | uuid
| created_at | timestamp
| habit_name | text
| days_of_week | string
| schedule_type | enum
| duration | number
| active | boolean
| **effective_from** | timestamp
| **effective_to** | timestamp

`effective_to` starts out as `null` for existing records.

When an update occurs where a habit field is changed, we add an `effective_to` to the existing record, and add a new record with `effective_from` as the current timestamp.

To get the latest habit schedule, query all records where the `effective_to` is `null`.

### Pros
- Uses 1 table
- Easy to understand

### Cons
- Existing table needs migration for new columns
- If there are other tables keying off of `id`, they'd need to take into account the new id. May be a pain to keep in sync...

## Using a history table

In this approach, we introduce a *separate* table called `HabitsHistory`.
This may also work better with `effective_from`, `effective_to` fields, if we want to be able to query history within a date range.

| Column        | Data Type
| :------------- |:-------------
| id | uuid
| created_at | timestamp
| habit_name | text
| days_of_week | string
| schedule_type | enum
| duration | number
| active | boolean
| **effective_from** | timestamp
| **effective_to** | timestamp

When an update happens, we create a new record in `HabitsHistory` with the `Habits`'s `created_at` time as `HabitsHistory`'s `effective_from` value and the current timestamp as its `effective_to` value. 

Then we update the `Habits` table with the new value.

### Pros
- Doesn't affect existing table

### Cons
- Whole record is duplicated even if only 1 field changes

### Using an audit table

This approach tracks just the change/delta that tooks place.

| Column        | Data Type
| :------------- |:-------------
| id | uuid
| changed_field | text
| changed_field_Id | uuid
| old_value | text
| new_value | text
| created_at | timestamp

### Pros
- Doesn't affect existing table
- No redundant data
- Good for when table has many fields, but only a few fields often changed

### Cons
- Need multiple records per change

### Other 

If there wasn't the requirement of needing to track history for a particular time in the past, versioning can be considered.

In this approach, we add a `version` field to our existing table, clients should always query the latest version for the current schedule.
There may be a separate table to track versions.

What is considered a new version though? When any fields changes? If so, different habits can have different versions, and that may be hard to manage.

| Column        | Data Type
| :------------- |:-------------
| id | uuid
| created_at | timestamp
| habit_name | text
| days_of_week | string
| schedule_type | enum
| duration | number
| active | boolean
| version | number

