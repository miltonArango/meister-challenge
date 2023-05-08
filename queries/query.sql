-- Assuming we need to analyze the last 29 days from the current date.

SELECT country
FROM mytable
WHERE registration_date >= current_date - interval '29 day'
GROUP BY country
HAVING COUNT(DISTINCT user_id) > 500
AND (MAX(DISTINCT user_id) - MIN(DISTINCT user_id)) / AVG(DISTINCT user_id) <= 0.05 OR (MAX(DISTINCT user_id) - MIN(DISTINCT user_id)) / AVG(DISTINCT user_id) >= 0.25;
