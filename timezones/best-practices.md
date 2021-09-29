# Timezone best practices

- Use UTC for anything other than presentation logic
  - OS timezone settings
  - datetime values in DBs
- Use unambiguous datetime representations -- either epoch timestamp or a [ISO-8061](https://en.wikipedia.org/wiki/ISO_8601) format with UTC specified, `YYYY-MM-DDTHH:mm:ssZ`.
  - `T` = separator for time
  - `Z` = Zero timezone; it's offset by 0 from the Coordinated Universal Time (UTC). Denotes UTC.
- Use datetime libraries instead of writing your own
