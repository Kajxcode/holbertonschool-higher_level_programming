-- script that lists number of records with same value
SELECT score, COUNT(*) AS NUMBER
FROM second_table
GROUP BY score
GROUP BY score ASC;