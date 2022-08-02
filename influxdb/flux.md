# Flux

Flux is InfluxDB's open source 'functional data scripting language'.

Supports: InfluxDB, MySQL, PostgreSQL, CSV.

## Query structure

Filter -> shape -> process.

```
from(bucket: "example-bucket")              // ── Source
    |> range(start: -1d)                    // ── Filter on time
    |> filter(fn: (r) => r._field == "foo") // ── Filter on column values
    |> group(columns: ["sensorID"])         // ── Shape
    |> mean()                               // ── Process
```

- **filter** functions iterate over each input; only rows that meet the condition is included in the output.
  - eg. `range`, `filter`
- shaping functions modify the structure of data in prep for processing
  - eg. `group`, `window`, `pivot`, `drop`, `keep`
- processing can be aggregating data, selecting specific data, rewriting rows, sending notifications.
  - eg. `count`, `mean`, `first`, `map`

### Resources
- https://docs.influxdata.com/flux/v0.x/get-started/query-basics/