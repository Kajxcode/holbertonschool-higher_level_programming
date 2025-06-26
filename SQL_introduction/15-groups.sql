-- script that lists number of records with same value
SELECT score, COUNT(*) AS NUMBER
FROM second_table
GROUP BY score
ORDER BY score ASC;