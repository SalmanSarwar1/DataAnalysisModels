-- Example SQL query for basic aggregation
SELECT category, SUM(sales) AS total_sales
FROM your_table_name
GROUP BY category;