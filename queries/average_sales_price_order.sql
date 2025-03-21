--  Average Sales Price per Order
SELECT 
    ORDERNUMBER,
    SUM(SALES) AS total_order_value,  -- Total revenue per order
    SUM(QUANTITYORDERED) AS total_items,  -- Total items in each order
    ROUND(SUM(SALES) / NULLIF(SUM(QUANTITYORDERED), 0), 2) AS avg_price_per_item  -- Average price per item
FROM sales_data
GROUP BY ORDERNUMBER
ORDER BY total_order_value DESC;
