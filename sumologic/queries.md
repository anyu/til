# Queries


```
_sourceCategory=MY_SOURCE_CATEGORY
| json "url","status"
| where url matches "/some/url"
| if (status matches /^4\d\d$/, 1,0) as ep_4xx
| if (status matches /^5\d\d$/,1,0) as ep_5xx
| timeslice 15m
|
sum(ep_4xx) as ep_4xxs_count,
sum(ep_5xx) as ep_5xxs_count,
count as request_count by _timeslice
| (ep_4xxs_count/request_count)*100 as ep_4xxs_percent
| (ep_5xxs_count/request_count)*100 as ep_5xxs_percent
| where (request_count < 100 and ep_5xxs_count > 10) OR
        (request_count >= 100 and ep_5xxs_percent > 3)
| where (request_count >= 100 and request_count < 500 and (ep_5xxs_count > 10 or ep_4xxs_count > 30)) or
        (request_count >= 500 and (ep_5xxs_percent > 3 or ep_4xxs_percent > 8))
```

AVG/LOW/HIGH REQUEST COUNT
```
| avg(request_count) as avg_req_count,
  pct(request_count, 50) as median_req_count,
  min(request_count) as lowest_req_count,
  max(request_count) as highest_req_count
```

AVG, MEDIAN ERROR COUNT > 0
```
| where ep_5xxs_count > 0
| avg(ep_5xxs_count) as avg_5xxs_count,
  pct(ep_5xxs_count, 50) as median_5xx_count
  ```

MEDIAN ERROR COUNTS > THRESHOLD
```
| where ep_5xxs_count > 20
| pct(ep_5xxs_count, 50) as median_5xx_count,
 avg(ep_5xxs_ratio) as avg_5xxs_ratio,
  pct(ep_5xxs_ratio, 50) as median_5xxs_ratio
  ```
