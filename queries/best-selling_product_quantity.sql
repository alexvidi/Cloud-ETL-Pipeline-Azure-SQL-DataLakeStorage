--  Best-Selling Product by Quantity
SELECT TOP 1 PRODUCTCODE, SUM(QUANTITYORDERED) AS total_units_sold
FROM sales_data
GROUP BY PRODUCTCODE
ORDER BY total_units_sold DESC;

