-- BigQuery Query
SELECT country
FROM `mytable`
WHERE registration_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 29 DAY)
GROUP BY country
HAVING COUNT(DISTINCT user_id) > 500
  AND ((MAX(DISTINCT user_id) - MIN(DISTINCT user_id)) / AVG(DISTINCT user_id)) <= 0.05 OR ((MAX(DISTINCT user_id) - MIN(DISTINCT user_id)) / AVG(DISTINCT user_id)) >= 0.25;