-- Example SQL query for exploratory data analysis
SELECT column_name, COUNT(*), AVG(column_name), MAX(column_name), MIN(column_name)
FROM your_table_name
GROUP BY column_name;