# Performance Tuning Report

## Baseline Profiling
I ran an `EXPLAIN ANALYZE` on the Month-Over-Month growth query. The database had to perform a full sequential scan on the `orders` table to aggregate by `orderdate`, which resulted in a higher execution time.

## Strategic Indexing
To optimize the aggregation, I implemented a B-Tree index on the `orderdate` column in the source `orders` table, as date-based filtering and grouping are heavily utilized in the advanced analytical queries.

**SQL Executed:**
`CREATE INDEX idx_orders_orderdate ON public.orders(orderdate);`

## Performance Improvements
After applying the index, rerunning the `EXPLAIN ANALYZE` showed that the query planner utilized an Index Scan rather than a Sequential Scan. This significantly reduced the execution time and lowered the overall cost of the query, making the analytical pipeline more efficient for the Star Schema.