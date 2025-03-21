--  Total Quantity Sold per Month
SELECT 
    FORMAT(ORDERDATE, 'yyyy-MM') AS year_month,  -- Extracts Year-Month format
    SUM(QUANTITYORDERED) AS total_quantity      -- Total quantity sold per month
FROM sales_data
GROUP BY FORMAT(ORDERDATE, 'yyyy-MM')
ORDER BY year_month;





