-- script that lists number of records with same value
SELECT score, COUNT(*) AS COUNT
FROM second_table
GROUP BY score
HAVING COUNT(*) > 1;