# Go w/ PostgreSQL

## “Code-first” ORMs

Define structs/types in code first, then generate SQL from them. Reflection is heavily used.

| Lib | Description | Pros | Cons | Notes
|----------|--| --| --| -- |
| [Gorm](https://github.com/go-gorm/gorm) | The most popular go ORM | - Makes simple queries easier, reduces boilerplate code<br/>- Active enough community support ([gitter](https://gitter.im/jinzhu/gorm)), likely more organic Q&A activity available (eg. stackoverflow)<br/>- Actgively developed, many contributors | - Complicated for more complex queries (multiple joins, subqueries, etc)<br/>- Extra layer of abstraction magic<br/>- Heavier performance cost & memory footprint due to use of reflection<br/>- Need to pass a lot of empty interfaces, so harder to check for compile-time errors<br/>- Heavier weight | There’s an auto-migration tool, or [gormigrate](https://github.com/go-gormigrate/gormigrate) for more complex migrations.<br/><br/>To use with goose, there’s [Gorm-goose](https://github.com/Altoros/gorm-goose) (but not very active), or we can [DIY it](https://medium.com/@poorva.mahajan2990/use-goose-the-gorm-way-5c7d3b791b35).
| [ent](https://entgo.io/) | Open-source, newer, graph-based ORM, from Facebook ([blog post](https://entgo.io/blog/2019/10/03/introducing-ent/)) | <br/>- Code generation avoids type errors<br/>- Unclear if there’s still an FB team staffed around it, but at least FB may feel some degree of responsibility still for support | - Extra layer of abstraction magic<br/>- Active-seeming community support ([slack](https://app.slack.com/client/T029RQSE6/C01FMSQDT53)/discord), but less organic Q&A activity <br/>- Likely more of an initial learning curve with the ent-specific concepts<br/>- Heavier weight | - Has its own auto-migration tool, [Atlas](https://atlasgo.io/).<br/>- Can be used with goose<Br/>- Seems like a less standard model of mapping relational data. Not sure what the graph implications are. 
| [xorm](https://gitea.com/xorm/xorm) | A more performant ORM | - More performant than gorm<br/>- Lighter weight than the above, but still heavier than below options<br/>|- Seems heavily used by Chinese community, which is cool, but GH discussions mostly in Chinese



## “Database-first” ORMs
Define DB schema first, then generate structs/types in code from them.

| Lib | Description | Pros | Cons | Notes
|----------|--| --| --| -- |
| [SQL Boiler](https://github.com/volatiletech/sqlboiler)  | Generates type-safe code from DB tables | - DB is single source of truth<br/>- Easy fallback to raw SQL, or sqlx<br/>- More performant than the code-first ORMs |- Bugs seem a little slow to be addressed (based on skim of GH issues + responses )<br/>- Largely inspired by Rails’ ActiveRecord, which some think overly abstracts the DB<br/>- [Slack](https://sqlboiler.from-the.cloud/) channel doesn’t seem as active (0 out of 145 users were active at the time)<br/>- One main contributor | - Some chatter that it’s a nice middle ground over the lighter code generators or ORMs<br/>- Needs separate tool for migrations (eg. goose)

# Lighter Code Generators / SQL Builders
Adds a minimal layer that helps automate/reduce SQL boilerplate.  

| Lib | Description | Pros | Cons | Notes
|----------|--| --| --| -- |
| [sqlc](https://github.com/kyleconroy/sqlc)  | Generate type-safe code at compile time.<br/><br/>1. Write queries in SQL<br/>2. Run sqlc to generate the go code<br/>3. Write code to call generated code. | - Actively developed, very lightweight<br/>- Helps w/ reducing SQL boilerplate while being very explicit (less magic)<br/>- Generated code is simple/readable<br/>- What gets generated can be configured; doesn’t generate things don’t asked for<br/>- Popular choice in this category | - GitHub bugs actively triaged, but not necessarily fixed. Not sure if it’s just perception from the active triaging, but a lot of filed bugs.<br/>- Joins sound trickier, but can fallback<br/>- Has ‘fixed queries’ - something about making slight changes to a SQL statement requires a new query?<br/>- Can’t take an arbitrary number of params (eg. for multi-row inserts), but there are workarounds<br/>- One main contributor | - A step beyond what SQL builders like squirrel does.<br/>- Needs separate tool for migrations (eg. goose) <br/> - Sounds like can be used with sqlx if needed
| [jet](https://github.com/go-jet/jet) | Generates type-safe code at compile time. | Has the ability to easily convert DB query results into arbitrary structs. <br/>- Very actively maintained, very lightweight<br/>- Specifically aimed at closing a gap with traditional SQL builders: that it’s hard to unpack results from a join from 2+ tables when the join is not a  simple 1:1 | Less popularly used than other options<br/>- How it denormalizes data can be helpful but also may lead to queries driving the data model(?)<br/>- Doesn’t prevent developers from querying the DB sub-optimally | - A step beyond what SQL builders like squirrel does.<br/>- Needs separate tool for migrations (eg. goose)
| [squirrel](https://github.com/Masterminds/squirrel) | Generates SQL at runtime; a query builder.|- Seems like it enables slightly more dynamic SQL building<br/>| - In maintenance mode<Br/>- Bugs no longer actively addressed<br/> | - Often used in conjunction with sqlx<br/>- Helps build SQL queries via composable parts <br/>- Needs separate tool for migrations (eg. goose)
| [sqlx](https://github.com/jmoiron/sqlx) | Extensions on go's standard database/sql lib, essentially a light DB wrapper.| - Performant | <br/>- Seems less actively maintained now; many GitHub issues don’t get responses<Br/>- One main contributor  | - Often used in conjunction with squirrel<br/>- Needs separate tool for migrations (eg. goose)

## Raw SQL Libraries

| Lib | Description | Pros | Cons | Notes
|----------|--| --| --| -- |
| [database/sql](https://pkg.go.dev/database/sql) | Go’s standard library DB interface. The default minimal option. | - Lots of support<br/>- More performant at runtime | - The raw-est way<br/>- SQL queries are strings; verifying that they actually work requires lots of test coverage<br/> | Code should refer to types from database/sql only, not driver package directly to avoid coupling

## Postgres Drivers (additionally needed with most of the above options)
| Lib | Description | Pros | Cons | Notes
|----------|--| --| --| -- |
| [lib/pq](https://github.com/lib/pq) | Historically most popular PG driver for Go | - Battle-tested | - In maintenance mode; maintainers suggest pgx for new features/reliable bug support
| [pgx](https://github.com/jackc/pgx) | PostgreSQL driver and toolkit for Go. | - Actively maintained<br/>- Performant | - Adds little beyond basic query interface | Seems to be the clear driver choice




